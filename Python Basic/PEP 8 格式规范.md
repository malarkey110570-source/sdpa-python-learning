# Python PEP 8 代码规范

> [!info] 什么是 PEP 8？  
> **PEP 8** 是 Python 官方推荐的代码风格指南（Style Guide）。
> 
> 它主要规定：
> 
> - 代码如何排版
>     
> - 空格怎么使用
>     
> - 变量和函数怎么命名
>     
> - 缩进怎么写
>     
> - 如何让代码更容易阅读
>     
> 
> PEP 8 通常**不会改变程序运行结果**，主要目的是提高代码的可读性和一致性。

---

# 1. 运算符两边留一个空格

## ✅ 推荐

```
x = 10
y = 20

result = x + y
average = (x + y) / 2
```

## ❌ 不推荐

```
x=10
y=20

result=x+y
average=(x+y)/2
```

常见运算符：

```
x = 10

x + y
x - y
x * y
x / y
```

> [!tip] 记忆  
> 大多数运算符的**左右各留一个空格**。

---

# 2. 比较运算符两边留空格

## ✅ 推荐

```
x == 10
x != 10
x > 10
x < 10
x >= 10
x <= 10
```

例如：

```
age = 22

if age >= 18:
    print("Adult")
```

## ❌ 不推荐

```
if age>=18:
    print("Adult")
```

---

# 3. 逗号后面加一个空格

## ✅ 推荐

```
numbers = [1, 2, 3, 4, 5]

print(1, 2, 3)
```

## ❌ 不推荐

```
numbers = [1,2,3,4,5]

print(1,2,3)
```

> [!tip] 记忆  
> **逗号前不空格，逗号后空一格。**

---

# 4. 括号内部不要加多余空格

## ✅ 推荐

```
print("Hello")

numbers = [1, 2, 3]

result = (x + y) * 2
```

## ❌ 不推荐

```
print( "Hello" )

numbers = [ 1, 2, 3 ]

result = ( x + y ) * 2
```

---

# 5. if、for、while 后面加空格

## if

```
if x > 10:
    print(x)
```

## for

```
for i in range(10):
    print(i)
```

## while

```
while x < 100:
    x = x + 1
```

通常不要模仿 Java / C 写成：

```
if (x > 10):
    print(x)
```

Python 通常直接写：

```
if x > 10:
    print(x)
```

---

# 6. 缩进使用 4 个空格

PEP 8 推荐：

**每一级缩进 = 4 个空格**

例如：

```
if x > 10:
    print("x is large")
```

嵌套：

```
if x > 10:
    for i in range(x):
        print(i)
```

逻辑结构：

```
if
    for
        print
```

> [!warning] 注意  
> 不要混合使用 Tab 和空格。
> 
> Python 对缩进非常敏感，缩进不仅仅是为了美观，还会影响程序结构。

---

# 7. 变量使用 snake_case

Python 普通变量推荐使用：

**snake_case（蛇形命名法）**

## ✅ 推荐

```
student_name = "Tom"
student_age = 22
exam_score = 85
average_score = 75.5
```

## ❌ 不推荐

```
studentName = "Tom"
StudentAge = 22
averagescore = 75.5
```

### snake_case 结构

```
student_name
average_score
total_price
exam_result
```

规则：

**全部小写 + 单词之间使用** `**_**` **连接**

---

# 8. 函数使用 snake_case

## ✅ 推荐

```
def calculate_average():
    pass
```

```
def calculate_exam_score():
    pass
```

## ❌ 不推荐

```
def CalculateAverage():
    pass
```

```
def calculateAverage():
    pass
```

---

# 9. 类使用 PascalCase

以后学习 Object-Oriented Programming（OOP）时会遇到 `class`。

类名使用：

**PascalCase**

例如：

```
class Student:
    pass
```

```
class StudentInformation:
    pass
```

```
class BankAccount:
    pass
```

特点：

**每个单词首字母大写，不使用** `**_**`**。**

---

# 10. 常量使用大写字母

如果一个值原则上不应该改变，可以使用全大写：

```
PI = 3.14159

MAX_SPEED = 120

DEFAULT_SIZE = 10
```

多个单词：

```
MAX_FILE_SIZE = 100
```

> [!note]  
> Python 不会真正禁止你修改这些变量。
> 
> 全大写只是一种程序员之间的约定，表示：
> 
> **“这个值原则上不要修改。”**

---

# 11. 函数默认参数不要在 = 两边加空格

这是一个容易混淆的特殊情况。

普通赋值：

```
x = 10
```

需要空格。

但是函数默认参数：

```
def calculate(x=10):
    return x * 2
```

通常不加空格。

## ❌ 不推荐

```
def calculate(x = 10):
    return x * 2
```

---

# 12. import 放在文件顶部

通常：

```
import math
import random

x = math.sqrt(25)

print(x)
```

一般不要：

```
x = 10

import math

y = math.sqrt(x)
```

多个模块通常分开写：

```
import math
import random
```

而不是：

```
import math, random
```

---

# 13. 函数之间留空行

例如：

```
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


result = add(10, 20)
print(result)
```

顶层函数和类之间通常留 **2 个空行**。

---

# 14. 一行代码不要太长

PEP 8 传统建议：

**每行代码不超过 79 个字符。**

如果表达式非常长，可以拆开：

```
total = (
    first_number
    + second_number
    + third_number
    + fourth_number
)
```

初学阶段不用特别纠结这个问题。

---

# 15. 一个完整的 PEP 8 示例

```
student_name = "Tom"
exam_score = 85

if exam_score >= 70:
    result = "Pass"
else:
    result = "Fail"

print(student_name, result)
```

这里同时使用了：

- `student_name` → snake_case
    
- `exam_score = 85` → `=` 两边空格
    
- `exam_score >= 70` → 比较符两边空格
    
- `if` → 条件后使用 `:`
    
- `result` → 4 空格缩进
    
- `print(student_name, result)` → 逗号后空一格
    
- `print(...)` → 括号内部没有多余空格
    

---

# 📌 PEP 8 速查表

|情况|推荐写法|
|---|---|
|赋值|`x = 10`|
|加法|`x + y`|
|减法|`x - y`|
|乘法|`x * y`|
|除法|`x / y`|
|等于比较|`x == y`|
|大于等于|`x >= y`|
|列表|`[1, 2, 3]`|
|函数调用|`print(x)`|
|if|`if x > 10:`|
|for|`for i in range(10):`|
|while|`while x < 10:`|
|缩进|4 个空格|
|变量|`student_name`|
|函数|`calculate_score()`|
|类|`StudentInformation`|
|常量|`MAX_SIZE`|

---

# 🧠 初学阶段重点记忆

> [!important] 目前最重要的 5 条
> 
> **1. 运算符左右留一个空格**
> 
> ```
> x = a + b
> ```
> 
> **2. 逗号后留一个空格**
> 
> ```
> numbers = [1, 2, 3]
> ```
> 
> **3. 括号内部不留多余空格**
> 
> ```
> print(x)
> ```
> 
> **4. 每一级缩进 4 个空格**
> 
> ```
> if x > 10:
>     print(x)
> ```
> 
> **5. 普通变量使用 snake_case**
> 
> ```
> student_name = "Tom"
> ```

---

# 🔗 相关笔记

- [[Python Variables]]
    
- [[Python Data Types]]
    
- [[Python Operators]]
    
- [[Python if Statements]]
    
- [[Python for Loops]]
    
- [[Python while Loops]]
    
- [[Python Functions]]
    

#Python #Programming #PEP8 #PythonBasics