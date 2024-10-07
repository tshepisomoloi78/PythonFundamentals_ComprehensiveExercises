def element_in_tuple():
    """
    Write a Python program to check whether an element exists within a tuple

    Use `r` and `5` as your inputs in STDIN

    Expected output:
    ```
    Enter r:
    True
    Enter 5:
    False
    ```
    """

    tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
    check1 = input("Enter r:")
    #enter your code here
    check2 = int(input("Enter 5:"))
    #enter your code here


def list_to_tuple():
    """
    Write a Python program to convert a list to a tuple
    """

    #Convert list to tuple
    listx = [5, 10, 7, 4, 15, 3]
    print(listx)
    #use the tuple() function built-in Python, passing as parameter the list


def length_of_tuple():
    """
    Write a Python program to find the length of a tuple.

    Expected output:
    ```
    ('W','e','T','h','i','n','k','C','o','d','e')
    11
    ```
    """

    # create a tuple

    #use the len() function to known the length of tuple


def sum_of_list(numbers):
    """
    Write a Python function to sum all the numbers in a list
    Sample List :
    `(8, 2, 3, 0, 7)`
    Expected Output :
    `20`

    Use `Y` in STDIN to test your code
    """

    total = 0
    #enter your code here

print(sum_of_list((8, 2, 3, 0, 7)))


def multiply_list(numbers):
    """
    Write a Python function to multiply all the numbers in a list.
    Sample List :
    `(8, 2, 3, -1, 7)`
    Expected Output :
    `-336`
    """

    total = 1
    #enter your code here

print(multiply_list((8, 2, 3, -1, 7)))


def unique_list(l):
    """
    Write a Python function that takes a list and returns a new list with unique elements of the first list.
    Sample List :
    `[1,2,3,3,3,3,4,5]`

    Unique List :
    `[1, 2, 3, 4, 5]`

    Use `Y` in STDIN to test your code
    """

    x = []
    #enter your code here

print(unique_list([1,2,3,3,3,3,4,5]))


def palindrome(string):
    """
    Write a Python function that checks whether a passed string is palindrome or not.
    Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

    Use the following words in STDIN to test the program:
    ```
    anna
    number
    madam
    racecar
    noon
    level
    kayak
    mom
    civic
    ```
    """

    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        #enter code here
        return ""
    return True


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    word = input("Please type in a word to test the program:")
    print(palindrome(word))
