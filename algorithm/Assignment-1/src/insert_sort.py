#/usr/local/bin/python3
# -*- coding: utf-8 -*-

def insert_sort(data, column):
    res = data
    for end in range(1, len(res)):
        for i in range(end, 0, -1):
            if res[i - 1][column
        ] > res[i][column]:
                res[i - 1], res[i] = res[i], res[i - 1]

    return res