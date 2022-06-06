#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return mylist[:]
    elif idx >= len(my_list):
        return my_list[:]
    else:
        new_list = my_list[:]
        return new_list.replace(idx, element)
