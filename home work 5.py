

# is a palindrome (the word is the same read backwards,
# like “wow”, “mom”, “malayalam”) .
def palindrome(word):
    """
        palindrome: takes in 'word' and returns True if 'word' is palindrome or
        False if 'word' is not a palindrome.
    """
    return False


def palindrome(word):
    return word == word[::-1]


word = "wow"
ans = palindrome(word)

if ans:
    print("Yes")
else:
    print("No")

#########################

# 2. Write a recursive function to calculate the sum
# of even numbers from 1 to n. (if n is 9, you should
# sum 2+4+6+8. If n is 12, you should sum 2+4+6+8+10+12)
# You can assume num will always be positive.
def sum_even(num):
    """
        sum_even: takes in 'num' and returns sum of even numbers from 1 to n.
    """
    return num

def sum_even(num):
    if num <= 1:
        return num

    return num + sum_even(num - 1)

num = 9
print(sum_even(num))

#########################
#3. Implement quicksort with recursion to sort a list.
# Here is a list that you can use:
# array = [10, 3, 1, 4, 6, 8]
def quicksort(array):
    """
        quicksort: takes in 'array' and returns sorted array.
    """
    return array


def quick_sort(arr, n):
    if n <= 1:
        return

    quick_sort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last


# A utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Driver program to test insertion sort
arr = [10, 3, 1, 4, 6, 8]
n = len(arr)
quick_sort(arr, n)
printArray(arr, n)
