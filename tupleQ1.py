tuple = eval(input("enter the tuple : "))
out = []
i = 0

while i<len(tuple):
	if i%2 != 0 and tuple[i]%2 == 0:
		out.append(tuple[i])
	i = i+1
print(out)