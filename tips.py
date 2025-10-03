# list = ["my","name"," is "," Naim "," rahman "]

# for number in list:
#     print(number)
name1={"naim":25}
name2={"rahman":25}

name = name1 | name2
print(name)

name4 = {**name1,**name2}
print(name4)