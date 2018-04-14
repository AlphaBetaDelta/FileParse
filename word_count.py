#!/usr/bin/python

import sys
import re
import json
from pathlib import Path
import unicodedata
import math
import argparse
from argparse import RawTextHelpFormatter


def main():
    """Parses inputs and call word_counter().

    This program will not work and will produce incorrect results
    if run with files with letters with diacritics. Also,
    text file formats must be UTF-8, not ANSI encoded.
    This program will not work and will produce incorrect results
    if run with files with letters with diacritics.

    Usage: -json (optional for json output) input_filename

    If usage is incorrect usage instructions are provided to stdout
    as an aid.

    Args:
        sys.argv: list of strings inputs

    Returns:
        True if usage is correct
    """

    # This program will not work and will produce incorrect results
    # if run with files with letters with diacritics.
    parser = argparse.ArgumentParser(
        description='Counts unique words in a file, outputs common (default)\n'
                    'or all words (-json option flag).',
        prog='word_count',
        epilog='Example output of common words when -json arg is NOT provided:\n'
               '    lend - 156\n'
               '    shown - 78\n'
               '\n'
               'Example output of all words when -json arg is provided:\n'
               '    {"bleed": 1, "showne": 1, "finis": 1, ...}\n',
        formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '-json',
        action='store_false',   # default is false
        help='output json list of the words and their frequency')

    parser.add_argument(
        'filename',
        help='filename')

    parser.add_argument(
        '-version', '-v',
        action='version',
        version='%(prog)s 1.0')

    args = parser.parse_args()

    if args.json:
        word_counter(json_flag=True, filename=args.filename)
    else:
        word_counter(json_flag=False, filename=args.filename)

    # json_flag = False

    # len_args = len(sys.argv)

    # # Parse input arguments
    # if len_args > 3:
    #     print("Usage: -json (optional for json output) input_filename")
    #     return -1
    # elif len_args > 2:
    #     if sys.argv[1] == '-json':
    #         json_flag = True
    #         filename = sys.argv[2]
    #     elif sys.argv[2] != '-json':
    #         print("Usage: -json (optional for json output) input_filename")
    #         return -1
    # elif len_args > 1:
    #         filename = sys.argv[1]
    # else:
    #     print("Usage: -json (optional for json output) input_filename")
    #     return False

    # word_counter(json_flag, filename)

    return True


def word_counter(json_flag, filename):
    """Counts unique words in a file, can output common or all words.

    The occurrence of words (case is ignored) is counted. The output
    is to stdout in a form similar to a histogram or frequency chart.
    The output is the unique word in the input file followed by the
    number of occurrences, i.e., "word = {number of occurrences}".
    One word per line is listed.

    For the default operation only the most common words are output,
    which is defined as words that occur with a percentage > 0.1%
    of the words in the file. With the -json option all words and
    their frequency are output.
   
    This program will not work and will produce incorrect results
    if run with files with letters with diacritics. Input files 
    are assumed to be English text.

    Example output to stdout when -json arg is NOT provided:
        lend - 156
        shown - 78
        ...

    Output to stdout when -json arg is provided:
        {"bleed": 1, "showne": 1, "finis": 1, ...}

    Args:
        json_flag (string): If the first argument is "-json" then the
        output will be a single string of a json list of the words and
        their frequency. If "-json" is NOT set then the output will be
        only the most common words in repeated lines of, e.g., 
        "bleed - 1".

        filename (string): The name of the ASCII or UTF-8 encoded text
            file to parse.

    Returns:
        True for success
    """

    # read in file
    contents = Path(filename).read_text()

    contents = contents.lower()

    # Find words that contain "'"" or "-", or words that do not
    words = re.findall("(?=\S*['-])[a-z'-]+|[a-z]+", contents)    
    
    adict = {}

    # Iterate through words and count occurrences,
    # save in dictionary with the word as the key.
    for key in words:
        adict[key] = adict.get(key, 0) + 1

    default_dict = {}

    len_words = len(words)

    # Iterate through words and save for default output if the word 
    # occurrence is > 0.1% of the words in the file.
    if len_words > 0:       
        for key in words:
            if adict[key]/len_words > 0.001:
                default_dict[key] = adict[key]

    # create list of dictionary keys
    default_keys = default_dict.keys()

    # output results (adict) to stdout
    if json_flag:
        if adict:
            print(json.dumps(adict))
    elif default_dict:
        #  print word and their respective frequency
        for key in default_keys:
            print("%s - %d" % (key, default_dict[key]))

    return True

if __name__ == "__main__":
    # Runs main function
    #   Enables the use of function word_counter as an imported module
    # Returns:
    #    The return value. True for success, False otherwise.
    #
    main()
