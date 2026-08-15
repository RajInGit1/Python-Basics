
a = int(input("enter number 1 :"))
b = int(input("enter number 2 :"))
c = int(input("enter number 3 :"))

if  a>b and a>c :
    print(f"{a} is greates")
elif b>a  and b>c:
    print(f"{b} is greates")
elif c>b and c>a :
    print(f"{c} is greatest")
else :
    print("both are eql")