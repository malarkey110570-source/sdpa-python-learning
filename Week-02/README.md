# Week 02 — Branching and Looping  
# 第二周 — 条件分支与循环

## Overview | 本周概述

This week focused on **control flow in Python**, especially how a program makes decisions and repeats instructions.

本周主要学习 Python 中的 **控制流程（Control Flow）**，重点理解程序如何根据条件作出判断，以及如何重复执行代码。

The content was divided into:

- **Lecture:** Branching and Looping
- **Tutorial:** Control-flow exercises and programming practice

本周内容主要分为：

- **Lecture：** 条件分支与循环
- **Tutorial：** 控制流程练习与编程实践

---

# Part 1 — Lecture  
# 第一部分 — Lecture 课堂内容

## 1. Control Flow | 控制流程

Normally, Python executes code from top to bottom.

通常情况下，Python 会按照代码从上到下的顺序执行。

For example:

```python
print("A")
print("B")
print("C")
```

Output:

```text
A
B
C
```

However, control-flow statements allow us to change this execution order.

但是，通过控制流程语句，我们可以改变程序执行代码的方式。

The two main ideas studied this week were:

本周主要学习两种控制方式：

1. **Branching / Selection — 条件分支**
2. **Looping / Iteration — 循环**

---

# 2. Boolean Conditions | 布尔条件

A condition evaluates to either:

一个条件表达式最终会得到：

```python
True
```

or:

```python
False
```

For example:

```python
x = 10

print(x > 5)
```

Output:

```text
True
```

Conditions are the foundation of `if` statements and loops.

条件判断是 `if` 语句以及循环的重要基础。

---

# 3. Comparison Operators | 比较运算符

Python provides several comparison operators.

Python 中常用的比较运算符包括：

| Operator 运算符 | Meaning 含义 |
|---|---|
| `==` | Equal to 等于 |
| `!=` | Not equal to 不等于 |
| `>` | Greater than 大于 |
| `<` | Less than 小于 |
| `>=` | Greater than or equal to 大于等于 |
| `<=` | Less than or equal to 小于等于 |

Example:

```python
x = 5

print(x == 5)
print(x != 5)
```

Output:

```text
True
False
```

### Important distinction | 重要区别

```python
=
```

means **assignment**.

表示 **赋值**。

```python
x = 5
```

means:

> Store the value `5` in the variable `x`.

意思是：

> 把数值 `5` 赋给变量 `x`。

However:

```python
==
```

means **comparison**.

表示 **比较两个值是否相等**。

```python
x == 5
```

asks:

> Is `x` equal to `5`?

即：

> `x` 是否等于 `5`？

---

# 4. if Statement | if 条件语句

The simplest form of branching uses `if`.

最基本的条件判断使用 `if`。

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

Output:

```text
x is greater than 5
```

Python first checks:

Python 首先判断：

```python
x > 5
```

If the result is `True`, the indented code runs.

如果结果为 `True`，就执行缩进部分的代码。

---

# 5. if / else | 二选一判断

An `else` block runs when the `if` condition is `False`.

如果 `if` 条件为 `False`，程序可以执行 `else` 中的代码。

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

这里使用：

```python
number % 2
```

来计算除以 `2` 后的余数。

If the remainder is `0`, the number is even.

如果余数是 `0`，说明数字是偶数。

---

# 6. if / elif / else | 多条件判断

When there are several possible conditions, Python uses:

如果程序需要判断多个条件，可以使用：

```python
if
elif
else
```

Example:

```python
x = 3
y = 8

if x == y:
    print("x and y are equal")
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
```

Output:

```text
x is smaller
```

Python checks conditions **from top to bottom**.

Python 会按照 **从上到下** 的顺序检查条件。

Once one condition is `True`, that branch runs and the remaining branches are skipped.

一旦某个条件为 `True`，Python 就执行对应代码，后面的分支不会继续判断。

---

# 7. Nested if Statements | 嵌套 if

An `if` statement can be placed inside another `if`.

一个 `if` 里面还可以继续放另一个 `if`。

Example:

```python
x = 15

if x > 10:
    print("Above ten")

    if x > 20:
        print("Above twenty")
    else:
        print("Not above twenty")
```

Output:

```text
Above ten
Not above twenty
```

Execution process:

执行顺序：

```text
x > 10 ?
   ↓
 True
   ↓
Enter outer if
进入外层 if
   ↓
x > 20 ?
   ↓
 False
   ↓
Run inner else
执行内层 else
```

An important idea is:

重要的一点是：

> The inner `if` is only checked after the outer `if` condition is satisfied.

> 只有外层 `if` 成立以后，程序才会进入内部继续进行第二次判断。

---

# 8. Understanding Indentation | 理解缩进

Indentation is extremely important in Python.

Python 中的缩进非常重要。

Correct:

```python
if x > 5:
    print("Greater than 5")
```

Incorrect:

```python
if x > 5:
print("Greater than 5")
```

Python uses indentation to determine which statements belong to a block.

Python 使用缩进来判断哪些代码属于同一个代码块。

PEP 8 normally recommends:

PEP 8 通常建议：

```text
4 spaces
```

for each indentation level.

即每一级缩进使用 **4 个空格**。

---

# 9. for Loops | for 循环

A `for` loop repeats code for a sequence of values.

`for` 循环可以让程序针对一组数据重复执行代码。

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

This is because:

这是因为：

```python
range(5)
```

produces:

产生：

```text
0, 1, 2, 3, 4
```

The final value `5` is not included.

需要注意：`5` 本身不会被包括进去。

---

# 10. range() | range 函数

`range()` is commonly used together with a `for` loop.

`range()` 经常与 `for` 循环一起使用。

## range(stop)

```python
range(5)
```

Produces:

```text
0, 1, 2, 3, 4
```

---

## range(start, stop)

```python
range(1, 5)
```

Produces:

```text
1, 2, 3, 4
```

---

## range(start, stop, step)

```python
range(1, 8, 2)
```

Produces:

```text
1, 3, 5, 7
```

Example:

```python
for i in range(1, 8, 2):
    print(i)
```

Output:

```text
1
3
5
7
```

General form:

通用形式：

```python
range(start, stop, step)
```

可以理解为：

```text
起始位置，停止位置，步长
```

Remember:

需要记住：

> `stop` is not included.

> `stop` 对应的数字不会被包含。

---

# 11. while Loops | while 循环

A `while` loop continues executing while a condition remains `True`.

只要条件一直为 `True`，`while` 循环就会不断执行。

Example:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Output:

```text
0
1
2
3
4
```

Execution:

执行过程：

```text
count = 0
    ↓
count < 5 ?
    ↓
True
    ↓
print(count)
    ↓
count += 1
    ↓
Check condition again
再次判断条件
```

When:

当：

```python
count = 5
```

the condition:

条件：

```python
count < 5
```

becomes:

变成：

```text
False
```

so the loop stops.

因此循环结束。

---

# 12. Infinite Loops | 无限循环

A common mistake with `while` loops is forgetting to update the loop variable.

使用 `while` 时，一个常见错误是忘记修改控制循环的变量。

Example:

```python
count = 0

while count < 5:
    print(count)
```

Here, `count` always remains `0`.

这里 `count` 永远都是 `0`。

Therefore:

因此：

```python
count < 5
```

is always `True`.

一直都是 `True`。

This creates an:

这会导致：

```text
Infinite Loop
无限循环
```

Correct version:

正确写法：

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

# 13. Counter Variables | 计数变量

A counter records how many times something has happened.

Counter 用于记录某件事情发生了多少次。

Example:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Here:

这里：

```python
count
```

is the counter.

就是计数变量。

---

# 14. Accumulator Variables | 累加变量

An accumulator stores a running total.

Accumulator 用来保存不断累积的结果。

Example:

```python
total = 0

for number in range(1, 11):
    total = total + number

print(total)
```

Output:

```text
55
```

The program calculates:

程序实际上进行了：

```text
1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
15 + 6 = 21
21 + 7 = 28
28 + 8 = 36
36 + 9 = 45
45 + 10 = 55
```

A shorter version is:

更简洁的写法：

```python
total += number
```

which is equivalent to:

等价于：

```python
total = total + number
```

---

# 15. Nested Loops | 嵌套循环

A loop can also be placed inside another loop.

一个循环内部还可以再放另一个循环。

Example:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

The execution process is:

执行逻辑：

```text
i = 0
    j = 0
    j = 1

i = 1
    j = 0
    j = 1

i = 2
    j = 0
    j = 1
```

The important rule is:

核心规律：

> For each single iteration of the outer loop, the inner loop completes all of its iterations.

> 外层循环每执行一次，内层循环都要完整执行一遍。

---

# Part 2 — Tutorial / Practice  
# 第二部分 — Tutorial 练习

## 1. Predicting Program Output | 判断程序输出

One important part of today's tutorial was reading code first and predicting its output without immediately running it.

今天 Tutorial 的一个重要训练是：

> **先读代码，自己判断输出，再运行程序验证。**

This helps develop an understanding of program execution.

这样可以训练自己真正理解程序是如何一步一步执行的，而不是只看最终答案。

For example:

```python
for i in range(5):
    print(i)
```

Before running the program, I should understand that:

在运行之前应该能够判断：

```python
range(5)
```

means:

```text
0, 1, 2, 3, 4
```

Therefore the output is:

因此输出：

```text
0
1
2
3
4
```

---

# 2. Following Variables Step by Step | 跟踪变量变化

For loops and `while` loops, it is useful to manually trace variable values.

对于循环程序，可以手动记录每一步变量发生了什么变化。

Example:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Trace table:

执行过程：

| Iteration 次数 | `count` before print | Output |
|---|---:|---:|
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 2 | 2 |
| 4 | 3 | 3 |
| 5 | 4 | 4 |

After that:

之后：

```python
count = 5
```

so:

所以：

```python
count < 5
```

is `False`.

循环结束。

---

# 3. Odd Number Sequence | 奇数序列

Example:

```python
for i in range(1, 8, 2):
    print(i)
```

Output:

```text
1
3
5
7
```

This helped practise understanding:

这个练习帮助理解：

```python
range(start, stop, step)
```

especially the meaning of `step`.

特别是 `step`（步长）的含义。

---

# 4. Nested Loop Output | 嵌套循环输出

One tutorial exercise involved understanding the following pattern:

Tutorial 中练习了类似这样的嵌套循环：

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output:

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

My understanding:

我的理解：

When:

当：

```python
i = 0
```

the complete inner loop runs:

内层循环完整执行：

```text
j = 0
j = 1
```

Then `i` becomes `1`.

之后外层 `i` 才变成 `1`。

---

# 5. Accumulator Exercise — Sum 1 to 10  
# 累加练习 — 计算 1 到 10 的总和

The tutorial included an accumulator-style problem.

Tutorial 中练习了使用累加变量计算总和。

Goal:

目标：

```text
1 + 2 + 3 + ... + 10
```

Code:

```python
total = 0

for number in range(1, 11):
    total += number

print(total)
```

Output:

```text
55
```

Step-by-step:

逐步变化：

```text
1
3
6
10
15
21
28
36
45
55
```

This exercise helped me understand that `total` must preserve the previous result.

这个练习让我理解：

> `total` 需要保存上一次循环计算出来的结果，然后继续累加新的数字。

---

# 6. Nested Loop Pattern Exercise | 嵌套循环图案练习

Another exercise involved using nested loops to print repeated symbols.

另一个练习是使用嵌套循环打印重复图案。

Example:

```python
rows = 5

for i in range(1, rows + 1):
    for j in range(1, 4):
        print("*", end=" ")
    print()
```

Output:

```text
* * *
* * *
* * *
* * *
* * *
```

The outer loop controls:

外层循环控制：

```text
Rows
行数
```

The inner loop controls:

内层循环控制：

```text
Number of stars in each row
每一行打印多少个 *
```

---

# 7. Understanding end="" | 理解 end 参数

Normally:

通常：

```python
print("*")
```

automatically moves to a new line.

每次 `print()` 执行完成后都会自动换行。

For example:

```python
print("*")
print("*")
print("*")
```

Output:

```text
*
*
*
```

However:

但是：

```python
print("*", end=" ")
```

prevents an immediate new line.

会阻止 `print()` 立即换行。

Example:

```python
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
```

Output:

```text
* * *
```

Then:

随后使用：

```python
print()
```

creates the new line.

来进行换行。

This is useful when printing patterns with nested loops.

这在使用嵌套循环打印图案时非常重要。

---

# 8. Reading Nested Code | 阅读嵌套代码的方法

When reading nested loops or nested `if` statements, I should work from the outside to the inside.

阅读嵌套结构时，可以遵循：

```text
Outer → Inner
外层 → 内层
```

For nested loops:

对于嵌套循环：

```text
Outer loop runs once
外层执行一次
        ↓
Inner loop runs completely
内层完整执行
        ↓
Outer loop moves to next value
外层进入下一个值
```

This makes complicated code easier to understand.

这样可以避免看到两个循环就混乱。

---

# Key Concepts Learned  
# 本周核心知识点

| Concept | 中文理解 |
|---|---|
| Control Flow | 控制程序执行顺序 |
| Boolean | `True` / `False` |
| `if` | 条件成立时执行代码 |
| `elif` | 判断其他条件 |
| `else` | 前面条件都不成立时执行 |
| Nested `if` | if 中再进行条件判断 |
| `for` | 按一定范围或序列循环 |
| `while` | 条件为 True 时持续循环 |
| `range()` | 生成循环使用的整数序列 |
| Counter | 记录循环次数 |
| Accumulator | 保存并累积结果 |
| Nested Loop | 循环内部再运行循环 |
| `end=""` | 控制 `print()` 是否立即换行 |
| Indentation | 表示 Python 代码块结构 |

---

# Common Mistakes  
# 常见错误

## 1. Confusing `=` and `==`  
## 混淆赋值和比较

Wrong:

```python
if x = 5:
```

Correct:

```python
if x == 5:
```

---

## 2. Writing `! =` instead of `!=`

Wrong:

```python
if y ! = 0:
```

Correct:

```python
if y != 0:
```

`!=` must be written together.

`!=` 中间不能加空格。

---

## 3. Forgetting the colon  
## 忘记冒号

Wrong:

```python
if x > 5
```

Correct:

```python
if x > 5:
```

This also applies to:

同样适用于：

```python
if
elif
else
for
while
```

---

## 4. Incorrect indentation  
## 缩进错误

Wrong:

```python
if x > 5:
print(x)
```

Correct:

```python
if x > 5:
    print(x)
```

---

## 5. Forgetting to update a while-loop variable  
## while 循环忘记更新变量

Wrong:

```python
count = 0

while count < 5:
    print(count)
```

This creates an infinite loop.

这会造成无限循环。

Correct:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

## 6. Forgetting that range() excludes stop  
## 忘记 range 不包含 stop

```python
range(1, 5)
```

means:

```text
1, 2, 3, 4
```

not:

而不是：

```text
1, 2, 3, 4, 5
```

---

# My Understanding After Week 2  
# Week 2 学习后的个人理解

After this week, I have started to understand that programming is not only about writing statements one after another.

经过 Week 2 的学习，我开始理解程序并不是简单地把一行一行代码从上到下写出来。

The important question is:

更重要的是要思考：

```text
Which code should run?
哪些代码应该执行？

When should it run?
什么时候执行？

How many times should it run?
应该执行多少次？
```

Branching solves:

条件判断主要解决：

```text
Should this code run?
这段代码应不应该执行？
```

Loops solve:

循环主要解决：

```text
How many times should this code run?
这段代码应该重复执行多少次？
```

Nested structures combine these ideas and allow more complex programs to be created.

嵌套结构则把这些逻辑组合起来，使程序可以完成更加复杂的任务。

---

# Week 2 Summary  
# Week 2 总结

This week I learned:

本周我学习了：

- How Boolean conditions work  
  布尔条件如何工作

- How to use `if`, `elif`, and `else`  
  如何使用条件分支

- How nested `if` statements work  
  如何理解嵌套条件

- How `for` loops work  
  `for` 循环的运行方式

- How `while` loops work  
  `while` 循环的运行方式

- How `range()` controls loops  
  如何使用 `range()` 控制循环

- How counters and accumulators work  
  如何使用计数变量和累加变量

- How nested loops execute  
  嵌套循环的执行顺序

- How to predict program output before running code  
  如何在运行代码之前分析程序输出

- How to use loops to calculate totals and print patterns  
  如何使用循环完成累加以及图案打印

---

## Next Step | 下一步

Continue practising control flow until I can read simple Python code and predict its output without running it first.

继续练习条件与循环，目标是：

> **看到简单的 Python 控制流程代码后，可以先在脑中分析执行过程和输出，而不是必须依赖运行代码才能知道结果。**

This will provide an important foundation for more advanced Python programming.

这会为后续更复杂的 Python 编程打下基础。
