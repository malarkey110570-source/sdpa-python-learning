# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:34:15 2026

@author: zy110570
"""
# String 和引号
name1 = "Yang"
name2 = 'Yang'

print(name1)
print(name2)

print(type(name1))
print(type(name2))

# test 1
print("single quotes are ''")
print('single quotes are ''')

# test 2
print('I'm learning Python') 
print("I'm learning Python")     


# String Indexing | 字符串索引
word = "Python" # 输出 P ，y , t

print(word[0])  # P
print(word[1])  # y
print(word[2])  # t


# String Slicing | 字符串切片
word = "Python"

print(word[1:4])


# test 1
word = "Python"

print(word[0:3])
print(word[2:6])


# test 2 
word = "Python"

print(word[0:6:2])

# test 3
word = "Python"

print(word[1:6:2])

# ex 1
string1 = "The name of my dog is Charlie!"
print(string1[0::2])

# ex 2
string2 = "My favourite car brand is mercedes benz."
start = string2.find("mercedes")
brand = string2[start:-1]
result = brand.title()
print(result)

# ex 2.1
start = string2.find("mercedes")
result = string2[start:-1].title()

print(result)

# ex 2.2
print(string2[string2.find("mercedes"):-1].title())


# ex 3
string3 = "The weather is taking a turn for the worse."
print(string3[2::4])

# ex 4
string1 = "The name of my dog is Charlie!"
string2 = "My favourite car brand is mercedes benz."
string3 = "The weather is taking a turn for the worse."
string4 = "There are many benefits to Python"
string5 = " strings are stored as an array of characters "
print(len(string1))
print(len(string2))
print(len(string3))
print(len(string4))
print(len(string5))


string5 = " strings are stored as an array of characters "
new_string = string5.strip()
print(len(new_string))

string1 = "The name of my dog is Charlie!"
string2 = "My favourite car brand is mercedes benz."
string3 = "The weather is taking a turn for the worse."

result = string1 + " " +string2 + " " + string3
print(result)

# ex 5
text = "JhonDipPeta"

result = text.find("Dip")
print(text[result:7])


text = "JhonDipPeta"

length = len(text)
middle = length // 2

start = middle - 1 
end = middle + 2
print(text[start:end])

# ex 6
s1 = "Ault"
s2 = "Kelly"
left = s1[0:2]
right = s1[2:4]

print(left + s2 + right)

s1 = "Ault"
s2 = "Kelly"

middle = len(s1) // 2

left = s1[:middle]
right = s1[middle:]

print(left + s2 + right)


# ex 7

s1 = "America"
s2 = "Japan"

middle1 = s1[len(s1) // 2]
middle2 = s2[len(s2) // 2]

first1 = s1[0]
first2 = s2[0]


last1 = s1[-1]
last2 = s2[-1]

print(first1 + first2 + middle1 + middle2 + last1 + last2)


# Conditions | 条件判断
x = 10

print(x == 10)
print(x != 10)
print(x > 5)
print(x < 5)



age = 20

if age >= 18:
    print("Adult")


age = 15

if age >= 18:
    print("Adult")

print("Done")


name = "John"
age = 20

if name == "John" and age == 23:
    print("Correct")
else:
    print("Wrong")


name = "Rick"
age = 20

if name == "John" or age == 20:
    print("Correct")
else:
    print("Wrong")
    
    
    x = 15

if x > 10:
    print("Above ten")

    if x > 20:
        print("Above twenty")
    else:
        print("Not above twenty")
        
# Nested If   
x = 8

if x > 10:
    print("Above ten")

    if x > 20:
        print("Above twenty")
    else:
        print("Not above twenty")

print("Done")        
        
        
# for        
for x in range(5):
    print(x)        
        
        
        
# while loop
count = 0

while count < 5:
    print(count)
    count += 1
    
# break    
    
    for x in range(10):
    if x == 5:
        break
    print(x)
    
    
# continue

for x in range(6):
    if x == 3:
        continue
    print(x)
    
    
#  loop 的 else

count = 0

while count < 3:
    print(count)
    count += 1
else:
    print("Finished")
    
    
# Nested Loops | 嵌套循环

for i in range(3):
    for j in range(2):
        print(i, j)
        
        
for i in range(1, 4):
    for j in range(1, 3):
        print(i * j)
        
        
rows = 3

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
    
    
    
# 练习
count = 1
total = 0

while count <= 10:
    total = total + count
    count = count + 1
    
print(total)


rows = 5

for i in range(1, rows + 1):
    for j in range(1,4):
        print("*",end=" ")
    print()
    
    

    
    