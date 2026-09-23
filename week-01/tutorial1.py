# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:03:16 2026

@author: 18346
"""
# Assign 1 to x 
x = 1  
y = x + 5
z = y

print(x)
print(y)
print(z)
     

# Integer and float types 整数和浮点数
x = 1
print(type(x))

x = 1.0
print(type(x))


# Division and floor division
print(10 / 2)
print(10 // 2)

print(10 / 4)
print(10 // 4)

print(17 / 3)
print(17 // 3)


# Boolean type
x = True
print(type(x))

x = False
print(type(x))


# String input
name = input("Enter your name")
print(name)


# Input returns a string
x = input("Enter a number: ")
print(x)
print(type(x))


# Convert string input to an integer
x = input("Enter a number")
x = int(x)

print(x)
print(type(x))


# Convert the input directly to an integer
x = int(input("Enter a number: "))
print(type(x))


# Convert the input directly to an string
x = 5
print(type(x))
x = str(x)
print(type(x))

# 报错代码，不能将字符串和整数相加
x = 5
print("The number is " + x)


# 加入str(x)
x = 5
print("The number is " + str(x))


age = 22
print("I am " + str(age) + " years old.")


age = "22"
print(age + age)


# 运算符
print(17 / 3)  # 真正的除法结果
print(17 // 3) # 商（向下取整）
print(17 % 3)  # 余数

# 使用余数和向下取整的商怎么算出原来的值
number = 17
divisor = 3
original = (number // divisor) * divisor + (number % divisor)
print(original)


# Exercises 1 :输出平方和幂方
number = int(input("Enter a number: "))

x = number * number  # x代表平方（squared）
y = number * number * number  # y代表幂方(cubic) 

print(x)
print(y)


# Exercises 2 :计算bmi
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / (height * height)

print("your BMI is " + str(bmi))


# Exercises 3 :(x + y) * (x + y) 通过括号改变运算顺序
x = int(input("Please enter an integer: "))
y = int(input("Please enter an integer: "))

result = (x + y) * (x + y)

print("your result is " + str(result))


# Exercises 4 : 12小时运算， 早上8点在9小时后在12小时制里的运算
star_time = 8
hours_later = 9

final_time = (star_time + hours_later) % 12

print(str(final_time) + " pm" )
 

# Input and output exercise

# 把一个人的名字存进变量，然后输出欢迎
name = str(input("Please enter your name: "))
print("Hello "+ name + ", " + "would you like to learn some Python today?" )

# 把一个人的名字存进变量，然后输出欢迎（Chatgpt version）
name = input("Please enter your name: ")  # input输出string，不需要额外str（）
print("Hello " + name + ", would you like to learn some Python today?")



# input first name and last name, convert last name and first name
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Welcome " + last_name + " " + first_name + "!")


# Challenge yourself 

# n + nn + nnn
n = input("Please enter an integer: ")
nn = n * 2
nnn = n * 3 

result = int(n) + int(nn) + int(nnn)

print(result)

# even or odd
number = int(input("Please enter an integer: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
# Write a Python program to calculate the sum of the digits in an integer (of 4 digits).
#写一个程序，计算一个 4 位整数各位数字之和。
number = int(input("Enter a four-digit integer: "))  # 1234

digit1 = number % 10  #  余4
number = number // 10  # 123

digit2 = number % 10  # 余3
number = number // 10  # 12

digit3 = number % 10  #余 2
number = number // 10 # 1

digit4 = number % 10
result = digit1 + digit2 + digit3 + digit4 

print(result)


# 6:52 a.m. 离开家，先以 8:15/mile 跑 1 mile，然后以 7:12/mile 跑 3 miles，再以 8:15/mile 跑 1 mile，问几点回家吃早餐？
easypace_time = 8 * 60 + 15
tempopace_time = (7 * 60 + 12) *3

total_time = easypace_time * 2 + tempopace_time

cost_minute = total_time // 60 
final_second = total_time % 60

start_hour = 6
start_minute = 52

total_minute = start_minute + cost_minute
final_hours = start_hour + (total_minute // 60)
final_minute = total_minute % 60
    
print(str(final_hours) + ":" + str(final_minute) + ":" + str(final_second) + " am")