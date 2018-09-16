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


def check_no_words(clean_text_str):
    no_spaces = clean_text_str.replace(' ', '')
    if not len(no_spaces):
        return True


def split_text_str(text_str):
    if text_str is None:
        return None
    else:
        wordlist = text_str.lower().split()
        return wordlist


def get_most_common_words_dict(wordlist, display_count):
    top_words_counts_list = Counter(wordlist).most_common(display_count)
    top_words_counts_dict = {}
    for word in top_words_counts_list:
        top_words_counts_dict[word[0]] = word[1]
    return top_words_counts_dict


def pretty_print_words_list(top_N_frequent_words, display_count):
    list_len = len(top_N_frequent_words)
    if list_len < display_count:
        print('There are only {} different words in text'.format(list_len))
    print('Top {} most frequent words in file:'.format(list_len))
    for key, value in top_N_frequent_words.items():
        print('{}: {}'.format(key, value))


if __name__ == '__main__':
    args = get_parser_args()
    text_str = load_data(args.filepath)
    display_count = args.display_count
    if text_str is None:
        exit('File is not found')
    clean_text_str = remove_punctuation(text_str)
    if check_no_words(clean_text_str):
        exit('There are no words in the file')
    wordlist = split_text_str(clean_text_str)
    top_N_frequent_words = get_most_common_words_dict(wordlist, display_count)
    pretty_print_words_list(top_N_frequent_words, display_count)
