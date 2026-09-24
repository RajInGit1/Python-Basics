username = ['user1', 'admin', 'guest', 'user2']

var = lambda n : any('0' <= i <= '9'  for i in n)

res = list(filter(var,username))
print(res)