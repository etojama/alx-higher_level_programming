#!/usr/bin/python3

# replace_in_list - replace element in a list
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    else idx >= len(my_list):
        return my_list
    mylist[idx] = element
    return my_list
