#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    n = len(boxes)
    boxes_checked = set([0])
    boxes_unchecked = set(boxes[0]).difference(set([0]))
    while len(boxes_unchecked) > 0:
        boxIdx = boxes_unchecked.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in boxes_checked:
            boxes_unchecked = boxes_unchecked.union(boxes[boxIdx])
            boxes_checked.add(boxIdx)
    return n == len(boxes_checked)
