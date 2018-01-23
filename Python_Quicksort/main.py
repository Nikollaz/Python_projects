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

    min_number_limit = -1000
    max_number_limit = 1000

    array = [
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit),
        random.randint(min_number_limit, max_number_limit)
    ]

    print quicksort(array)
