import os
from string import punctuation
from collections import Counter
import argparse


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="ansi") as text_file:
            return text_file.read()
    else:
        return None


def get_most_frequent_words(normalized_text):
    top_words_count = 10
    return Counter(normalized_text.split(" ")).most_common(top_words_count)


def normalize_text(text):
    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text.lower()


def get_args():
    parser = argparse.ArgumentParser(description="Enter the path directory:")
    parser.add_argument("-file", required=True, help="Path to file")
    return parser.parse_args()


if __name__ == '__main__':
    path_to_file = get_args().file
    text_from_file = load_data(path_to_file)
    if text_from_file is None:
        exit("File not found")
    else:
        print(get_most_frequent_words(normalize_text(text_from_file)))
