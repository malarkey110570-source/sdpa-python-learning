````markdown
# SDPA Python Learning Journey

> Learning Python through SDPA — one bug at a time.  
> 通过 SDPA 学习 Python，在一个个 Bug 中进步。

This repository records my real learning process in the **EMATM0048 Software Development: Programming and Algorithms (SDPA)** course at the University of Bristol.

本仓库用于记录我在布里斯托大学 **EMATM0048 — Software Development: Programming and Algorithms (SDPA)** 课程中的 Python 学习过程。

Rather than only storing finished solutions, I also keep early attempts, mistakes, debugging notes, and improved versions of my code.

相比只保存最终答案，我更希望记录真实的学习轨迹，包括最初的代码、出现的错误、调试过程以及后续改进。

---

## Learning Goals | 学习目标

- Build a solid foundation in Python  
  建立扎实的 Python 基础

- Practise solving programming problems independently  
  练习独立分析和解决编程问题

- Learn from mistakes and keep useful debugging notes  
  从错误中学习，并记录有价值的调试经验

- Develop better coding style and readable variable naming  
  逐渐养成规范、可读的代码习惯

- Understand the logic behind code instead of only memorising syntax  
  理解代码背后的逻辑，而不是单纯记忆语法

- Turn suitable ideas into small projects over time  
  将适合的想法逐步发展成小项目

---

## Current Progress | 当前进度

### Week 01 — Completed ✅

Week 01 focused on the fundamentals of Python programming.

第一周主要完成了 Python 编程基础学习，包括：

- Variables and assignment | 变量与赋值
- Basic data types | 基本数据类型
  - `int`
  - `float`
  - `str`
  - `bool`
- `input()` and `print()` | 输入与输出
- Type conversion | 类型转换
- String operations | 字符串操作
- Arithmetic operators | 算术运算符
- `/`, `//`, and `%`
- Operator precedence | 运算优先级
- Basic comparison with `==`
- Basic `if / else` logic | 基础条件判断
- Simple debugging and code formatting | 基础调试与代码规范

A major focus this week was learning how to break a larger problem into smaller steps before translating it into Python.

本周一个重要的收获是开始学习：

> **Break the problem down first, then translate each step into Python.**  
> **先拆解问题，再把每一步翻译成 Python。**

---

## Learning Log | 学习日志

| Week | Status | Main Topics |
|---|---|---|
| [Week 01](week-01/README.md) | ✅ Completed | Python basics, input/output, types, operators, `if / else` |
| Week 02 | ⏳ Coming soon | To be updated |

Future week folders will only be created when that week's learning begins.

后续周文件夹只会在对应课程真正开始学习后创建。

---

## Week Index | 周目录

- [Week 01 — Python Basics](week-01/README.md)
- Week 02 — Coming soon

Each weekly folder contains notes based on what I actually studied that week.

每周目录将主要记录：

- Course topics | 课程知识点
- Tutorial work | Tutorial 练习
- Exercises | 编程练习
- Challenges | 挑战题
- Mistakes and debugging | 错误与调试
- What I learned | 学习总结
- Things to review | 待复习内容

---

## Python Topics | Python 知识进度

### Fundamentals

- [x] Variables and assignment
- [x] `int`
- [x] `float`
- [x] `str`
- [x] `bool`
- [x] `type()`
- [x] `input()`
- [x] `print()`
- [x] Type conversion
- [x] String concatenation
- [x] String repetition

### Operators

- [x] `+`
- [x] `-`
- [x] `*`
- [x] `/`
- [x] `//`
- [x] `%`
- [x] Basic `**`
- [x] `==`
- [x] Operator precedence

### Control Flow

- [x] Basic `if`
- [x] Basic `else`
- [x] Indentation
- [ ] More complex conditions
- [ ] `elif`
- [ ] Loops
- [ ] Functions

Topics are marked as completed only after they have actually been studied or used.

只有真正学习或实际使用过的知识点才会被标记为完成。

---

## Week 01 Highlights | 第一周练习亮点

Some of the problems completed during Week 01 include:

本周完成的部分练习包括：

- Calculate the square and cube of a number  
  计算一个数字的平方和立方

- Build a simple BMI calculator  
  编写简单 BMI 计算程序

- Calculate `(x + y) * (x + y)`  
  使用括号控制运算顺序

- Calculate time on a 12-hour clock using `%`  
  使用 `%` 处理 12 小时制循环

- Reverse first name and last name output  
  反向输出姓和名

- Calculate `n + nn + nnn` using string operations  
  利用字符串操作完成 `n + nn + nnn`

- Determine whether a number is even or odd  
  判断整数的奇偶性

- Calculate the sum of the digits in a four-digit integer  
  使用 `% 10` 和 `// 10` 拆分四位整数

- Solve a running-time calculation using seconds, `//`, and `%`  
  使用统一时间单位、整除和取余解决跑步时间 Challenge

---

## Debugging Notes | 调试记录

Mistakes are intentionally kept as part of the learning process.

错误不是需要隐藏的内容，而是本仓库学习记录的一部分。

Some issues encountered so far:

```text
invalid character '（' (U+FF08)
````

Cause:

```text
Chinese full-width brackets （）
instead of
English half-width brackets ()
```

Other mistakes included:

```text
=   vs   ==
```

```text
str + int
```

```text
missing :
```

and incorrect operator precedence assumptions.

These mistakes are documented because understanding **why something failed** is often more useful than simply seeing the final correct answer.

---

## Coding Style | 代码规范

I am gradually following basic Python style conventions while learning.

目前正在逐渐养成以下代码习惯：

```python
x = y + 5
```

instead of:

```python
x=y+5
```

Use descriptive variable names:

```python
start_hour
final_minute
easy_pace_time
```

instead of relying too heavily on:

```python
x
y
z
```

Other habits:

* Four-space indentation
* Spaces around binary operators
* `snake_case` variable names
* Clear comments
* Meaningful variable names

---

## Things I Am Currently Improving | 当前重点提升

### Operator Precedence

One area that still needs more practice is operator precedence.

目前需要重点加强：

```text
()
↓
* / // %
↓
+ -
```

Operators at the same precedence level are generally evaluated from left to right.

Example:

```python
20 / 5 * 2
```

becomes:

```text
20 / 5 = 4.0
4.0 * 2 = 8.0
```

---

## Mini Projects | 小项目

No dedicated mini projects yet.

目前暂时没有独立 Mini Project。

The priority is to build a strong foundation first. Suitable ideas will gradually be developed into small projects as more Python concepts are learned.

现阶段优先打好 Python 基础。随着课程继续推进，会逐步将合适的想法发展成小项目。

---

## Repository Philosophy | 仓库记录原则

This repository is not intended to show only perfect code.

It is intended to show progress.

这里不会只保存“正确答案”。

我希望 Git history 能真实记录：

```text
I don't know
↓
I try
↓
I get an error
↓
I understand why
↓
I fix it
↓
I learn something
```

The goal is not to pretend that every problem was easy.

The goal is to become better at solving the next one.

---

## Learning Progress | 学习进度

### Week 01

✅ Completed the first Python tutorial.

Current understanding includes:

```text
variables
data types
input / output
type conversion
strings
/ // %
basic conditions
basic debugging
problem decomposition
```

Next step:

> Continue strengthening Python fundamentals and problem-solving skills before moving into more advanced programming concepts.

继续巩固基础语法、运算逻辑与独立解决问题的能力，再逐步进入更复杂的 Python 内容.

```

这一版和你的 `week-01/README.md` 是配套的：

**根目录 README = 整个学习旅程的 Dashboard**

**`week-01/README.md` = 第一周详细学习记录**

以后 Week 02 开始时，根 README 只需要更新 `Current Progress`、`Learning Log` 和 `Python Topics`，不用每周全部重写。
```
