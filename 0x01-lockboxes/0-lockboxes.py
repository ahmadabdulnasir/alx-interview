#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shuaib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2022, salafi'
__version__ = "0.01t"
"""


def findOpenedBox(opened_boxes):
    """
        This function find opened boxes
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """
       A method that check if all the boxes can be opened given n number of locked boxes
       Each box may contain keys to the other boxes.
       boxes: list of list

       Return: bool (True if all boxes can be opened else False)
    """
    if len(boxes) == 0 or boxes == [[]]:
        return True

    seen_boxes = {}
    while True:
        if len(seen_boxes) == 0:
            seen_boxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = findOpenedBox(seen_boxes)
        if keys:
            for key in keys:
                try:
                    if seen_boxes.get(key) and seen_boxes.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    seen_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in seen_boxes.values()]:
            continue
        elif len(seen_boxes) == len(boxes):
            break
        else:
            return False

    return len(seen_boxes) == len(boxes)


def boot():
    canUnlockAll([[]])


if __name__ == "__main__":
    boot()
