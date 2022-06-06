#!/usr/bin/python3

# print_reversed_list_integer - print list in reverse
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
