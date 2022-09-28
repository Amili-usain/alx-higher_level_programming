#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        nume = 0
        deno = 0
        for tup in my_list:
            nume += (tup[0] * tup[1])
            deno += tup[1]
        return (nume / deno)
    return 0
