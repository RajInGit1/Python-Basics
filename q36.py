'''def genD():
    for i in range(97,122):
        return chr(i),i
print(genD())'''
        




'''def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact


def isStrongNum(n):
    temp = n
    s = 0

    while n!=0:
        ld = n%10
        s +=factorial(ld)
        n = n//10

    if temp == s:
        print("strong num")
    else:
        print("not strong num")

isStrongNum(2)'''

def primeNum(n):

    if n < 2:
        return false
        
    
     for i in range(1,n+1):
        if n % i ==0:
            
            return false
            
            
        
    return True

l = 1
h= 10

for i in range(1,h):
    if primeNum(i):
        print(i)
