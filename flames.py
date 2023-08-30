# # step 1 make dict of full forms of remaining last word
# # step 2 Take input from user and cut common elements
# # step 3 count remaining elements 8
# # step 4 make a list of flames  cut every 8 element until 1 not comes
#

import itertools


def flames(name1, name2):
    full_forms_list = [
        'Friends',
        'Love',
        'Affection',
        "Marriage",
        "Enemy",
        'Siblings']

    for common in name1:
        # print(common)
        if common in name2:
            name1 = name1.replace(common, '')
            name2 = name2.replace(common, "")

    remaining_word = name1 + name2
    length_of_remaining_word = len(remaining_word)

    while len(full_forms_list) > 1:
        index = length_of_remaining_word % len(full_forms_list)
        full_forms_list.pop(index - 1)
    return full_forms_list[0]


name1 = input('TYPE YOUR FIRST NAME  : ')
name2 = input('TYPE YOUR SECOND NAME : ')
relationship = flames(name1, name2)
print(relationship)
