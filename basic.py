list = ["my","name"," is "," Naim "," rahman "]

for number in list:
    print(number)
name1={"naim":25}
name2={"rahman":25}

name = name1 | name2
print(name)

name4 = {**name1,**name2}
print(name4)
1
# print("hello,world!")
name="naim"
age=25
city="gazipur"
# print("My name is "+name+" iam "+ str(age)+ " year old."+"I live in "+city)
# # intger r string can not + 

print(f"my name is {name} and i am {age} year old , I live in {city}")
used of Format
print("my name is {n} iam {d} year old i live in {c}".format(n="naim",d=25,c="gazipur"))
print("the name of this bird is {n} .It live in bangladesh . it is {d} mitier long ".format(n="doiel",d=22))
a=23
b=5
print(a+b)
print(a*b)
print(a/b)
print(a-b)cd

name = input("enter your name : ")
print("hello {n} ".format(n=name))


n=""
print("hello {n} ".format(n=input("what is you name :")))

print(n)


num1=int(input("enter the number :"))
num2=int(input("enter the seconde number :"))

print(num1+num2)

num1=int(input("Enter you number :"))

if num1==0:
    print("the number is Zero")
elif num1%2 ==0:
    print(f"the number {num1} is even")
else:
    print(f"the number {num1} is odd")               
