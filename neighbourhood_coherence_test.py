from __future__ import print_function, division
from aux_functions import paradigmatic_neighbours, load_language_specific_data, load_model, parse_arguments


def test_cluster(cluster_words, model_under_evaluation):
    max_score = (len(cluster_words) - 1) * len(cluster_words)
    score = 0
    for word in cluster_words:
        try:
            neighbourhood = paradigmatic_neighbours(word, model_under_evaluation)
            score += sum(1 for word in cluster_words if word in neighbourhood)
        except:
            pass
    cluster_score = round(score/max_score, 2)
    print(cluster_score)
    return cluster_score


def neighbourhood_coherence_test(evaluation_data, model_under_evaluation):
    results = []
    for cluster in sorted(evaluation_data.keys()):
        print(cluster, end= ': ')
        results.append(test_cluster(evaluation_data[cluster], model_under_evaluation))
    return round(sum(results)/len(results),2)


def main():
    path_to_model, model_format, language = parse_arguments()
    model = load_model(path_to_model, model_format)
    language_data = load_language_specific_data(language)
    result = neighbourhood_coherence_test(language_data, model)
    print('Final score:', result)


if __name__ == "__main__":
    main()
