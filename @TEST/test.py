a = [ [i+j for j in range(5)] for i in range(3) ]
for i in a:
    print(i)

b=list(zip(*a[::-1]))
print(b)

c=list(zip(*b[::-1]))
print(c)