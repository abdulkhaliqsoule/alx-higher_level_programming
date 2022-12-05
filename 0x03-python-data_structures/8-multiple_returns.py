#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with length of a string and first character
    Args:
        sentence: sentence
    Returns:
        tuple with length of string and its first character
    """
    length = len(sentence)
    first_character = sentence[0]
    if sentence == "":
        first_character = None
    return ((length, first_character))
