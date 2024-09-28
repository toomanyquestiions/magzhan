print("4","8","15","16","23","42")

print("4","8","15","16","23","42",sep="\n")

x=int(input("Number :"))
print(x)
x+=1
print(x)
x+=1
print(x)


x=int(input("Number one :"))
y=int(input("Number two :"))
z=int(input("Number three :"))

sum=x+y+z

print("sum: ",sum)

x=int(input("Length :"))

p=(x**2)*6
s=x**3

print("Volume = ",s)
print("Area = ",p)


x=int(input("Child :"))
y=int(input("Num :"))

z=y//x

print(z)
e=y%x

print(e)


x=int(input("Number :"))

y=x//1000

print("The digit in the thousands position is ", y)

z=(x%1000)//100

print("The number in the hundreds position is  ", z)

e=((x%1000)%100)//10

print("The digit in the tens position is  ", e)

d=(((x%1000)%100)%10)

print("The digit in the position of units  ", d)


x=int(input("Number :"))

y=(x+1)//2

print(y)

