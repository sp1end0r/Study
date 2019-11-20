#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def insert_sort(data, row):
    res = data
    for end in range(1, len(res)):
        for i in range(end, 0, -1):
            if res[i - 1][row] > res[i][row]:
                res[i - 1], res[i] = res[i], res[i - 1]

    return res