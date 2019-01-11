![Gavagai](gavagai.png)

# ParaLex
ParaLex is a data set of paradigmatic term clusters in multiple languages, intended as a resource for evaluating word spaces and other semantic similarity models.

The dataset consists of thematic word lists that represent a number of different semantic 
paradigms, such as days of the week, months of the year and common fruit and vegetables. 
The evaluation data has been translated to more than 45 different languages.

Source code to run the suggested evaluation methodologies is also available.


## Download

The data set is available as a CSV file [here](ParaLex.csv).

## Running the Evaluation Package

Clone this directory to the machine you want to run the evaluation on.

There are two evaluation scripts: neighbourhood_coherence_test.py and suggestion_test.py.

For help on running the the scripts, call them with a help flag -h:

python3 neighbourhood_coherence_test.py -h

Some typical usage examples would be:

python3 vector_file.txt EN
python3 glove_vector_file.txt EN -f glove

The default input format for a model is a Word2Vec text file. Glove format text files and binary files are also accepted
using the relevant flags. 

## Contribute

While we will work to extend the data set to include new languages, and more paradigmatic clusters,
we encourage anyone in the field to contribute to the data set. You can do so by following the [common
GitHub workflow](https://guides.github.com/introduction/flow/): fork the project, make changes to 
it according to [these instructions](ANNOTATION_INSTRUCTIONS.md), and submit a pull request.

## License and attribution

The data set licensed under [Apache License 2.0](ParaLex/LICENSE).

When referring to the ParaLex data set, please cite this publication

    @paper{sumbler2018paralex,
        author = {Peter Sumbler and Fredrik Olsson and Nina Viereckel and Lars Hamberg and Jussi Karlgren and Maria Verbitskaya and Magnus Sahlgren},
        title = {ParaLex: A Multilingual Resource for Evaluating Semantic Similarity Models},
        conference = {In preparation},
        year = {2018},
        pages = {},
        keywords = {Semantic Similarity; Evaluation; Lexical Resources; Word Embeddings; Multilingual Resources},
        url = {}
    }

## About Gavagai

[Gavagai](http://gavagai.se/) is a Swedish language technology company spun off from the 
Swedish Institute of Computer Science. Gavagai builds services such 
as [the Gavagai Explorer](https://explorer.gavagai.se/), 
and [the Gavagai Monitor](http://monitor.gavagai.se/).
