num = int(input("enter the  num : "))

ld = num%10
fd =num//10

if (ld * 10) + fd == num:
	print("civen num is same")
else:
	print("given num is diff")