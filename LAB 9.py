a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a:
    if i >=5:
        b.append(i)

print(b)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=[]

for i in b:
    for y in a:
        if i==y:
            c.append(i)

print(c)


