'''
def  PrimeNo() :
    num = int(input("enter the number : "))

    if num % 2 == 0 and num >0:
        print (True)

    else:
        print (False)

PrimeNo()
PrimeNo()
'''
'''
import sys

def PrimeNo(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

num = int(sys.argv[1])
print(PrimeNo(num))'''

import sys
print(sys.argv[1])
