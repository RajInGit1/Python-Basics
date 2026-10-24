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

#import sys
#print(sys.argv[1])


def prime_number(n):

    i = 2

    while n > i:

        if n % i == 0:
            print(f'{n} Not Prime Number')

            break
        i = i + 1

    else:
        print(f'{n} Prime Number')

prime_number(1)
prime_number(2)
prime_number(11)
prime_number(12)
