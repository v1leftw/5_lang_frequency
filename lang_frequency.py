import os
from collections import Counter
import argparse
import codecs
import re

'''
two try blocks with same exception 
to be sure to read the file on any encoding.
Actually I don't know have to handle this encoding operations.
Maybe be you can suggest something? :)
Works:
UTF-8
ANSI
UNICODE

RUSSIAN
ENGLISH
FRENCH
ARABIC
'''


def load_data(filepath):
    if os.path.isfile(filepath):
        try:
            with codecs.open(filepath, "r", encoding="utf-8") as text_file:
                return text_file.read()
        except UnicodeDecodeError:
            try:
                with codecs.open(filepath, "r") as text_file:
                    return text_file.read()
            except UnicodeDecodeError:
                exit("Can't read the file")


def get_most_frequent_words(normalized_text):
    top_words_count = 10
    return Counter(normalized_text.split(" ")).most_common(top_words_count)


def normalize_text(text):
    text = re.sub("[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]", "", text)
    return text.lower()


def get_args():
    parser = argparse.ArgumentParser(description="Enter the path directory:")
    parser.add_argument("-file", required=True, help="Path to file")
    return parser.parse_args()


if __name__ == "__main__":
    path_to_file = get_args().file
    text_from_file = load_data(path_to_file)
    if text_from_file is None:
        exit("File not found")
    else:
        print("Top words:")
        top_words = get_most_frequent_words(normalize_text(text_from_file))
        for elem in top_words:
            print(elem[0], "-", elem[1])
