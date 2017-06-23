# coding:utf-8
import math


def binary_search(list, item):
    list.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = math.ceil((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == '__main__':
    print(binary_search([1, 3, 5, 6], 6))
