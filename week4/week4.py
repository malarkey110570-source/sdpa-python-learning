# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:31:49 2026

@author: zy110570
"""
# 1
def cel_far(celsius):  # def定义函数，cel_far函数名，celsius 是parameter
    """
    Input: celsius
    Returns Fahrenheit
    """

    fahrenheit = (celsius * 1.8) + 32 # 函数主体

    return fahrenheit # 返回结果

# parameter 是形式参数，只代表一个位置一个变量名




# 2
def add(a, b):
    return a + b
 #定义一个叫 add 的东西。”
 #但它不会立刻计算。
 #真正执行是在：
add(3, 5)

result = add(3, 5) 

#3 + 5
#↓
#8
#↓
#return 8
#↓            没有指定 return，或者只有一个空的 return 时，function 会返回 None；function 也可以 return 多个值
#result = 8   把 function 内部产生的结果送回调用它的位置。



# 3

# Positional Arguments 关键字参数，第一个argument对应第一个parameter，第二个对应第二个
def printName(firstName, lastName, reverse):
    
 printName("Olga", "Raheem", False)
 
 
 


 
# Default Parameter 默认参数
 def printName(firstName, lastName, reverse=False):
    
 # reverse=False 如果调用function时没有提供reverse，就自动使用False


     printName("Olga", "Raheem")
     # 默认等价reverse = False

     printName("Olga", "Raheem", reverse=True)
     # 覆盖默认值
     
     
# parameters 可以是 tuple、list、dictionary 等复杂类型。



# 可变参数

def make_pizza(size, *toppings):

    make_pizza(16, "pepperoni")


    make_pizza(
    12,
    "mushrooms",
    "green peppers",
    "extra cheese"
)

    for topping in toppings:
       print(topping)



#  Scope

def f(x):
    y = 1
    x = x + y
    return x
# y 是在函数里创建的，属于局部作用域，只存在函数内部
# 同一个变量名字可能出现在不同scope中，但是他们不一定是一个变量


## Function
#→ 把一段代码包装起来

##Module
#→ 把很多 functions 放到独立 .py 文件里   




#recursive function


#def something(n):

#    if 最简单情况:
#        return 答案

#    else:
 #       return something(更小的问题)
 
 
 # EX1
def multi(a, b):

    if b == 1:
        return a

    else:
        return a + multi(a, b - 1)




# EX2
def multi(a, b):
    result = 0

    while b > 0:
        result += a
        b -= 1

    return result
 
    
 #EX3
def isPal(s):
       
    if len(s) <= 1:
        return True

    else:
        if s[0] == s[-1]:
            return isPal(s[1:-1])

        else:
            return False 
        
        
# 你先看到 recursive function 时问自己两个问题：
#哪里停止？
#→ base case

#每一次怎么让问题变小？
#→ recursive step
     
        
# lambda 一个很短、临时使用的小 function。

#  def multiply(x, y):
#    return x * y


lambda x, y: x * y     
# lambda parameters : expression       
        
        
# EX1
r = lambda x, y: x * y
        
r(12, 3)       
        
        
        
# map 
#map(function, iterable)    
numbers = [1, 2, 3, 4, 5] 
    
def square(x):
    return x * x


map(square, numbers)

list(map(...))


# EX 1
def length_of_all_elements(arr):
    return list(map(len, arr))

["alpaca", "SDPA", "data science"]

[6, 4, 12]



# map + lambda

# normal
def square(x):
    return x * x

map(square, numbers)


# 变形
map(lambda x: x * x, numbers)



# map() 也可以接多个 iterables **

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

list(map(pow, first_it, second_it))



# filter()

# EX1

result = []

def starts_with_a(arr):

    ret_arr = []

    for elem in arr:

        if elem[0].lower() == "a":
            ret_arr.append(elem)

    return ret_arr


def starts_with_a(arr):

    return list(
        filter(
            lambda word: word[0].lower() == "a",
            arr
        )
    )

        
        
# Comprehension

squares = []

for i in range(10):
    squares.append(i * i)
    
    
squares = [i * i for i in range(10)]   
    
# new_list = [expression for member in iterable]    
    

# Comprehension 加 if

result = []

for number in numbers:
    if number > 10:
        result.append(number)
        
        
        
[number for number in numbers if number > 10]     
        
        
 # Dictionary Comprehension  

squares = {
    i: i * i
    for i in range(10)
}     
        
#4A Functions
把代码封装起来
↓
input → function → output

4B Recursion
function 甚至可以调用自己
↓
base case + smaller problem

4C Smaller Functions
把一些常见的遍历/筛选写得更抽象、更紧凑
↓
lambda / map / filter / comprehension
    