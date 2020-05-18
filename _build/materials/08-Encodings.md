---
interact_link: content/materials/08-Encodings.ipynb
download_link: assets/downloads/08-Encodings.ipynb.zip
pdf_link: assets/pdf/08-Encodings.pdf
layout: materials
title: '08-Encodings'
prev_page:
  url: /materials/07-Loops
  title: '07-Loops'
next_page:
  url: /materials/09-FunctionsI
  title: '09-FunctionsI'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

- **A2** due Monday (11:59 PM)
- **Exam I** _next_ Friday (4/24)
- Coding Labs Chat
    - **CL2** 'grades' posted
    - **CL3** 'answers' posted
    - A note about Coding Labs (& general frustration)

![I tried!](img/itried.png)

# Encodings & Dictionaries

- symbols & representations
- Encodings
- Dictionaries
- `ord` & `chr`

What is a human representaion? human encoding? 

How do computers encode information?

#### Clicker Question #1

What is a symbol?

- A) A character that can be typed on a computer
- B) Something that can stand in the place of something else
- C) Something that looks like something else
- D) A character or sign used to represent something arbitrary
- E) I have no idea

## Symbols

<div class="alert alert-success">
Symbols are characters (or 'signs') of arbitrary shape, that can refer to (or represent) something. 
</div>

##  Representation

<div class="alert alert-success">
To represent means to stand in for something.
</div>

- **iconic representation** : the object looks like the thing it represents (i.e. a picture)
- **symbolic representation** : the symbol does *not* look like the thing it represents (i.e. letters, numbers) 


### Symbol Examples : concepts

- The symbol `2` represents the concept of `two-ness`. 
    - This is arbitrary: there is nothing 'two-like' about `2`
    - We need not use this symbol. The symbol `II` also represent `two-ness`.
    - `2` and `II` are two different representations for the concept of two.
- The symbol `b`, in english represents the sound `buh` (sort of). 
    - There is nothing 'buh' like about the symbol `b`

### Symbol Examples : rules

Given the symbol `2`, or `b` we have systematic rules of things we can do with them. 
- We can take `2` and add `1` and get a new symbol which represents the concept of `the value one bigger than two`
- We can concatenate some, but not all, other letters (symbols) to `b` to start making rules
- These rules are agnostic to what `2` or `b` represent, they are simply manipulations we can do with these symbols

## Digital Computers

Computers don't care about what the symbols look like. They don't care what symbols you use.

But, once a rule is established for a certain symbol, the computer will always follow that rule. 

<div class="alert alert-success">
Computation is symbol manipulation - using formal rules to manipulate symbols. 
</div>

Whenever we have symbols, and rules to manipulate them, we can do computation. 

When we use these symbols that represent meaningful things, we can use computers to make meaningful inferences.

Everything you think of as a computer (laptop, cell phone, etc.) works as a digital computer.

##  Encoding & Decoding

<div class="alert alert-success">
Encoding can be thought of as the process of 'changing representation', and decoding as the process of changing it back. 
</div>

Changing back and forth between using the symbol '2' and 'II' to represent the concept of two is an example of "changing representation."

## Aside: Binary

Fundamentally, digital computers can represent two states. Because of this, we say computers are / use binary. 

From binary, we can build up to store other things, that reduce down to binary representations.

We can then encode any value we would like to represent on our computer.  

### Binary in Code



{:.input_area}
```python
## The `bin` operator returns the binary representation of an integer
# encoding an integer
print(bin(1))
```


{:.output_stream}
```
0b1

```



{:.input_area}
```python
print(bin(78))
```


{:.output_stream}
```
0b1001110

```



{:.input_area}
```python
#possible to encode Booleans in binary
#encoding a boolean
bin(False)
```





{:.output_data_text}
```
'0b0'
```





{:.input_area}
```python
print(bool(0b0))
```


{:.output_stream}
```
False

```



{:.input_area}
```python
# We can also convert binary back to integers with 
# decoding from binary
int(0b1011)
```





{:.output_data_text}
```
11
```



## Character Encodings

Character encodings are a set of rules of how to represent a broad range of characters (symbols) in computers. 

We already have a way to represent numbers in binary.  

Using numbers, we can build a general procedure to encode characters as numbers.

We then have a way to represent characters, that we can reduce all the way to binary, that we can use that on computers.

## Example: Character Encoding

As a simple example, let's assign a number to a series of characters we want to be able to represent. 

Every time we see that number, we can evaluate it to replace it with the character it represents. 

### Character Encoding in Code



{:.input_area}
```python
# Set the value we want to encode
character_encoding = 0

# Use conditional to interpret the character as a particular symbol
if character_encoding == 0:
    print('ñ')
elif character_encoding == 1:
    print('é')
elif character_encoding == 2:
    print('¿')
```


{:.output_stream}
```
ñ

```

## Aside: Dictionaries


<div class="alert alert-success">
A dictionary is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
</div>

### Dictionaries as Key-Value Collections



{:.input_area}
```python
# Create a dictionary
dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}
```




{:.input_area}
```python
# Check the contents of the dictionary
print(dictionary)
```


{:.output_stream}
```
{'key_1': 'value_1', 'key_2': 'value_2'}

```



{:.input_area}
```python
# Check the type of the dictionary
type(dictionary)
```





{:.output_data_text}
```
dict
```





{:.input_area}
```python
# Dictionaries also have a length
# length refers to how many pairs there are
len(dictionary)
```





{:.output_data_text}
```
2
```



### Dictionaries: Indexing & Looping



{:.input_area}
```python
# Dictionaries are indexed using their keys
dictionary['key_1']
```





{:.output_data_text}
```
'value_1'
```





{:.input_area}
```python
# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for item in dictionary:
    print('Loop Iteration')
    print('\tKey:\t', item)
    print('\tValue:\t', dictionary[item])
```


{:.output_stream}
```
Loop Iteration
	Key:	 key_1
	Value:	 value_1
Loop Iteration
	Key:	 key_2
	Value:	 value_2

```



{:.input_area}
```python
# another approach that you will find if you Google
for key, val in dictionary.items():
    print('Loop Iteration')
    print('\tKey:\t', key)
    print('\tValue:\t', val)
```


{:.output_stream}
```
Loop Iteration
	Key:	 key_1
	Value:	 value_1
Loop Iteration
	Key:	 key_2
	Value:	 value_2

```

#### Clicker Question #2

Which of the following would create a dictionary of length 3?

- A) `{'Student_1' : 97, 'Student_2'}`
- B) `{'Student_1', 'Student_2', 'Student_3'}`
- C) `['Student_1' : 97, 'Student_2': 88, 'Student_3' : 91]`
- D) `{'Student_1' : 97, 'Student_2': 88, 'Student_3' : 91}`
- E) `('Student_1' : 97, 'Student_2': 88, 'Student_3' : 91)`


#### Clicker Question #3

Fill in the '---' in the code below to return the value stored in the second key.



{:.input_area}
```python
height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict['height_2']
```





{:.output_data_text}
```
68
```



- A) I did it
- B) I think I did it...
- C) I tried and am stuck
- D) No clue where to start...

### Example Dictionaries



{:.input_area}
```python
student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

student_emails
```





{:.output_data_text}
```
{'Betty Jennings': 'bjennings@eniac.org',
 'Ada Lovelace': 'ada@analyticengine.com',
 'Alan Turing': 'aturing@thebomb.gov',
 'Grace Hopper': 'ghopper@navy.usa'}
```





{:.input_area}
```python
completed_coding_lab = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

completed_coding_lab
```





{:.output_data_text}
```
{'A1234': True, 'A5678': False, 'A9123': True}
```





{:.input_area}
```python
mixed_types = {
    True  : [1, 2, 3],  
    False : None
}

mixed_types
```





{:.output_data_text}
```
{True: [1, 2, 3], False: None}
```



#### Clicker Question #4

Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.

- A) I did it
- B) I think I did it...
- C) I tried and am stuck
- D) No clue where to start...



{:.input_area}
```python
# YOUR CODE HERE
car = {'make': 'Hyundai' ,
      'model': 'Sante Fe',
      'year': 2017}

# print(car)
car
```





{:.output_data_text}
```
{'make': 'Hyundai', 'model': 'Sante Fe', 'year': 2017}
```



### Dictionaries are mutable

This means that dictionaries, once created, values *can* be updated.



{:.input_area}
```python
# remember what dictionary we created above
completed_coding_lab
```





{:.output_data_text}
```
{'A1234': True, 'A5678': False, 'A9123': True}
```





{:.input_area}
```python
# change value of specified key
completed_coding_lab['A5678'] = True
completed_coding_lab
```





{:.output_data_text}
```
{'A1234': True, 'A5678': True, 'A9123': True}
```



Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.



{:.input_area}
```python
print(completed_coding_lab)
len(completed_coding_lab)
```


{:.output_stream}
```
{'A1234': True, 'A5678': True, 'A9123': True}

```




{:.output_data_text}
```
3
```





{:.input_area}
```python
## remove key-value pair using del
del completed_coding_lab['A5678']

print(completed_coding_lab)
len(completed_coding_lab)
```


{:.output_stream}
```
{'A1234': True, 'A9123': True}

```




{:.output_data_text}
```
2
```



### Dictionaries and operators

The operators we've discussed previously can be used when working with dictionaries.

To determine if a specified key is present in a dictionary we can use the `in` operator:



{:.input_area}
```python
if 'A1234' in completed_coding_lab:
    print('Yes, that student is in this class')
```


{:.output_stream}
```
Yes, that student is in this class

```

#### Clicker Question #5

What will the value of `result` be after this code has run?



{:.input_area}
```python
dictionary = {'alpha' : [8, 12], 
              'beta'  : [13, 30], 
              'theta' : [4, 8]}

check = 10

for item in dictionary:
    temp = dictionary[item]
    if temp[0] <= check <= temp[1]:
        result = item
        
print(result)
```


{:.output_stream}
```
alpha

```

- A) alpha
- B) [8, 12] 
- C) beta 
- D) theta 
- E) alpha beta

### Additional Dictionary Properties

- Only one value per key. No duplicate keys allowed. 
    - If duplicate keys specified during assignment, the last assignment wins.



{:.input_area}
```python
# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}
```





{:.output_data_text}
```
{'Student': 91}
```



- **keys** must be of an immutable type (string, tuple, integer, float, etc)
- Note: **values** can be of any type



{:.input_area}
```python
# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-31-27b11708f095> in <module>()
      1 # lists are not allowed as key types
      2 # this code will produce an error
----> 3 {['Student'] : 97}

```

{:.output_traceback_line}
```
TypeError: unhashable type: 'list'
```


- Dictionary keys are case sensitive.




{:.input_area}
```python
{'Student' : 97, 'student': 88, 'STUDENT' : 91}
```





{:.output_data_text}
```
{'Student': 97, 'student': 88, 'STUDENT': 91}
```



#### Clicker Question #6

Why does the following code produce an error?



{:.input_area}
```python
student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : ['ada@analyticengine.com'],
    'Ada Lovelace' : 'aturing@thebomb.gov',
    ['Grace Hopper'] : 'ghopper@navy.usa'
}
```


- A) duplicate keys
- B) mutable key specified
- C) keys are case sensitive 
- D) mutable value specified 
- E) ¯\\\_(ツ)\_/¯

## Character Encodings with Dictionaries



{:.input_area}
```python
# Define some character encodings
character_encodings = {
    0 : 'ñ',
    1 : 'é',
}
```




{:.input_area}
```python
# Use character encodings to use symbols we want - example 1
my_sentence = 'no hablo espa' + character_encodings[0] + 'ol'
print(my_sentence)
```


{:.output_stream}
```
no hablo español

```



{:.input_area}
```python
# Use character encodings to use symbols we want - example 2
my_sentence = 'yo hablo ingl' + character_encodings[1] + 's'
print(my_sentence)
```


{:.output_stream}
```
yo hablo inglés

```

## Unicode

<div class="alert alert-success">
Unicode is a system of systematically and consistently representing characters. 
</div>

Every character has a unicode `code point` - an integer that can be used to represent that character. 

If a computer is using unicode, it displays a requested character by following the unicode encodings of which `code point` refers to which character. 

### ORD & CHR

<div class="alert alert-success">
<code>ord</code> returns the unicode code point for a one-character string.
</div>

<div class="alert alert-success"> 
<code>chr</code> returns the character encoding of a code point. 
</div>

### ord & chr examples



{:.input_area}
```python
print(ord('a'))
```


{:.output_stream}
```
97

```



{:.input_area}
```python
print(chr(97))
```


{:.output_stream}
```
a

```

### Inverses

`ord` and `chr` are inverses of one another. 



{:.input_area}
```python
inp = 'b'
out = chr(ord(inp))

assert inp == out
print('Input: \t', inp, '\nOutput: ', out)
```


{:.output_stream}
```
Input: 	 b 
Output:  b

```