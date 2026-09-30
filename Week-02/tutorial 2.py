# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

count = 1
total = 0

while total <= 10:
    total = total + count
    count = count + 1
    
print(total)



row = 5

for i in range(1, row + 1):
    for j in range(1,4):
        print("*",end =" ")
    print()
    
    
n =int(input("please enter an integer"))
count = 0
while n != 0:
    n = n // 10
    count += 1 
print(count)




n = int(input("Please Enter  an integer"))
reversal = ""
while n != 0:
    digit = n % 10
    reversal += str(digit)
    n = n // 10

print(reversal)
    

s1 = "SDPA is fun"
s2 = "Alpaca are cute"

s1 = s1.lower()
s2 = s2.lower()

com = ""

for letter in s1:
    if letter in s2 and letter != " " and letter not in com:
        com += letter
print(com)



n = int(input("Please enter an integer"))

for divisor in range(2,n):
    if n % divisor == 0:
        print("is not prime")
      
        break

    else:
        print("is a prime")


print("  ** ")
print(" *  *")
print(" *   *")

for i in range(1,7):
    for j in range(1,4):
        print('|*   *|')
        print('| * * |' )
        print('|  ** |')
        print('* ====== *')


n = input("Please enter an integer")
reversal = n[::-1]
print(reversal)