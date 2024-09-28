
x=int(input("The number: "))

bin=x<<1

if bin == 0 :
    print("WARNING!!")
else :
    print(bin)


x=int(input("Enter a number1: "))
y=int(input("Enter a number2: "))
z=str(input("Choose operator: "))

if z==("+"):
    print(x+y)
elif z==("-"):
    print(x-y)
elif z==("*"):
    print(x*y)
elif z==("/"):
    print(x/y)
else:
    print("Invalid operator")


x=input("Enter a number: ")

if len(x)==4:
    x_int = int(x)
    y = x_int // 1000
    z = (x_int % 1000) // 100
    e = ((x_int % 1000) % 100) // 10
    d = (((x_int % 1000) % 100) % 10)
    if (y+d)==(z+e):
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")



x=int(input("Enter a number: "))

if x>=18:
    print("Access allowed")
else:
    print("Access denided")

x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))

if x+1==y:
    if y+1==z:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
x_2=int(input("Enter a number: "))
y_2=int(input("Enter a number: "))

if x == x_2 or y == y_2:
    print("YES")
else:
    print("NO")


 x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))

if x>y and y<z:
    print(y)
if x>z and z<y:
    print(z)
if z>x and x<y:
    print(



























x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))

if x>y and y<z:
    print(y)
if x>z and z<y:
    print(z)
if z>x and x<y:
    print(x)