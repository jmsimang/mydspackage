from mydspackage import recursion, sorting


def test_sum_array():
    """
    Make sure sum_array works properly
    """
    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert recursion.sum_array([10, 1, 12, 9, 2]) == 34, 'incorrect'
    assert recursion.sum_array([1, 2, 3, 4, 5]) == 15, 'incorrect'


def test_fibonacci():
    """
    Make sure fibonacci works properly
    """
    assert recursion.fibonacci(7) == 13, 'incorrect'
    assert recursion.fibonacci(3) == 2, 'incorrect'
    assert recursion.fibonacci(25) == 75025, 'incorrect'


def test_factorial():
    """
    Make sure factorial works properly
    """
    assert recursion.factorial(10) == 3628800, 'incorrect'
    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(1) == 1, 'incorrect'
    assert recursion.factorial(0) == 1, 'incorrect'


def test_reverse():
    """
    Make sure reverse works properly
    """
    assert recursion.reverse('Hello') == 'olleH', 'incorrect'
    assert recursion.reverse('Privacy') == 'ycavirP', 'incorrect'
    assert recursion.reverse('World') == 'dlroW', 'incorrect'
    assert recursion.reverse('') == '', 'incorrect'


def test_bubble_sort():
    """
        Make sure bubble sort works properly
    """
    assert sorting.bubble_sort([5, 3, 2, 4, 1]) == [1, 2, 3, 4, 5], 'incorrect'
    assert sorting.bubble_sort([3, 3, 2, 1]) == [1, 2, 3, 3], 'incorrect'
    assert sorting.bubble_sort([33, 25, 30, 24, 11]) == [11, 24, 25, 30, 33], 'incorrect'
    assert sorting.bubble_sort([]) == [], 'incorrect'


def test_merge_sort():
    """
        Make sure merge sort works properly
    """
    assert sorting.merge_sort([5, 3, 2, 4, 1]) == [1, 2, 3, 4, 5], 'incorrect'
    assert sorting.merge_sort([3, 3, 2, 1]) == [1, 2, 3, 3], 'incorrect'
    assert sorting.merge_sort([33, 25, 30, 24, 11]) == [11, 24, 25, 30, 33], 'incorrect'
    assert sorting.merge_sort([]) == [], 'incorrect'


def test_quick_sort():
    """
        Make sure quick sort works properly
    """
    assert sorting.quick_sort([5, 3, 2, 4, 1]) == [1, 2, 3, 4, 5], 'incorrect'
    assert sorting.quick_sort([3, 3, 2, 1]) == [1, 2, 3, 3], 'incorrect'
    assert sorting.quick_sort([33, 25, 30, 24, 11]) == [11, 24, 25, 30, 33], 'incorrect'
    assert sorting.quick_sort([]) == [], 'incorrect'
