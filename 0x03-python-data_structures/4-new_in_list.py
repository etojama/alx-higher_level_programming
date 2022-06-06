#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return mylist.copy()
    elif idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        return new_list.replace(idx, element)
