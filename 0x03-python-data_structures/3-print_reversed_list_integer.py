#!/usr/bin/python3

# print_reversed_list_integer - print list in reverse
def print_reversed_list_integer(my_list=[]):
    for i in range(my_list):
        print("{:d}".format(my_list.reverse()))
