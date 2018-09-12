import argparse
import re


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Input path to the analysed file')

    parser.add_argument(
        'filepath',
        help='Path to text file')

    args = parser.parse_args()
    return args

def load_data(filepath):
    file = open(filepath)
    text_str = file.read()
    return text_str


def remove_punctuation(text_str):
    clean_text_str = re.sub(r'[^\w]', ' ', text_str)
    return clean_text_str

def tokenize(text_str):
    if text_str is not None:
        wordlist = text_str.lower().split()
        return wordlist
    else:
        return None

def get_words_frequency_dict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    frequency_dict = dict(zip(wordlist, wordfreq))
    return frequency_dict


def get_top_10_frequent_words(frequency_dict):
    top_10_list = sorted(
        frequency_dict.items(),
        key=lambda x: x[1],
        reverse = True)[:10]
    return top_10_list


def pretty_print_list_of_tuples(top_10_list):
    print('Top 10 most frequent words in file:')
    for i in top_10_list:
        print('{}: {}'.format(i[0], i[1]))


if __name__ == '__main__':
    args = get_parser_args()
    text_str = load_data(args.filepath)
    if text_str is None:
        exit('Failed to load file')
    clean_text_str = remove_punctuation(text_str)
    wordlist = tokenize(clean_text_str)
    frequency_dict = get_words_frequency_dict(wordlist)
    top_10_list = get_top_10_frequent_words(frequency_dict)
    pretty_print_list_of_tuples(top_10_list)
