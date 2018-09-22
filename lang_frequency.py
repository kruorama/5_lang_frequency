import argparse
import re
from collections import Counter


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Input path to the analysed file')

    parser.add_argument(
        '-f',
        '--filepath',
        help='Path to text file',
        required=True)

    parser.add_argument(
        '-c',
        '--display_count',
        help='Number of top frequent words to display',
        type=int,
        default=10)

    args = parser.parse_args()
    return args


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            text_str = file_handler.read()
        return text_str
    except FileNotFoundError:
        return None


def remove_punctuation(text_str):
    clean_text_str = re.sub(r'[^\w]', ' ', text_str)
    return clean_text_str


def check_empty_string(clean_text_str):
    str_without_spaces = clean_text_str.replace(' ', '')
    return not str_without_spaces


def split_text_str(text_str):
    if text_str is None:
        return None
    else:
        wordlist = text_str.lower().split()
        return wordlist


def get_most_common_words(wordlist, display_count):
    most_frequent_words = Counter(wordlist).most_common(display_count)
    return most_frequent_words


def pretty_print_words_list(most_frequent_words, display_count):
    list_len = len(most_frequent_words)
    if list_len < display_count:
        print('There are only {} different words in text'.format(list_len))
    print('Top {} most frequent words in file:'.format(list_len))
    for word, count in most_frequent_words:
        print('{}: {}'.format(word, count))


if __name__ == '__main__':
    args = get_parser_args()
    text_str = load_data(args.filepath)
    display_count = args.display_count
    if text_str is None:
        exit('File is not found')
    clean_text_str = remove_punctuation(text_str)
    if check_empty_string(clean_text_str):
        exit('There are no words in the file')
    wordlist = split_text_str(clean_text_str)
    most_frequent_words = get_most_common_words(wordlist, display_count)
    pretty_print_words_list(most_frequent_words, display_count)
