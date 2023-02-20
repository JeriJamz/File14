z = [1,2,3]
x = [1,2,3,4,5]
y = map(lambda i: i**2,x)
z.append(4)
print(list(y))
print(z)
