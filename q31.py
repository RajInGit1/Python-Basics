# numbers = [2,3,4,5,6,7,8,9,10]

# prime = lambda n : n > 1 and all(n % i != 0 for i in range(2,n))

# res = tuple(filter(prime, numbers))

# print(res)

# to extract numbers divisible by 3 from a list of numbers

# numbers = [1,2,3,4,5,6,7,8,9,10]

# var = lambda n : n % 3 == 0

# res = tuple(filter(var,numbers))

# print(res)


# to find employees with salary  above 50000 :

# employees = [
#     {"name": "John", "salary": 60000},
#     {"name": "Alice", "salary": 45000},
#     {"name": "Bob", "salary": 70000},
#     {"name": "Eve", "salary": 55000}, ]

# var = lambda n : n ["salary"] > 50000

# res = list(filter(var,employees))

# print(res)