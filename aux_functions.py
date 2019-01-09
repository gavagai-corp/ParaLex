import csv


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
