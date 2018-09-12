import argparse
import re
from collections import Counter


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Input path to the analysed file')

    parser.add_argument(
        'filepath',
        help='Path to text file')

    args = parser.parse_args()
    return args


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            print(filepath)
            text_str = file_handler.read()
        return text_str
    except FileNotFoundError:
        return None


def remove_punctuation(text_str):
    clean_text_str = re.sub(r'[^\w]', ' ', text_str)
    return clean_text_str


def no_words_check(clean_text_str):
    no_spaces = clean_text_str.replace(" ", "")
    if len(no_spaces) == 0:
        return True

def tokenize(text_str):
    if text_str is not None:
        wordlist = text_str.lower().split()
        return wordlist
    else:
        return None


def get_words_frequency(wordlist):
    most_common_words_counts_list = Counter(wordlist).most_common(10)
    return most_common_words_counts_list


def pretty_print_words_list(words_counts_list):
    list_len = len(words_counts_list)
    if list_len < 10:
        print('There are only {} different words in text'.format(
                                                list_len))
    print('Top {} most frequent words in file:'.format(list_len))
    for word in words_counts_list:
        print('{}: {}'.format(word[0], word[1]))


if __name__ == '__main__':
    args = get_parser_args()
    text_str = load_data(args.filepath)
    if text_str is None:
        exit('File is not found')
    clean_text_str = remove_punctuation(text_str)
    if no_words_check(clean_text_str):
        exit('There are no words in the file')
    wordlist = tokenize(clean_text_str)
    top_10_frequent_words = get_words_frequency(wordlist)
    pretty_print_words_list(top_10_frequent_words)
