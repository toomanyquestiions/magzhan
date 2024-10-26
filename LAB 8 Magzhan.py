#1.1
user_input = input("Введите фразу: ")
user_input = user_input.lower()
char_list = list(user_input)
print("Созданный список:", char_list)

#1.2
input=input("Enter: ")

vowels="aeiouAEIOU"

vow=[]
nonvow=[]
symbols=[]
for i in input:
    if i in vowels:
        vow.append(i)
    elif i.isalpha():
        nonvow.append(i)
    else:
        symbols.append(i)

print(vow)
print(nonvow)
print(symbols)

#2.1
students={}

students["name"]=input("Enter Student Name: ")
students["assignments"]=list(map(int, input("Scores: ").split()))
students["lab"]=list(map(int, input("Scores: ").split()))
students["test"]=list(map(int, input("Scores: ").split()))

print(students)
#2.2
checkedlist={}

checkedlist["name"]=input("Enter Student Name: ")
checkedlist["sub_activities"]=len(students["assignments"])+len(students["lab"])+len(students["test"])
print(checkedlist)



