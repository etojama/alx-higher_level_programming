#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_c = my_list.copy()
    for i in range(0, len(my_list)):
        check = my_list[i]
        if check % 2 == 0:
            new_c[i] = 1
        else:
            new_c[i] = 0
    return new_c
