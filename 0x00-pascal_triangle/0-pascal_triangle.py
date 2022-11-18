#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shuaib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2022, salafi'
__version__ = "0.01t"
"""


def pascal_triangle(n):
    """This function returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
