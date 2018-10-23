import os
from collections import Counter
import argparse
import re
from string import punctuation


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r") as text_file:
            return text_file.read()


def get_most_frequent_words(raw_text):
    top_words_count = 10
    return Counter(raw_text.split(" ")).most_common(top_words_count)


def normalize_text(text):
    raw_text = re.sub(r'[{}]'.format(punctuation), "", text)
    return raw_text.lower()


def get_args():
    parser = argparse.ArgumentParser(description="Enter the path directory:")
    parser.add_argument("-file", required=True, help="Path to file")
    return parser.parse_args()


if __name__ == "__main__":
    path_to_file = get_args().file
    text_from_file = load_data(path_to_file)
    if text_from_file is None:
        exit("File not found")
    print("Top words:")
    top_words = get_most_frequent_words(normalize_text(text_from_file))
    print(top_words)
    for word, count in top_words:
        print(word, "-", count)
