"""
separator.join(iterable)
    - join() takes an iterable as input.
    - append the 'separator' after each element of the iterable (except the last one)
    - and return the string
    - TypeError: if the provided iterable contains any non-string value

iterable:
    - any python object that capable of returning it's members one at a time
        - that allows it to be iterated over in a for-loop
    - native iterable: List, Tuple, String, Dictionary and Set
    - among from other objects: where you define __iter__() or __getitem()__  method
"""


def main():
    # joining tuple
    names = ("Razib", "Sazib", "Nazmul", "Neyamul")
    print(", ".join(names))
    # Razib,Sazib,Nazmul,Neyamul

    # joining list
    fruits = ["apple", "orange", "mango", "banana"]
    print("/".join(fruits))
    # apple/orange/mango/banana

    # joining string
    s1 = 'abc'
    s2 = '123456'
    print(s1.join(s2))  # 1abc2abc3abc4abc5abc6 note no 'abc' after the last element of iterator s2 - 6
    print(s2.join(s1))  # a123456b123456c note no '123456' after the last element of the iterator s1 - c

    # joining list of numbers - TypeError, and solve it using map()
    nums = [1, 2, 3, 4, 5]
    # print(','.join(nums))  # TypeError - non-string value
    print(','.join(map(str, nums)))  # right way to print 1,2,3,4,5 in console

    # joining dictionaries - joins key
    d = {'name': 'Razib', 'city': 'Dhaka', 'country': 'Bangladesh'}
    print(','.join(d))  # name,city,country


if __name__ == "__main__":
    main()
