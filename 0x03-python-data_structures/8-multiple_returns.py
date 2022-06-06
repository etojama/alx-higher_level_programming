#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        result = (0, None)
        return result
        # sentence[0] = None
    else:
        str_len = (len(sentence), sentence[0:1])
        return str_len
