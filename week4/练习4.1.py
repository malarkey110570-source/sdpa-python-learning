# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:16:05 2026

@author: 18346
"""

def  foo ( x ,  y ): 
    global  a 
    a  =  42 
    x , y  =  y , x 
    b  =  33 
    b  =  17 
    print ( a , b , x , y )

a ,  b ,  x ,  y  =  1 ,  15 ,  3 , 4  
foo ( 17 ,  4 ) 
print ( a ,  b ,  x ,  y )



def countdown(n):
    if (n == 0):
        print('game over')
    else:
        print(n)
        countdown(n - 1)
        
countdown(10)


# EX.1

def findnth(s,sub,n):
    start = -1
    
    
    for i in range(n):
      start =  s.find(sub,start + 1)  
       
      if start == -1:
           break

    return start

s = "abc xyz abc jkjkjk abc lkjkjlkj abc jlj"
print(findnth(s,'abc',3))



# EX 2.1
def recursive_list_sum(data_list):
    total = 0
    
    for element in data_list:
        if type(element) == list:
            total += recursive_list_sum(element)
        else:
            total += element
            
    return total
            
print( recursive_list_sum([1, 2, [3,4],[5,6]]))



# EX 2.2

def  Recurgcd ( a ,  b ):
    if b == 0:
        return a
    
    return Recurgcd(b, a%b)  #前一个 b 变成新的 a
                             #余数 a % b 变成新的 b
    
print ( Recurgcd ( 12 , 14 ))



# 2.3

def is_prime(i):
    m = 2

    while m * m <= i:
        if i % m == 0:
            return False
        m += 1

    return True


def num_primes(n):
    # Base case
    if n < 2:
        return 0

    # Recursive case
    if is_prime(n):
        return 1 + num_primes(n - 1)
    else:
        return num_primes(n - 1)


print(num_primes(25))


# challenge 1

def pascal_triangle(n):

    if n == 1:        #base case
        row = [1]
        print(row)
        return row
   
    previous_row = pascal_triangle(n - 1)
        
    new_row = [1]
    
    for i in range(len(previous_row) -1):
        new_row.append(previous_row[i] + previous_row[i + 1])

    new_row.append(1)

    print(new_row)

    return new_row


pascal_triangle(6)



# challenge 2
def ispangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(text.lower())
    
    
    if alphabet - letters == set():
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))



# challenge 3
import string

def caesar(txt, n, coded=False):
    abc = string.ascii_uppercase
    txt = txt.upper()
    result = ""

    for char in txt:
        if char in abc:
            pos = abc.find(char)

            if coded:
                new_pos = (pos + n) % 26
            else:
                new_pos = (pos - n) % 26

            result += abc[new_pos]

        else:
            result += char

    return result


n = 3

x = caesar("Hello, here I am!", n)
print(x)

print(caesar(x, n, True))

