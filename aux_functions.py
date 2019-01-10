import csv
import os
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
# from api_functions import paradigmatic_neighbours


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
    if format_flag == '-b':
        model = KeyedVectors.load_word2vec_format(file, binary=True, encoding='utf8')
    elif format_flag == '-g':  # glove format_flag
        w2v_file = file[:-4] + '.w2v.txt'
        if w2v_file in os.listdir():
            pass
        else:
            glove2word2vec(file, w2v_file)
        model = KeyedVectors.load_word2vec_format(w2v_file, binary=False, encoding='utf8')
    else:
        model = KeyedVectors.load_word2vec_format(file, binary=False, encoding='utf8')
    return model
