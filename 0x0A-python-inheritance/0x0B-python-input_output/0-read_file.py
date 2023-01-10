#!/usr/bin/python3
"""
read_file function
"""


def read_file(filename=""):
    """reads a txt file (UTF*) and prints it to stdout"""

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        print(data, end='')
