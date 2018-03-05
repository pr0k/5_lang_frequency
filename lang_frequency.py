import re
import argparse


def args_from_parser():
    parser = argparse.ArgumentParser(
        'shows the most commonly used words in the text in descending order\n'
    )
    parser.add_argument(
        'text_file',
        help='specify ../*.txt',
        type=str,
    )
    parser.add_argument(
        '-c',
        '--count',
        help='number of output words, default=10',
        default=10,
        type=int,
    )
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def remove_characters(text):
    pattern = re.compile('[^\w ]')
    return pattern.sub(' ', text)


def get_frequency_of_words(text):
    text = text.lower().split()
    text_words = {}
    for word in text:
        if word not in text_words:
            text_words[word] = text.count(word)
    return [word for word in sorted(
                list(text_words.items()),
                key=lambda pair: pair[1],
                reverse=True,
                )
            ]


def print_most_frequent_words(list_of_words, count):
    print('\nWord:\n')
    for i in range(count):
        print(
            '{0:15} \tis meets {1} times'.format(
                list_of_words[i][0],
                list_of_words[i][1],
            )
        )


if __name__ == '__main__':
    try:
        args = args_from_parser()
        print_most_frequent_words(
            get_frequency_of_words(
                remove_characters(
                    load_data(
                        args.text_file
                    )
                )
            ),
            args.count,
        )
    except IndexError:
        print(
            '\nwarning: there are less '
            '{} words included in the text!'.format(args.count)
        )
    except ValueError:
        print(
            '\nerror:\tthere is no text in the file '
            '<{}>\nspecify the text data file'.format(args.text_file)
        )
    except FileNotFoundError:
        print(
            '\nerror:\tfile is not found\ntry:\t$ python lang_frequency.py '
            'path/to/text/file/*.* [-c COUNT]'
        )
