l = ['no',34,3.4,'nahi','nhi',90,'never']

d={}

for i in l:
    if type(i) == str:
        d[i] = i[0] + i[-1]
print(d)