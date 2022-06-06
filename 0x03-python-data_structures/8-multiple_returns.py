#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    else:
        str_len = len(sentence) and sentence[0]
        return str_len
