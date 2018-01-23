"""
    Main class with the functions required to sort the array using the quicksort method
"""

def quicksort(array):
    """
        Entrance function
    """
    quicksort_helper(array, 0, len(array)-1)

    return array

def quicksort_helper(array, min_limit, max_limit):
    """
        Function that orders the values between min_limit and max_limit (inclusive)
        using the first element as the pivot
    """

    pivot_index = min_limit
    pivot_value = array[pivot_index]
    left_mark = min_limit
    right_mark = max_limit

    if pivot_index == min_limit and max_limit - min_limit > 1:
        left_mark += 1

    if pivot_index == max_limit and max_limit - min_limit > 1:
        right_mark -= 1

    while True:

        if right_mark < left_mark:
            break

        if array[left_mark] <= pivot_value:

            left_mark += 1

        else:

            while True:

                if right_mark < left_mark:
                    break

                if array[right_mark] >= pivot_value:

                    right_mark -= 1

                else:

                    array[left_mark] = array[left_mark] + array[right_mark]
                    array[right_mark] = array[left_mark] - array[right_mark]
                    array[left_mark] = array[left_mark] - array[right_mark]

                    left_mark += 1
                    right_mark -= 1
                    break

        if right_mark < left_mark and right_mark - left_mark < 2:

            temp = array[right_mark]
            array[right_mark] = array[pivot_index]
            array[pivot_index] = temp
            break

    if max_limit - min_limit > 1:

        if right_mark - min_limit > 1:

            quicksort_helper(array, min_limit, right_mark - 1)

        if max_limit - right_mark > 1:

            quicksort_helper(array, right_mark + 1, max_limit)
