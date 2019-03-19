def sum_array(array):
    """ Return the sum of all numerical values in an list or array-like object.

    :param array: list or array-like object with numerical values.
    :return: sum of all numerical values in a list or array-like object.

    Examples:
        >>>> sum_array([5, 3, 2])
        10
    """
    return sum(array)


def fibonacci(n, cache={}):
    """
    Function generates the nth number in the fibonacci sequence, using recursion and
    memoization to handle numbers that occur more than once.

    :param cache: the results cache
    :param n: the whole number
    :return: the nth number in the fibonacci sequence

    Examples:
        >>>> fibonacci(25)
        75025
    """
    try:
        if n < 0:
            raise ValueError('Input error: n must be a whole number, i.e., from zero going up')
        return 0 if n == 0 else (1 if n < 3 else cache[n])
    except ValueError as ve:
        print(str(ve))
    except KeyError:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]


def factorial(n):
    """ Function calculates the factorial of any positive numerical (integer) value.

    :param n: any positive numerical (integer) value.
    :return: the factorial of the given numerical (integer) value.

    Examples:
        >>>> factorial(10)
        3628800
    """
    try:
        if n < 0:
            raise AssertionError
        return 1 if n <= 1 else n * factorial(n - 1)
    except AssertionError:
        print('Error: n must be a positive integer')


def reverse(word):
    """ Function accepts a string object and reverses it in place.

    :param word: the string object to be reversed.
    :return: the reversed string object.

    Examples:
        >>>> reverse('Hello!')
        !olleH
    """
    try:
        if len(word) < 0:
            raise ValueError('Input error: word cannot be empty')
        return word[::-1]
    except ValueError as ve:
        print(str(ve))
