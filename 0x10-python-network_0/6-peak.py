#!/usr/bin/python3

def find_peak(list_of_integers):
    """Return a peak of unsorted integers list."""
    if not list_of_integers:
        return None

    list_size = len(list_of_integers)
    mid = int(list_size / 2)
    peak = list_of_integers[mid]

    if (mid == list_size - 1 or peak >= list_of_integers[mid + 1]) and (mid == 0 or peak >= list_of_integers[mid - 1]):
        return peak
    elif mid > 0 and list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

