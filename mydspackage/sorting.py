def bubble_sort(items):
    """ Return array of items, sorted in ascending order.

    :param items: the unsorted array
    :return: the array of items sorted in ascending order.

    Example:
        >>>> bubble_sort([3, 2, 1])
        [1, 2, 3]
    """
    if len(items) < 2:
        return items
    for num in range(len(items)-1, 0, -1):
        for i in range(num):
            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items


def merge(items, start, mid, end):
    """
    Function divides a list or array-like object into two and sorts the values (in place)
    in ascending order before merging them together.

    :param items: the list or array-like object containing unsorted values
    :param start: the start point to denote the start position of an item in the list or array-like object.
    :param mid: the mid point to denote the middle position of an item in the list or array-like object.
    :param end: the end point to denote the last position of an item in the list or array-like object.
    :return: None
    """
    left = items[start:mid]
    right = items[mid:end]
    s_copy = start
    l_index = 0
    r_index = 0
    while (start + l_index < mid) and (mid + r_index < end):
        if left[l_index] <= right[r_index]:
            items[s_copy] = left[l_index]
            l_index += 1
        else:
            items[s_copy] = right[r_index]
            r_index += 1
        s_copy += 1
    if start + l_index < mid:
        while s_copy < end:
            items[s_copy] = left[l_index]
            l_index += 1
            s_copy += 1
    else:
        while s_copy < end:
            items[s_copy] = right[r_index]
            r_index += 1
            s_copy += 1


def linear_merge(items, start, end):
    """
    Function divides a list or array-like object into smaller chunks recursively and then
    calls the sorting algorithm to sort the list or array-like object in ascending order.

    :param items: the unsorted list or array-like object containing values.
    :param start: the start index of an item in the list or array-like object.
    :param end: the end index of an item in the list or array-like object.
    :return: the list or array-like object of items sorted in ascending order.
    """
    if (end - start) > 1:
        mid = (start + end) // 2
        linear_merge(items, start, mid)
        linear_merge(items, mid, end)
        return merge(items, start, mid, end)


def merge_sort(items):
    """ Function returns list or array-like object of items, sorted in ascending order.

    :param items: the unsorted list or array-like object containing values.
    :return: the list or array-like object of items sorted in ascending order.

    Example:
        >>>> merge_sort([3, 2, 1])
        [1, 2, 3]
    """
    if len(items) < 2:
        return items
    linear_merge(items, 0, len(items))
    return items


def quick_sort(items):
    """ Function returns list or array-like object of items, sorted in ascending order.

    :param items: the unsorted list or array-like object containing values.
    :return: the list or array-like object of items sorted in ascending order.

    Example:
        >>>> quick_sort([3, 2, 1])
        [1, 2, 3]
    """
    low = []
    high = []
    same = []
    if len(items) < 2:
        return items
    pivot = items[0]
    for i in range(len(items)):
        if items[i] < pivot:
            low.append(items[i])
        elif items[i] > pivot:
            high.append(items[i])
        else:
            same.append(items[i])
    return quick_sort(low) + same + quick_sort(high)
