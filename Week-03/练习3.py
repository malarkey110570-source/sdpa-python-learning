# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:59:14 2026

@author: 18346
"""

# EX 1.1
s = [0] * 3
print(s)

s[0] += 1
print(s)


s = [''] * 3
print(s)

s[0] += 'a'
print(s)



s = [[]] * 3
print(s)

s[0] += [1]
print(s)


# EX 1.2

device1 = ['Macbook Pro', 2479]
device2 = ['Dell XPS', 1899]
device3 = ['Asus Notebook', 1599]



device1.append('White')
device2.append('Silver')
device3.append('Red')

device3[0] ='Asus Zenbook'

print(device1)
print(device2)
print(device3)

device = [device1,device2,device3]

print(device)


# EX 1.3

list1 = ["Hello", "Bye"]
list2 = ["World", "Python"]


mergeList = []


for word1 in list1:
    for word2 in list2:
        mergeList.append(word1 + " "  + word2)
print(mergeList)
        

# EX 1.4
numbers = [12, 24, 22, 66, 99, 45, 99, 57, 89, 99, 20, 99]
numbers_copy = numbers[:]

for number in numbers_copy:
    if number == 99:
        numbers.remove(number)

print(numbers)


# EX 2.1
sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

print(min(sampleDict, key=sampleDict.get))

# EX 2.2
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]

sample_dict = {
    'Jhon': 47,
    'Emma': 69,
    'Kelly': 76,
    'Jason': 97
}
roll_number_copy = roll_number[:]

for number in roll_number:
        if number not in sample_dict.values():           
            roll_number_copy.remove(number)
print(roll_number_copy)



# EX 2.3
d1 =  { "name": "John", "age": 21, "budget": 23000 }
d2 =   { "name": "Steve",  "age": 32, "budget": 40000 }
d3 =   { "name": "Martin",  "age": 16, "budget": 2700 }
# Expected output: 65700

d = [d1,d2,d3]

sumbudget = 0

for person in d:
    sumbudget += person["budget"]
    
print(sumbudget)



# EX 3.1

list1 = [1,2,3,4,5,5,5,6,7,8,9]
list2 = [9,10,11,11,5,7,12,13,14]


set1 = set(list1)
set2 = set(list2)

intersection = set1 & set2
result = list (intersection)

print(result)

# EX 3.2

list1 = [1,2,3,4,5,5,5,6,7,8,9]
list2 = [9,10,11,11,5,7,12,13,14]

set1 = set(list1)
set2 = set(list2)

result = set1 - set2

print(result)


# EX 3.3

str1 = 'hello'
str2 = 'abcd'
str3 = 'software'

set1 = set(str1)
set2 = set(str2)
set3 = set(str3)

strings = [str1,str2,str3]
sets = [set1,set2,set3]

for i in range(len(strings)):
    if len(strings[i]) == len(sets[i]):
        print("Ture")
        
    else:
        print("False")

# EX 3.4
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]




for name, actor,species in main_characters:
    print(name,"is a",species.lower(),"voiced by",actor)
    
    
    
# EX 3.5   

studentData = ("John Smith", 11743, ("Computer Science", "Mathematics"))
    
name,student_id,(major,minor) = studentData

print(name)
print(student_id)
print(major)
print(minor)


# EX 3.6
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3]

zipped = zip(list1, list2)
print(list(zipped))

# Bonus Chanllenge 1 Flipping Dictionaries


fav_animals = {
    'Kevin': 'horse',
    'Fanqi': 'Alpaca',
    'Jack': 'dog',
    'Ayush': 'dog',
    'Zahraa': 'Alpaca',
    'Ioana': 'cat',
    'Edgardo': 'cat'
}

flipped = {}

for person, animal in fav_animals.items():
    if animal not in flipped:
        flipped[animal] = []

    flipped[animal].append(person)

print(flipped)


# Bonus chanllenge 2

sentence = input("Please input a sentence: ")
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)


# Bonus chanllenge 3

x = (1, 2, 3, 4)
y = (3, 5, 2, 1)
z = (2, 2, 3, 1)

result = []

zipped = zip(x,y,z)
for group in zipped:
    result.append(sum(group))
    
k = tuple(result)
print(k)
    


