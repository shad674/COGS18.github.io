---
interact_link: content/materials/Exam1-Practice.ipynb
download_link: assets/downloads/Exam1-Practice.ipynb.zip
pdf_link: assets/pdf/Exam1-Practice.pdf
layout: materials
title: 'Exam1-Practice'
prev_page:
  url: /materials/Exam1-Review
  title: 'Exam1-Review'
next_page:
  url: /materials/E1-Answers
  title: 'E1-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Exam #1 Practice Questions

To practice for the first exam, read through each of these questions and try and answer the question _before_ you run the code.

Since this is a notebook, you can also then run this code to check what it does. 

Make sure you understand why each thing does what it does!

## Variables & Operators

For each of the following cells, after executing the code, what will the value of `var_a` be?



{:.input_area}
```python
# Variables-1
var_b = 2
var_a = var_b = 2%3
```




{:.input_area}
```python
# Variables-2
var_b = False 
var_c = True
var_d = True
var_a = var_b or var_c or var_d
```




{:.input_area}
```python
# Variables-3
var_b = 2**3
var_c = 2
var_a = float(var_b/var_c)
```




{:.input_area}
```python
# Variables-4
var_a = 5**2 <= 30 or 25%4 > 1
```


## Indexing

Given the following list:



{:.input_area}
```python
my_lst = ['Python', True, 12, 'Java', False, None, 23, 'C++']
```


What will each of the following code cells print out?



{:.input_area}
```python
len(my_lst)
```




{:.input_area}
```python
my_lst[1:4]
```




{:.input_area}
```python
my_lst[-3:]
```




{:.input_area}
```python
my_lst[1::2]
```




{:.input_area}
```python
my_lst[1:6:2]
```


## Conditionals

### Conditionals 1

What will the following code print out?



{:.input_area}
```python
if True and not False:
    print('Yay')
elif False or not False:
    print('Also yay')
```


### Conditionals 2

What will the following code print out?

a) 1  b) 2  c) broken d) 3 e) This code won't execute



{:.input_area}
```python
if 10%2 == 5:
    print('1')
elif True and False or False:
    print('2')
elif 5/0:
    print('broken')
else:
    print('3')
```


## Loops

### Loops 1

What will the following code print out:

A) 0 | B) 1 | C) 2 | D) 3 | E) 4



{:.input_area}
```python
counter = 0
my_lst = [True, 3, False, False]
for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1
        break
```


### Loops 2

What will the following code print out:

A) 1 4 9 16 | B) 1 2 3 4| C)9 16 25 | | D) 1 4 9



{:.input_area}
```python
my_lst = [1, 2, 3, 4, 5]

for item in my_lst[0:-2]:
    print(item**2)
```


### Loops 3

What will the following code print out:



{:.input_area}
```python
index_outer = 1
while index_outer < 4:
    
    index_inner = 1
    
    while index_inner <= index_outer:
        print(index_inner, end=" ")
        index_inner = index_inner + 1
        
    print("")
    index_outer = index_outer + 1
```
