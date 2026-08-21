num = 6
sum = 0
i = 1

while i < n:
	if n % i ==0:
		sum = sum + i
	i = i + 1
if sum == num:
	print(f"{num} it is a perfect number")
else:
	print(f"{num} it is not perfect number")