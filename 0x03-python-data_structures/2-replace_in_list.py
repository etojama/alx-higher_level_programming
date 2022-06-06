#!/usr/bin/python3

# replace_in_list - replace element in list
def replace_in_list(my_list, idx, element):
    """replace element in list"""

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        return mylist.insert(idx, element)
