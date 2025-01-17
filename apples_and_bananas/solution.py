#!/usr/bin/env python3

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel(s) allowed',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text = args.text
    vowel = args.vowel

    if os.path.isfile(text):
        text = open(text).read()

    # Method 1: Iterate every character
    # new_text = []
    # for char in text:
    #     if char in 'aeiou':
    #         new_text.append(vowel)
    #     elif char in 'AEIOU':
    #         new_text.append(vowel.upper())
    #     else:
    #         new_text.append(char)
    # text = ''.join(new_text)

    # Method 2: str.replace
    # for v in 'aeiou':
    #     text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    # Method 3: Use a list comprehension
    # new_text = [
    #     vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    #     for c in text
    # ]
    # text = ''.join(new_text)

    # Method 4: Define a function, use list comprehension
    def new_char(c):
        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c

    # text = ''.join([new_char(c) for c in text])

    # Method 5: Use a `map` to iterate with a `lambda`
    # text = ''.join(
    #     map(
    #         lambda c: vowel if c in 'aeiou' else vowel.upper()
    #         if c in 'AEIOU' else c, text))

    # Method 6: `map` with the function
    text = ''.join(map(new_char, text))

    # Method 7: Regular expressions
    # text = re.sub('[aeiou]', vowel, text)
    # text = re.sub('[AEIOU]', vowel.upper(), text)

    print(text.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
