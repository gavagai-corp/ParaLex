from __future__ import print_function, division
from gensim.models import Word2Vec
# from gensim.models.keyedvectors import KeyedVectors
from random import shuffle  # A function to randomly shuffle a list.
import os  # A library to interface with the operating system.
import sys
from time import time
from collections import Counter
from numpy import mean, std, var
from itertools import combinations as choose
import io


# from api_functions import paradigmatic_neighbours
# our_dataset = ['en/'+f for f in os.listdir('en')]


def paradigmatic_neighbours(word):
    return [word for word, _ in model.most_similar(word, topn=30)]


def seed_suggestions_fancy(seeds):
    suggestions = Counter()
    for seed in seeds:
        neighbours = paradigmatic_neighbours(seed)
        for neigh in neighbours:
            if neigh not in seeds:
                suggestions[neigh] += 1
    return suggestions


def get_words_from_cluster_file(filename):
    """An administrative function to read each cluster file in the data set and return the first eight items as a list.
    The remaining items are outliers, not related to this task."""
    with io.open(filename, mode='rU', encoding='utf-8') as f:
        output = []
        for line in list(f):  # Took away the chop of 8 here
            spaced_line = line.strip().lower().replace(' ',
                                                       '_')  # Some admin for multi-word expressions. Normalise to lowercase. Strip newline characters.
            output.append(spaced_line)
    return output


def cluster_permutations(list_of_words):
    permutations = []
    seed_combinations = choose(list_of_words, 2)
    for seed_comb in seed_combinations:
        corresponding_targs = [word for word in list_of_words if word not in seed_comb]
        permutations.append((list(seed_comb), corresponding_targs))
    return permutations


def cluster_test(cluster_words, threshold=2):
    """Takes a cluster as a list of words, gets all permutations and calls permutation_test for each permutation."""
    perm_scores = []
    all_possibilities = cluster_permutations(cluster_words)
    for poss in all_possibilities:
        perm_score = permutation_test(poss[0], poss[1], threshold)
        perm_scores.append(perm_score)
    return round(mean(perm_scores), 2), round(std(perm_scores), 2), round(var(perm_scores), 2)


def permutation_test(seeds, targets, threshold=2):
    print("Seeds:", seeds, "Targets:", targets)
    current_suggestions = seed_suggestions_fancy(seeds)
    current_suggestions_vocab = current_suggestions.keys()

    iteration = 0
    # print(seeds)
    # print("Initially yields: ", len(current_suggestions),"suggestions")
    # print(current_suggestions)
    new_targets_found = [target for target in targets if target in current_suggestions_vocab]
    # print('ntf',new_targets_found)
    current_score = round(len(new_targets_found) / len(targets), 2)  # Percentage of targets in suggestions.
    # print("Initial Score: ",current_score) # From initial suggestions, before any incorporating.

    if current_score > 0.99:
        # print("Perfect score on this cluster without iterating.")
        return 1

    else:
        while iteration < 3:  # For each iteration.

            # Accept filtered suggestions according to some criteria:
            suggestions_to_accept = [term for term in current_suggestions if current_suggestions[term] >= threshold]
            # Also add targets found in the most recent iteration, in case these don't meet criteria.
            suggestions_to_accept += new_targets_found

            seeds.extend(suggestions_to_accept)

            seeds = list(set(seeds))  # Controlling for accidental duplicates.

            iteration += 1  # Increase count variable.

            # print("\nIter #:",iteration)
            # print("Currently {0} seeds.".format(len(seeds)))
            # print(seeds) # Can be uncommented for further inspection.

            current_suggestions = seed_suggestions_fancy(seeds)
            current_suggestions_vocab = current_suggestions.keys()

            # print("Currently yielding", len(current_suggestions),"suggestions.")
            # print(current_suggestions) # Can be uncommented for further inspection.

            if len(current_suggestions) > 200:  # Controlling for too many suggestions. Generously.
                # print("Too many suggestions to be sensible.")
                return current_score

            new_targets_found = [target for target in targets if target in current_suggestions_vocab]
            # print('ntf',new_targets_found)
            current_score += round(len(new_targets_found) / len(targets), 2)
            # print("Current Score: ",current_score)

            if current_score > 0.99:
                # print("Perfect score on this cluster at iteration #{0}.".format(iteration))
                return 1

        return current_score


def cluster_sanity_check(cluster):
    initial_words = get_words_from_cluster_file(cluster)
    final_words = []
    for word in initial_words:
        if word in model.vocab:
            #        if len(paradigmatic_neighbours(word,lang)) > 0:
            final_words.append(word)
    if len(final_words) >= 3:
        return True, final_words
    else:
        return False, []


def iter_sug_test_with_seed_coherence(list_of_clusters, threshold):
    """An implementation of the test filtering suggestions by coherence with current seeds.
    Takes a list of clusters, a number of initial seeds and a threshold of coherence.
    Carries out the test for 5 iterations, printing the cumulative recall at each iteration.
    Unlike the previous implementation, no filering functions are needed - it's all built in."""

    cluster_progress = 0
    total_clusters = len(list_of_clusters)
    scores = []
    cluster_scores = []
    for clust in list_of_clusters:
        cluster_progress += 1
        print('\n\n---NEW CLUSTER---\n#{0} of {1}:\n'.format(cluster_progress, total_clusters))
        check, good_words = cluster_sanity_check(clust)
        if check:
            clust_score, clust_std, clust_var = cluster_test(good_words, threshold)
            print('Mean Cluster score:', clust_score)
            print('Cluster Variance:', clust_var)
            print('Cluster SD:', clust_std)
            scores.append(clust_score)
            cluster_scores.append((clust, clust_score, clust_var, clust_std))

        else:
            print('Cluster skipped.')

    overall_test_score = round(sum(scores) / total_clusters, 2)
    clusters_skipped = total_clusters - len(scores)

    return overall_test_score, clusters_skipped, cluster_scores


def pretty_print(test_results):
    overall_test_score, clusters_skipped, cluster_scores = test_results

    print('\n\n---INFO---\n\nOverall Test Score:', overall_test_score)

    print('{0} clusters skipped'.format(clusters_skipped))

    print('\nSTATS', sys.argv[1:], '\n')
    for tup in cluster_scores:
        print(tup[0], '\t', tup[1], '\t', tup[2], '\t', tup[3])


if __name__ == '__main__':
    if sys.argv[2] == '-t':
        # model = KeyedVectors.load_word2vec_format(sys.argv[1], binary=False)
        model = Word2Vec.load_word2vec_format(sys.argv[1], binary=False, encoding='utf8')
    elif sys.argv[2] == '-b':
        model = Word2Vec.load_word2vec_format(sys.argv[1], binary=True, encoding='utf8')
    lang = sys.argv[3]
    # argv 1=vecs, 2=vec_format, 3=lang in GavFormat
    our_dataset = ['testData/' + lang + '/' + f for f in os.listdir('testData/' + lang + '/')]
    # our_dataset = our_dataset + ['testData2/'+lang+'/'+f for f in os.listdir('testData2/'+lang+'/')]
    results = iter_sug_test_with_seed_coherence(list_of_clusters=our_dataset, threshold=2)
    pretty_print(results)