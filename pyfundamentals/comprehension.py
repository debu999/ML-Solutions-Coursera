import sys
from pprint import pprint as pp
from math import factorial as fct

def main():
    words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
    pp(words)
    pp([len(word) for word in words])
    pp(sorted([fct(i) for i in range(20)]))
    pp(sorted({fct(i) for i in range(20)}))
    cnt_to_cap = {'Odisha':"Bhubaneswar","MP":"Bhopal","Gujrat":"Gandhinagar","India":"New Delhi","Pakistan":
                  "Islamabad"}

    cap_to_cnt = {cap:con for con,cap in cnt_to_cap.items()}
    pp(cnt_to_cap)
    pp(cap_to_cnt)
    pass

    from math import sqrt

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2,int(sqrt(x)+1)):
            if x % i == 0:
                return False
        return True

    print([x for x in range(101) if is_prime(x)])
    prime_square_divisors = {x*x:(1,x,x*x) for x in range(101) if is_prime(x)}
    pp(prime_square_divisors)


def interation_test():
    """
    Function:
    iteration_test returns a test of iter and next
    Stop Iteration exception.
    :return:
    """
    a = list("DEBABRATA PATNAIK TEST STRING")
    pp(a)
    itr = iter(a)
    s = ""
    for i in range(len(a)):
        s += next(itr)
    pp(s)
    '''next(itr) after the end of iteration will result in StopIteration error in python
    '''
    try:

        next(itr)
    except StopIteration:
        pp("StopIteration Error encountered if next(iterator) after all elements are parsed")


def iter_check_empty(itr):
    iterator = iter(itr)
    try:
        a = list(itr)
        print(a)
        return next(iterator)
    except StopIteration:
        raise ValueError("Provided Iterator is Empty")


if __name__ == "__main__":
    main()
    interation_test()
    try:
        pp(iter_check_empty([]))
    except:
        pp("Error detected while fetching first data from empty list")
    try:
        pp(iter_check_empty({}))
    except:
        pp("Error detected while fetching first data from empty dictionary")
    try:
        pp(iter_check_empty({1:1,2:2,3:3}))
    except:
        pp("Error detected while fetching first data from dictionary set")
    try:
        pp(iter_check_empty(set("Debabrata")))
    except:
        pp("Error detected while fetching first data from empty set")