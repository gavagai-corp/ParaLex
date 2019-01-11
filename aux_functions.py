import csv
import os
import argparse
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec


def paradigmatic_neighbours(word, model_under_evaluation):
    return [word for word, _ in model_under_evaluation.most_similar(word, topn=30)]


def read_csv(filename='ParaLex.csv'):
    output = []
    with open(filename) as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            output.append([term.strip() for term in line if term != ''])
    return output[1:]


def load_language_specific_data(language):
    data_sheet = read_csv()
    if len(language) > 3:  # language name
        selection_column = 1
    else:  # language code
        selection_column = 0
    rows = [row for row in data_sheet if row[selection_column] == language.upper()]
    if len(rows) == 0:
        raise Exception('Language not found')
    output = {}
    for row in rows:
        output[row[2]] = row[3:]
    return output


def load_model(file, format_flag):
    if format_flag == 'binary':
        model = KeyedVectors.load_word2vec_format(file, binary=True, encoding='utf8')
    elif format_flag == 'glove':
        w2v_file = file[:-4] + '.w2v.txt'
        if w2v_file in os.listdir():
            pass
        else:
            glove2word2vec(file, w2v_file)
        model = KeyedVectors.load_word2vec_format(w2v_file, binary=False, encoding='utf8')
    else:
        model = KeyedVectors.load_word2vec_format(file, binary=False, encoding='utf8')
    return model


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_model", help="the path of the model you wish to evaluate")
    parser.add_argument("model_format", help="the format of the model you are evaluating")
    parser.add_argument("language", help="the language of the model")
    args = parser.parse_args()
    print(args)
