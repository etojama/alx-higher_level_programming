#!/usr/bin/python3

# replace_in_list - replace element in list
def replace_in_list(my_list, idx, element):
    """replace element in list"""

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
