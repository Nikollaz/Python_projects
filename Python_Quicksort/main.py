#!/usr/bin/python
"""
    Basic Quicksort algorithm

    @author: Nicolas.Saavedra
"""
#pylint: disable-msg=C0103
#pylint: disable-msg=E1121

import random

from classes.quicksort_utils import quicksort

if __name__ == "__main__":

    array = [
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100)
    ]

    print quicksort(array)
