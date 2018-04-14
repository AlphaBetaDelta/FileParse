# FileParse
Reads in a file of English text, and then shows a list of the most common words in the file.

### Features

`usage: word_count [-h] [-json] [-version] filename`

Counts unique words in a file, outputs common (default)
or all words (-json option flag).

##### positional arguments:

`filename      filename`

##### optional arguments:
>  -h, --help    show this help message and exit
  -json         output json list of the words and their frequency
  -version, -v  show program's version number and exit

##### Example output of common words when -json arg is NOT provided:
 lend - 156
    shown - 78

##### Example output of all words when -json arg is provided:
 {"bleed": 1, "showne": 1, "finis": 1, ...}


### Full Description

 Counts unique words in a file, can output common or all words.

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
 if run with files with letters with diacritics. Input files are assumed
 to be English text.

##### Usage:
 `python word_count.py -json (optional for json output) input_filename`

##### Example output to stdout when -json arg is NOT provided:
  lend - 156
     shown - 78
        ...

##### Output to stdout when -json arg is provided:
 {"bleed": 1, "showne": 1, "finis": 1, ...}

##### Args:

>    json_flag (string): If the first argument is "-json" then the
        output will be a single string of a json list of the words and
        their frequency. If "-json" is NOT set then the output will be
        only the most common words in repeated lines of, e.g., 
        "bleed - 1".

>    filename (string): The name of the ASCII or UTF-8 encoded text
            file to parse.

##### Execution:

`python word_count.py henry_V.txt`
      or
 `python word_count.py -json henry_V.txt`

##### Test-suite:
 `python test_suite.py`

##### Python version:
  `Python 3.6.5`
