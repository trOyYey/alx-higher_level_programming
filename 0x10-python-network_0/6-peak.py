#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def get_peak(intList, first, last):
    """recursive function that looks for peak in given paramter"""
    if first == last:
        return intList[first]

    mid = int((last - first) / 2) + first

    if intList[mid - 1] < intList[mid] and intList[mid + 1] < intList[mid]:
        return intList[mid]

    elif intList[mid + 1] > intList[mid] :
        return get_peak(intList, mid + 1, last)
    else:
        return get_peak(intList, first, mid)

def find_peak(list_of_integers):
    """ finds the peak in the list if list is empty return None"""

    if list_of_integers is None or list_of_integers == []:
        return None
    last = len(list_of_integers) - 1
    peak = get_peak(list_of_integers, 0 , last)
    return peak
