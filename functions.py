def multiply(x, y):
    """
    Multiply two `ints` or `floats` and return the product
    :param x: first `int` or `float` to be multiplied
    :param y: second `int` or `float` to be multiplied
    :return: `float` or `int` product of `x` and `y`
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Check a string to see if it is identical forward and backwards.
    NOT case sensitive.
    :param string: the string to be checked
    :return: True if the string is a palindrome, False if not.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
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


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(sentence))

answer = multiply(18, 3)
print(answer)
