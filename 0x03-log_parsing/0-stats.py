#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shuaib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2022, salafi'
__version__ = "0.01t"
"""

import sys


def displayMessage(status_codes, total_file_size):
    """
    This Take in the a dict of status codes and total_file_size (int) 
    and print a formatted message
    """

    print(f"File size: {total_file_size}")
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print(f"{key}: {val}")


def boot():
    total_file_size = 0
    code = 0
    counter = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            line_as_list = line.split() # turn the line into list
            line_as_list = line_as_list[::-1] # reverse the line

            if len(line_as_list) > 2:
                counter += 1

                if counter <= 10:
                    total_file_size += int(line_as_list[0]) # get the file size
                    code = line_as_list[1] # get the status code

                    if code in status_codes.keys():
                        status_codes[code] += 1
                if counter == 10:
                    displayMessage(status_codes, total_file_size)
                    counter = 0
    except KeyboardInterrupt:
        print(" ---  Keyboard Interupt with Ctrl+C\n\t Exiting ....")
    finally:
        displayMessage(status_codes, total_file_size)


if __name__ == "__main__":
    boot()

