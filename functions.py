def multiply(x: float, y: float) -> float:
    """
    Multiply two `ints` or `floats` and return the product
    :param x: first `int` or `float` to be multiplied
    :param y: second `int` or `float` to be multiplied
    :return: `float` or `int` product of `x` and `y`
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check a string to see if it is identical forward and backwards.
    NOT case sensitive.
    :param string: the string to be checked
    :return: True if the string is a palindrome, False if not.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check a string to see if it is identical forward and backwards,
    excluding whitespace and punctuation.  NOT case sensitive.
    :param sentence: the string to be checked
    :return: True if the string is a palindrome, False if not
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number, for positive `n` """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence(242)