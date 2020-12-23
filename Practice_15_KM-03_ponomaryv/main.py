from factorial.factorial import fact
from exp_root.root import *
from exp_root.exponentiation import *
from logarithm.logarithm import *


def cheker_log(text):
    val = input(text)
    while type(val) != int:
        try:
            if int(val) < 0 or int(val) == 1 :
                val = "a"
            val = int(val)
            return int(val)
        except:
            val = input("Entered an incorrect value, try again,")
    return int(val)

def cheak_2(text):
    val = input(text)
    while type(val) != int :
        try:
            if int(val) <= 0 :
                val = "a"
            val = int(val)
            return int(val)
        except:
            val = input("Entered an incorrect value, try again,( you must keep a value > 0 ) :")
    return int(val)

def cheker_3(text):
    val = input(text)
    while type(val) != int:
        try:
            val = int(val)
            return int(val)
        except:
            val = input("Entered an incorrect value, try again,(you must enter a number  ")
    return int(val)

def fackt():
    n=cheak_2("Enter value: ")
    print(f'Factorial {n} = {fact(n)}')

def exp_rooot():
    try:
        er = int(input("Chose(1 = root2, 2 = root3, 3 = exp2 ,4 = exp3) :"))
        if er == 1:
            n = cheak_2("Enter value: ")
            print (f'root {n} = {root2(n)}')
        elif er == 2:
            n = cheak_2("Еnter value: ")
            print(f'third root {n} = {root3(n)}')
        elif er == 3:
            n = cheker_3("Еnter value: ")
            print(f"exp2 {n} = {exp2(n)}")
        elif er == 4 :
            n = cheker_3("Enter value: ")
            print(f'exp3 {n} = {exp3(n)}')
    except:
        print("Entered an incorrect value, try again\n")
        exp_rooot()

def logh():
    try:
        log_ = int(input("Chose (1 = log; 2 = ln; 3= lg): "))
        if log_ == 1:
            base = cheker_log("Enter base logarithm: ")
            a=cheak_2("Enter A: ")
            a=int(a)
            print(f"log {base} {a}= {log(a,base)}")
        elif log_ == 2:
            B = cheak_2("Enter B: ")
            print(f"ln {B}= {ln(B)}")
        elif log_ == 3:
            B = cheak_2("Enter B: ")
            print(f"lg {B} = {lg(B)}")
    except:
        print("Entered an incorrect value, try again\n")
        logh()

def main():
    try:
        a = int(input("Chose(logarithm = 1, factorial = 2, exp_root = 3): "))
        if a == 1:
            logh()
        elif a == 2:
            fackt()
        elif a == 3:
            exp_rooot()
    except:
        print("your chose not corect try again\n")
        main()


if __name__ == '__main__':
    main()

