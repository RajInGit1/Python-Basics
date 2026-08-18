# # n=int(input("enter num"))

# # # i = 10
# # # while i>1:
# # #     print(i,end=" ")
# # #     i=i-1

# # i = 1

# # while i <=10:
# #     print(f"{n} * {i} = {n*i}")
# #     i = i+1

# n = 5
# s = 1                           # if you have sum just sum = 0 / if you have product just prod = 1
# i = 1
# while i<=n:
#     s = s * i
#     i = i + 1
# print(s)



s = "python"
i = 0

while i < len(s):
    if i%2==0:
     print(s[i])                          # here i is for indexing
    i = i+1