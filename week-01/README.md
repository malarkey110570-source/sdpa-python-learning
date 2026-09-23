当然，下面就是可以直接复制进 `week-01/README.md` 的版本：

````markdown
# Week 01 | 第 01 周

> EMATM0048 — Software Development: Programming and Algorithms  
> University of Bristol  
> Python Learning Journey

This week focused on the fundamentals of Python programming, including variables, basic data types, user input, type conversion, arithmetic operators, and simple conditional logic.

本周主要学习 Python 编程基础，包括变量、基本数据类型、用户输入、类型转换、算术运算符，以及简单的条件判断，并通过 Tutorial 1 的练习理解这些概念在程序中的实际使用。

---

## Topics Covered | 涵盖主题

- Variables and assignment | 变量与赋值
- Basic data types | 基本数据类型
  - `int`
  - `float`
  - `str`
  - `bool`
- User input with `input()` | 使用 `input()` 获取用户输入
- Output with `print()` | 使用 `print()` 输出结果
- Type conversion | 类型转换
  - `int()`
  - `float()`
  - `str()`
- String concatenation | 字符串拼接
- Arithmetic operators | 算术运算符
- Comparison operators | 比较运算符
- Basic `if / else` statements | 基础条件判断
- Operator precedence | 运算优先级

---

## Key Concepts | 关键概念

### 1. Variables and Data Types | 变量与数据类型

Python variables do not require an explicit type declaration.

Python 中变量不需要提前声明数据类型，变量的类型由赋给它的值决定。

```python
x = 1
y = 1.0
name = "Yang"
is_learning = True
````

The four basic types encountered this week:

| Type    | Example | Description                 |
| ------- | ------- | --------------------------- |
| `int`   | `10`    | Integer / 整数                |
| `float` | `10.0`  | Floating-point number / 浮点数 |
| `str`   | `"10"`  | String / 字符串                |
| `bool`  | `True`  | Boolean / 布尔值               |

Example:

```python
x = 1      # int
x = 1.0    # float
```

---

### 2. Input and Type Conversion | 输入与类型转换

`input()` always returns a string.

`input()` 获取的用户输入默认都是 `str`，即使用户输入的是数字。

```python
number = input("Enter a number: ")
print(type(number))
```

To perform numerical calculations, the input needs to be converted:

```python
number = int(input("Enter an integer: "))
height = float(input("Enter your height: "))
```

Numbers can also be converted into strings:

```python
age = 22
print("I am " + str(age) + " years old.")
```

Important difference:

```python
"10" + "5"   # "105"
10 + 5       # 15
```

The first operation is string concatenation, while the second is numerical addition.

---

### 3. Arithmetic Operators | 算术运算符

| Operator | Meaning                 | Example       |
| -------- | ----------------------- | ------------- |
| `+`      | Addition / 加法           | `5 + 2`       |
| `-`      | Subtraction / 减法        | `5 - 2`       |
| `*`      | Multiplication / 乘法     | `5 * 2`       |
| `/`      | Division / 普通除法         | `5 / 2 → 2.5` |
| `//`     | Floor division / 向下取整除法 | `5 // 2 → 2`  |
| `%`      | Modulo / 取余             | `5 % 2 → 1`   |
| `**`     | Exponentiation / 幂运算    | `5 ** 2`      |

Example:

```python
number = 17
divisor = 3

original = (number // divisor) * divisor + (number % divisor)

print(original)
```

This represents:

```text
17 = 5 × 3 + 2
```

---

### 4. `/`, `//` and `%`

```python
print(17 / 3)   # 5.666666...
print(17 // 3)  # 5
print(17 % 3)   # 2
```

* `/` returns the result of normal division.
* `//` returns the floor-divided result.
* `%` returns the remainder.

`%` and `//` can also be combined to break numbers into individual digits.

```python
number = 1234

digit1 = number % 10
number = number // 10
```

After this:

```text
digit1 = 4
number = 123
```

---

### 5. Operator Precedence | 运算优先级

Python follows an order of operations.

Basic order encountered this week:

```text
()
↓
* / // %
↓
+ -
```

For operators at the same precedence level, evaluation is generally performed from left to right.

Example:

```python
2 + 3 * 4
```

Result:

```text
14
```

But:

```python
(2 + 3) * 4
```

Result:

```text
20
```

This is an area I need to continue practising.

---

### 6. Basic Conditional Logic | 基础条件判断

```python
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Important distinction:

```python
x = 5       # Assignment / 赋值
x == 5      # Comparison / 判断是否相等
```

Python also uses indentation to define which statements belong to a conditional block.

---

## Exercises | 练习

### Square and Cube | 平方与立方

```python
number = int(input("Enter a number: "))

square = number * number
cube = number * number * number

print(square)
print(cube)
```

---

### BMI Calculator | BMI 计算

```python
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / (height * height)

print("Your BMI is " + str(bmi))
```

This exercise helped me understand how parentheses affect the order of calculation.

```python
weight / height * height
```

and

```python
weight / (height * height)
```

have completely different meanings.

---

### `(x + y) × (x + y)`

```python
x = int(input("Please enter an integer: "))
y = int(input("Please enter an integer: "))

result = (x + y) * (x + y)

print("Your result is " + str(result))
```

---

### 12-Hour Clock | 12 小时制

```python
start_time = 8
hours_later = 9

final_time = (start_time + hours_later) % 12

print(str(final_time) + " pm")
```

This demonstrated a practical use of the modulo `%` operator.

---

### User Input and Strings | 用户输入与字符串

```python
name = input("Please enter your name: ")

print("Hello " + name + ", would you like to learn some Python today?")
```

Since `input()` already returns a string:

```python
str(input(...))
```

is unnecessary in this case.

---

### First Name and Last Name

```python
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Welcome " + last_name + " " + first_name + "!")
```

---

## Challenges | 挑战题

### `n + nn + nnn`

```python
n = input("Please enter an integer: ")

nn = n * 2
nnn = n * 3

result = int(n) + int(nn) + int(nnn)

print(result)
```

Example:

```text
n = "5"
nn = "55"
nnn = "555"

5 + 55 + 555 = 615
```

---

### Even or Odd | 判断奇偶数

```python
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Key idea:

```text
number % 2 == 0
```

means the number is divisible by 2.

---

### Sum of Four Digits | 四位数各位数字之和

```python
number = int(input("Enter a four-digit integer: "))

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number % 10
number = number // 10

digit4 = number % 10

result = digit1 + digit2 + digit3 + digit4

print(result)
```

Key pattern:

```text
% 10  → get the last digit
// 10 → remove the last digit
```

Example:

```text
1234 % 10  → 4
1234 // 10 → 123
```

---

### Running Time Challenge | 跑步时间计算

Problem:

```text
Start: 6:52 a.m.

1 mile @ 8:15 / mile
3 miles @ 7:12 / mile
1 mile @ 8:15 / mile
```

Code:

```python
easy_pace_time = 8 * 60 + 15
tempo_pace_time = (7 * 60 + 12) * 3

total_time = easy_pace_time * 2 + tempo_pace_time

cost_minute = total_time // 60
final_second = total_time % 60

start_hour = 6
start_minute = 52

total_minute = start_minute + cost_minute

final_hours = start_hour + total_minute // 60
final_minute = total_minute % 60

print(
    str(final_hours)
    + ":"
    + str(final_minute)
    + ":"
    + str(final_second)
    + " am"
)
```

Result:

```text
7:30:06 am
```

Main idea:

```text
Convert all time values into seconds
↓
Perform the calculation
↓
// 60 → complete minutes
% 60  → remaining seconds
```

---

## Mistakes & Debugging | 错误与调试

### 1. Chinese Full-Width Brackets | 中文全角括号

Error:

```text
invalid character '（' (U+FF08)
```

Wrong:

```python
int（input（"Enter a number"））
```

Correct:

```python
int(input("Enter a number"))
```

Python code should use English half-width punctuation.

---

### 2. `=` vs `==`

Wrong:

```python
if number % 2 = 0:
```

Correct:

```python
if number % 2 == 0:
```

```text
=   → assignment / 赋值
==  → comparison / 相等判断
```

---

### 3. Missing `:`

Wrong:

```python
else
```

Correct:

```python
else:
```

---

### 4. Indentation | 缩进

Python uses indentation as part of its syntax.

```python
if number % 2 == 0:
    print("Even")
```

Use four spaces for each indentation level.

---

### 5. Mixing Strings and Integers

This does not work:

```python
x = 5
print("The number is " + x)
```

Correct:

```python
print("The number is " + str(x))
```

---

### 6. Unnecessary Type Conversion

Since `input()` already returns `str`:

```python
name = str(input("Please enter your name: "))
```

works, but `str()` is unnecessary.

Better:

```python
name = input("Please enter your name: ")
```

---

### 7. Code Style | 代码格式

Use spaces around binary operators:

```python
x = y + 5
bmi = weight / (height * height)
```

Avoid:

```python
x=y+5
```

Comments:

```python
# Calculate BMI
```

Variable names should normally use `snake_case`:

```python
start_hour
final_minute
easy_pace_time
```

---

## What I Learned | 我学到了什么

After Week 01, I can:

* Understand and distinguish `int`, `float`, `str`, and `bool`
* Create variables and understand assignment using `=`
* Use `input()` and understand that it returns a string
* Convert values using `int()`, `float()`, and `str()`
* Use strings for concatenation and repetition
* Use `/`, `//`, and `%`
* Explain quotient and remainder
* Use `%` for divisibility and cyclic calculations
* Write simple `if / else` conditions
* Break a four-digit integer into individual digits
* Convert between seconds and minutes using `//` and `%`
* Break a programming problem into smaller steps
* Identify common Python syntax and type errors

本周最大的收获：

> 先把现实问题拆成几个小步骤，再把每一步翻译成 Python。

---

## Things to Review | 待回顾事项

* [ ] Practise operator precedence / 继续练习运算优先级
* [ ] Remember that operators at the same precedence level are generally evaluated left to right
* [ ] Strengthen the difference between `/`, `//`, and `%`
* [ ] Practise `if / else` syntax and indentation
* [ ] Remember `=` vs `==`
* [ ] Continue practising type conversion
* [ ] Use more descriptive variable names
* [ ] Follow basic PEP 8 formatting
* [ ] Try solving simple problems before asking for hints

### Priority Review | 优先复习

> **Operator precedence / 运算优先级** is currently the main topic I need to strengthen.

Remember:

```text
()
↓
* / // %
↓
+ -
```

Example:

```python
20 / 5 * 2
```

Python evaluates it from left to right:

```text
20 / 5 = 4.0
4.0 * 2 = 8.0
```

---

## Week 01 Summary | 第一周总结

Week 01 introduced the basic building blocks of Python.

第一周从最基础的数据类型和变量开始，逐渐进入输入输出、类型转换、运算符，最后通过 Challenge 将这些基础知识组合起来解决实际问题。

The most useful concepts for me this week were:

```text
input() → str
int() / float() / str()
/  //  %
% 2 → divisibility
% 10 → last digit
// 10 → remove last digit
// 60 and % 60 → time conversion
```

Next step: continue building confidence with expressions, conditions, and problem-solving before moving into more complex Python structures.

```

直接整段复制到你的 `week-01/README.md` 即可。
```
