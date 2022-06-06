#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return mylist[:]
    else idx >= len(my_list):
        return my_list[:]
    else:
        new_list = my_list[:]
        return new_list.replace(idx, element)
