#!/usr/bin/python3

# element_at - checking element at index
def element_at(my_list, idx):
    """Return index at position idx"""
    if idx < 0:
        return
    elif idx > len(my_list):
        return
    else:
        return my_list[idx]
