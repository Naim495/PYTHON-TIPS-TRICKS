# list = ["my","name"," is "," Naim "," rahman "]

# for number in list:
#     print(number)
name1={"naim":25}
name2={"rahman":25}

name = name1 | name2
print(name)

name4 = {**name1,**name2}

print(name4)


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


a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))

if a>b:
      if a>c:
            print(f"{a} is the bigest number")
      else :
            print(f"{c} is the bigist number ")
elif b>a:
      if b>c:
            print(f"{b} is the bigist number")
      else :
            print(f"{c} is the biggist number")  
age=int(input("Enter your age :"))

if age>18 or age == 18:
    print("you are adult")
else :
    print("your are minor") 

for i in range(1,100):
      
      if i %2==0:
            print(i)
sum=0
for i in range(1,101):
    sum = sum + i

print(sum)    


