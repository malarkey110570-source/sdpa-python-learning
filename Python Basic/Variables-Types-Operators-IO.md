# Week 01 — Python Basics | 第 01 周：Python 基础

> **EMATM0048 — Software Development: Programming and Algorithms (SDPA)**  
> University of Bristol  
> Week 01 Learning Notes

本周主要学习 Python 的基础概念，并通过 Tutorial 1 将这些概念应用到实际练习中。  
重点不只是记住 Python 语法，而是开始学习如何把问题拆成更小的步骤，再逐步写成程序。

---

## Topics Covered | 本周主题

- Python Programs & Scripts | Python 程序与脚本
- Interactive vs Script Mode | 交互模式与脚本模式
- Variables & Values | 变量与值
- Objects & Data Types | 对象与数据类型
- Type Conversion | 类型转换
- Expressions | 表达式
- Arithmetic Operators | 算术运算符
- Comparison Operators | 比较运算符
- Input & Output | 输入与输出
- Variable Naming | 变量命名
- Comments | 注释
- Basic `if / else` | 基础条件判断
- Problem Solving & Debugging | 问题求解与调试

---

# 1. Course Mindset | 课程核心思路

本课程虽然大量使用 Python，但真正重要的是学习：

- Knowledge of concepts | 概念理解
- Programming skills | 编程技能
- Problem solving | 问题求解

可以把本周的学习思路概括成：

```text
Problem
↓
Break it into smaller steps
↓
Choose suitable variables and operations
↓
Translate the steps into Python
↓
Test and debug
```

也就是说：

> Python 是工具，Problem Solving 才是核心能力。

---

# 2. Python Program Structure | Python 程序基本结构

Python 程序由一系列 statement / command 组成。

例如：

```python
print("Hello World!")
```

多个语句可以组成一个 script：

```python
print("First line")
print("Second line")
print("This looks like a script")
```

---

# 3. Python Modes | Python 运行方式

## Interactive Mode | 交互模式

在 Shell 中一行一行输入代码：

```text
>>> 2 + 3
5
```

特点：

- 一次输入一行
- Python 立即计算
- 适合快速测试表达式

## Script Mode | 脚本模式

把多行代码写入 `.py` 文件，再执行整个脚本：

```python
x = 5
y = 10

print(x + y)
```

本周主要通过 Spyder 使用 Script Mode。

---

# 4. Variables & Values | 变量与值

Python 使用 `=` 进行赋值：

```python
x = 1
y = x + 5
z = y

print(x)
print(y)
print(z)
```

输出：

```text
1
6
6
```

`=` 的含义是：

> 把右边的值绑定到左边的变量名。

例如：

```python
x = 5
```

表示变量名 `x` 现在代表值 `5`。

---

# 5. Objects & Data Types | 对象与数据类型

Python 中的数据都是 object，每个 object 都有自己的 type。

本周主要接触：

| Type | Example | Meaning |
|---|---|---|
| `int` | `10` | Integer / 整数 |
| `float` | `10.0` | Floating point / 浮点数 |
| `str` | `"10"` | String / 字符串 |
| `bool` | `True` | Boolean / 布尔值 |
| `NoneType` | `None` | 特殊空值类型 |

查看类型：

```python
x = 1
print(type(x))

x = 1.0
print(type(x))
```

输出：

```text
<class 'int'>
<class 'float'>
```

---

## Dynamic Typing | 动态类型

Python 是 dynamically typed。

```python
x = 1
print(type(x))

x = "Alpaca"
print(type(x))
```

同一个变量名可以重新绑定到不同类型的对象。

---

# 6. Boolean | 布尔值

```python
x = True
print(type(x))

x = False
print(type(x))
```

Boolean 主要用于：

- 条件判断
- 分支逻辑
- `if / else`

---

# 7. Input & Output | 输入与输出

## `print()`

用于向 Console 输出内容：

```python
x = 10
print(x)
```

## `input()`

用于获取用户输入：

```python
name = input("Enter your name: ")
print(name)
```

---

## Important: `input()` always returns `str`

即使用户输入：

```text
5
```

Python 仍然会把它当成：

```text
"5"
```

也就是字符串。

例如：

```python
x = input("Enter a number: ")

print(x)
print(type(x))
```

会得到：

```text
<class 'str'>
```

---

# 8. Type Conversion | 类型转换

## `str → int`

```python
x = input("Enter a number: ")
x = int(x)
```

也可以直接：

```python
x = int(input("Enter a number: "))
```

## `str → float`

```python
height = float(input("Enter your height: "))
```

适合可能带小数的输入。

## `int / float → str`

```python
age = 22

print("I am " + str(age) + " years old.")
```

---

# 9. Strings | 字符串

## String Concatenation | 字符串拼接

```python
first_name = "Yang"
last_name = "Zhang"

print(last_name + " " + first_name)
```

结果：

```text
Zhang Yang
```

## String vs Number

```python
"10" + "5"
```

结果：

```text
"105"
```

而：

```python
10 + 5
```

结果：

```text
15
```

## String Repetition | 字符串重复

```python
n = "5"

print(n * 2)
print(n * 3)
```

结果：

```text
55
555
```

---

# 10. Expressions | 表达式

表达式通常由：

```text
<object> <operator> <object>
```

组成。

例如：

```python
5 + 3
```

其中：

```text
5   → object
+   → operator
3   → object
```

整个表达式最终会产生一个 value。

---

# 11. Arithmetic Operators | 算术运算符

| Operator | Meaning |
|---|---|
| `+` | Addition / 加法 |
| `-` | Subtraction / 减法 |
| `*` | Multiplication / 乘法 |
| `/` | Division / 普通除法 |
| `//` | Floor division / 向下取整除法 |
| `%` | Modulo / 取余 |
| `**` | Exponentiation / 幂 |

---

# 12. `/`, `//`, `%`

```python
print(17 / 3)
print(17 // 3)
print(17 % 3)
```

结果：

```text
5.666666666666667
5
2
```

## `/`

普通除法：

```python
10 / 2
```

得到：

```text
5.0
```

即使结果看起来是整数，`/` 仍然返回 `float`。

## `//`

Floor division：

```python
17 // 3
```

得到：

```text
5
```

## `%`

Modulo / 取余：

```python
17 % 3
```

得到：

```text
2
```

因为：

```text
17 = 3 × 5 + 2
```

---

# 13. Quotient + Remainder | 商与余数

```python
number = 17
divisor = 3

original = (number // divisor) * divisor + (number % divisor)

print(original)
```

可以理解为：

```text
原数 = 商 × 除数 + 余数
```

---

# 14. Operator Precedence | 运算优先级

目前需要记住：

```text
()
↓
* / // %
↓
+ -
```

例如：

```python
2 + 3 * 4
```

先计算：

```text
3 * 4 = 12
```

再：

```text
2 + 12 = 14
```

而：

```python
(2 + 3) * 4
```

先算括号：

```text
2 + 3 = 5
5 * 4 = 20
```

同一级别的 `* / // %` 一般从左往右计算。

例如：

```python
20 / 5 * 2
```

结果：

```text
20 / 5 = 4.0
4.0 * 2 = 8.0
```

> **本周重点复习：运算优先级。**

---

# 15. Comparison Operators | 比较运算符

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

例如：

```python
4 == 5
```

结果：

```text
False
```

而：

```python
4 != 5
```

结果：

```text
True
```

---

# 16. `=` vs `==`

```python
x = 5
```

表示：

```text
Assignment / 赋值
```

而：

```python
x == 5
```

表示：

```text
Comparison / 判断是否相等
```

---

# 17. Logic Operators | 逻辑运算符

本周课件介绍：

```python
and
or
```

例如：

```python
surfing = True
work = False

print(surfing and work)
print(surfing or work)
```

逻辑表：

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

---

# 18. Augmented Assignment | 复合赋值

```python
x = x + 5
```

可以写成：

```python
x += 5
```

其他形式：

```python
x -= 3
x *= 2
x /= 2
x **= 3
```

例如：

```python
x = 4
x **= 3
```

结果：

```text
64
```

---

# 19. Variable Naming | 变量命名

推荐：

```python
height
weight
bmi
start_hour
final_minute
easy_pace_time
```

不推荐长期大量使用：

```python
x
y
z
```

变量名应该尽量表达它代表什么。

## Naming Rules

变量名可以包含：

```text
A-Z
a-z
0-9
_
```

但不能：

```text
以数字开头
```

Python 变量名区分大小写：

```python
alpaca
Alpaca
```

是两个不同变量。

---

# 20. Comments | 注释

单行注释：

```python
# Calculate BMI
```

注释的主要作用是提高可读性。

---

# 21. Basic `if / else`

本周在奇偶判断练习中实际使用：

```python
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

基本结构：

```python
if condition:
    code
else:
    code
```

Python 使用缩进表示代码块，通常使用 4 个空格。

---

# 22. Exercise 1 — Square and Cube | 平方与立方

```python
number = int(input("Enter a number: "))

square = number * number
cube = number * number * number

print(square)
print(cube)
```

---

# 23. Exercise 2 — BMI Calculator

```python
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / (height * height)

print("Your BMI is " + str(bmi))
```

最初错误：

```python
bmi = weight / height * height
```

Python 实际会按：

```text
(weight / height) * height
```

执行。

正确：

```python
bmi = weight / (height * height)
```

---

# 24. Exercise 3 — `(x + y) * (x + y)`

```python
x = int(input("Please enter an integer: "))
y = int(input("Please enter an integer: "))

result = (x + y) * (x + y)

print("Your result is " + str(result))
```

---

# 25. Exercise 4 — 12-Hour Clock

```python
start_time = 8
hours_later = 9

final_time = (start_time + hours_later) % 12

print(str(final_time) + " pm")
```

核心：

```text
8 + 9 = 17
17 % 12 = 5
```

说明 `%` 可以处理周期性问题。

---

# 26. Input Exercise — Welcome Message

```python
name = input("Please enter your name: ")

print("Hello " + name + ", would you like to learn some Python today?")
```

因为 `input()` 已经返回 `str`：

```python
str(input(...))
```

是多余的。

---

# 27. First Name + Last Name

```python
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Welcome " + last_name + " " + first_name + "!")
```

---

# 28. Challenge — `n + nn + nnn`

```python
n = input("Please enter an integer: ")

nn = n * 2
nnn = n * 3

result = int(n) + int(nn) + int(nnn)

print(result)
```

例如：

```text
n = "5"
nn = "55"
nnn = "555"

5 + 55 + 555 = 615
```

这里利用了：

```text
字符串重复
+
类型转换
```

---

# 29. Challenge — Even or Odd

```python
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

核心：

```text
偶数 % 2 = 0
```

---

# 30. Challenge — Sum of Four Digits

目标：

```text
1234
↓
1 + 2 + 3 + 4
↓
10
```

核心技巧：

```text
% 10  → 取最后一位
// 10 → 去掉最后一位
```

代码：

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

注意：

```text
digit1 实际是个位
digit2 是十位
digit3 是百位
digit4 是千位
```

---

# 31. Challenge — Running Time

题目：

```text
Start: 6:52 am

1 mile @ 8:15
3 miles @ 7:12
1 mile @ 8:15
```

## Step 1 — Convert to seconds

```text
8 × 60 + 15 = 495 seconds
7 × 60 + 12 = 432 seconds
432 × 3 = 1296 seconds
```

总时间：

```text
495 + 1296 + 495
= 2286 seconds
```

## Step 2 — Convert seconds back

```text
2286 // 60 = 38
2286 % 60 = 6
```

即：

```text
38 minutes 6 seconds
```

## Step 3 — Add to start time

```text
52 + 38 = 90 minutes
90 // 60 = 1 hour
90 % 60 = 30 minutes
```

最终：

```text
7:30:06 am
```

代码：

```python
easy_pace_time = 8 * 60 + 15
tempo_pace_time = (7 * 60 + 12) * 3

total_time = easy_pace_time * 2 + tempo_pace_time

cost_minute = total_time // 60
final_second = total_time % 60

start_hour = 6
start_minute = 52

total_minute = start_minute + cost_minute

final_hour = start_hour + total_minute // 60
final_minute = total_minute % 60

print(
    str(final_hour)
    + ":"
    + str(final_minute)
    + ":"
    + str(final_second)
    + " am"
)
```

---

# 32. Debugging Notes | 调试记录

## Chinese Full-Width Brackets

错误：

```text
invalid character '（' (U+FF08)
```

错误写法：

```python
print（x）
```

正确：

```python
print(x)
```

写 Python 时尽量切换到英文输入法。

---

## `str + int`

错误：

```python
x = 5

print("The number is " + x)
```

正确：

```python
print("The number is " + str(x))
```

---

## `=` vs `==`

错误：

```python
if number % 2 = 0:
```

正确：

```python
if number % 2 == 0:
```

---

## Missing `:`

错误：

```python
else
```

正确：

```python
else:
```

---

## Indentation

```python
if number % 2 == 0:
    print("Even")
```

通常使用 4 个空格。

---

# 33. PEP 8 Basics | 基础代码规范

## 运算符两侧留空格

推荐：

```python
x = y + 5
bmi = weight / (height * height)
```

不推荐：

```python
x=y+5
```

## 函数名和括号之间不留空格

推荐：

```python
print(x)
int(x)
```

不推荐：

```python
print (x)
int (x)
```

## 逗号后加空格

```python
print(x, y, z)
```

## 注释

```python
# Calculate BMI
```

---

# 34. Spyder Notes

## Undo

```text
Ctrl + Z
```

Redo：

```text
Ctrl + Shift + Z
```

部分情况下：

```text
Ctrl + Y
```

## `input()` blocks execution

如果程序运行到：

```python
name = input("Enter your name: ")
```

程序会暂停并等待输入。

如果 Spyder 正在运行整个文件，那么它可能先停在前面的 `input()`，即使当前正在查看后面的代码。

---

# 35. What I Can Do Now | 本周已经掌握

- [x] 创建变量
- [x] 理解 `=` 是赋值
- [x] 使用 `int`
- [x] 使用 `float`
- [x] 使用 `str`
- [x] 使用 `bool`
- [x] 认识 `None`
- [x] 使用 `type()`
- [x] 使用 `input()`
- [x] 使用 `print()`
- [x] 使用 `int()`
- [x] 使用 `float()`
- [x] 使用 `str()`
- [x] 字符串拼接
- [x] 字符串重复
- [x] 使用 `/`
- [x] 使用 `//`
- [x] 使用 `%`
- [x] 使用 `**`
- [x] 理解基础比较运算
- [x] 区分 `=` 和 `==`
- [x] 基础 `if / else`
- [x] 判断奇偶数
- [x] 使用 `% 10` 拆数字
- [x] 使用 `// 10` 删除最后一位
- [x] 使用 `// 60` 和 `% 60` 处理时间
- [x] 阅读简单 Python 报错
- [x] 使用基础 PEP 8 风格
- [x] 开始把问题拆成多个步骤

---

# 36. Things to Review | 待复习

- [ ] 加强运算优先级
- [ ] 熟练区分 `/`、`//`、`%`
- [ ] 继续练习 comparison operators
- [ ] 熟练写 `if / else`
- [ ] 保持 4 空格缩进
- [ ] 熟练类型转换
- [ ] 使用更有意义的变量名
- [ ] 继续遵守基本 PEP 8 格式
- [ ] 做题前先写出解题步骤
- [ ] 尽量先独立尝试，再查看提示

---

# Week 01 Summary | 第一周总结

这一周从最基础的：

```python
x = 1
```

逐渐学习到：

```text
Variables
↓
Objects & Types
↓
Input / Output
↓
Type Conversion
↓
Strings
↓
Expressions
↓
Operators
↓
/ // %
↓
Comparison
↓
Basic if / else
↓
Problem Decomposition
↓
Debugging
```

本周最大的收获不是某一条具体语法，而是开始理解：

> **先理解问题，再拆解问题，最后再写代码。**

下一步重点：

> **继续加强运算优先级、条件判断和独立解决问题的能力。**
