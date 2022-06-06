#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)

    if lena < 1:
        tuple_a = (0, 0)
    elif lena < 2:
        tuple_a = (tuple_a[0], 0)

    if lenb < 1:
        tuple_b = (0, 0)
    elif lenb < 2:
        tuple_b = (tuple_b[0], 0)

    add_all = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return add_all
