#!/usr/bin/python3

def no_c(my_string):
    return my_string.translate({ord('c'): None}) and my_string.translate({ord('C'): None})
