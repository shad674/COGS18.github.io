#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - A3 due Monday 11/1 (11:59 PM)
# - E2 next Friday 11/5 - review will be Wed.
# - A4 posted later today; due Fri 11/12 <- this is a change
# - mid-course survey now [available](https://docs.google.com/forms/d/e/1FAIpQLSfZVIyKtegSiD3oRiKT6BwnQbTMFELxXwfhCuyKa1CmMsCk0A/viewform?usp=sf_link) (*optional*; link also on Canvas; due Mon 11/1 for extra credit)

# - Lecture recordings now available in Media Gallery on Canvas (allows for subtitles)
# - E1 regrades have been handled

# **CL5 Feedback**
# 
# - sketching out a task is difficult
# - test out your functions after you write them
# - debugging - how to go about it
# - `to_quarantine()` - default values; many people attempted!

# **In place vs. Not in place**
# 
# - In place directly update the object, *without assignment*

# In[1]:


my_list = ['a', 'b', 'c']
my_list.reverse()
my_list


# - Not in place creates a new object; original object remains unchanged

# In[2]:


car = {'brand': 'BMW', 'model': 'M5', 'year': 2019, 'color': 'Black'}
car.keys()


# In[3]:


# original object remains unchanged
car


# **Q&A**
# 
# Q: Why does my code still run without the return?  
# A: The function can still be defined *and* executed; you just won't be able to store the output from the function without a `return` statement.
# 
# Q: Why does a method belong to something? Why do we use methods?  
# A: Today's lecture will clear this up! It allows you to keep things organized and utilize object-oriented programming.
# 
# Q: If I wanna achieve a goal, what's the best way to check if there exists a direct method or I should write a function.  
# A: Some of this knowledge comes with practice/time. If the thing you want to do is likely only something you'd want to do with that *type* of variable (i.e. capitalize a string), there's likely a method attached to that type. If it's something more general that's common in programming (i.e. sort something), there's likely a generic function for it. If it's something specialized specific to the code you're writing at that time, you'll likely want to define your own function or class (What we're discussing today!)
# 
# Q: I am confused about the relationship between methods and functions. I learned about their difference. So, are they two totally different things or are methods special types of functions?  
# A: Methods are *special* types of functions. All methods are functions, but not all functions are methods. We're going to make this clear today! 
# 
# Q: Will we be asked to manually created functions for methods that we already know on exams? for instance, can we use the sort method or do we have to code our own sort function ever?  
# A: On exams, you can absolutely use any existing functions or methods. You will have to define your own functions on the exam ...but they will not be functions that already exist in Python.

# # Classes
# 
# - objects
# - `class`
#     - attributes
#     - methods
# - instances
#     - `__init__`

# ## Objects
# 
# <div class="alert alert-success">
# Objects are an organization of data (called <b>attributes</b>), with associated code to operate on that data (functions defined on the objects, called <b>methods</b>).
# </div>

# #### Clicker Question #1
# 
# Given what we've discussed in this course so far, if you wanted to store information about a date, how would you do so?
# 
# - A) string
# - B) dictionary
# - C) list
# - D) integers stored in separate variables

# ### Storing Dates (Motivation)

# In[4]:


# A date, stored as a string
date_string = '29/09/1988'
print(date_string)


# In[5]:


# A date, stored as a list of number
date_list = ['29', '09', '1988']
date_list


# In[6]:


# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)


# In[7]:


# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary


# Ways to organize data (variables) and functions together. 

# ### Example Object: Date

# In[8]:


# Import a date object
from datetime import date


# In[9]:


get_ipython().run_line_magic('pinfo', 'date')


# In[10]:


# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)


# In[11]:


# Check what type of thing `my_date` is
type(my_date) 


# ## Accessing Attributes & Methods

# <div class="alert alert-success">
# Attributes and methods are accessed with a <code>.</code>, followed by the attribute/method name on the object. 
# </div>

# ### Date - Attributes
# 
# Attributes look up & return information about the object.

# **attributes** maintain the object's state, simply returning information about the object to you

# In[12]:


# Get the day attribute
my_date.day


# In[13]:


# Get the month attribute
my_date.month


# In[14]:


# Get the year attribute
my_date.year


# ### Date - Methods
# 
# These are _functions_ that *belong* to and operate on the object directly.

# **methods** modify the object's state

# In[15]:


# Method to return what day of the week the date is
my_date.weekday()


# In[16]:


# Reminder: check documentation with '?'
get_ipython().run_line_magic('pinfo', 'date.weekday')


# It's also possible to carry out operations on multiple date objects.

# In[17]:


# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)


# In[18]:


# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365,"years") #in years


# ### Listing Attributes & Methods : `dir`

# In[19]:


# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.


# In[20]:


## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)


# #### Clicker Question #2
# 
# Given the code below:

# In[21]:


my_date = date(year = 1050, month = 12, day = 12)


# Which is the best description:
# - A) `my_date` is an object, with methods that store data, and attributes that store procedures
# - B) `my_date` is variable, and can be used with functions
# - C) `my_date` is an attribute, with methods attached to it
# - D) `my_date` is a method, and also has attributes
# - E) `my_date` is an object, with attributes that store data, and methods that store procedures

# #### Clicker Question #3
# 
# For an object `lets` with a method `do_something`, how would you execute that method?
# 
# - A) `do_something(lets)`
# - B) `lets.do_something`
# - C) `lets.do_something()`
# - D) `lets.do.something()`
# - E) ¯\\\_(ツ)\_/¯

# #### Clicker Question #4
# 
# For an object `lets` with an attribute `name`, how would you return the information stored in `name` for the object `lets`?
# 
# - A) `name(lets)`
# - B) `lets.name`
# - C) `lets.name()`
# - D) lets.get.name()
# - E) ¯\\\_(ツ)\_/¯

# **Course Announcements (Mon 11/1)**
# 
# - A3 due tonight (11:59 PM)
# - CL6 due Wed 
# - E2 this Friday 11/5
# - A4 is now available (you can already do Part I; due 11/12)
# - mid-course survey now [available](https://docs.google.com/forms/d/e/1FAIpQLSfZVIyKtegSiD3oRiKT6BwnQbTMFELxXwfhCuyKa1CmMsCk0A/viewform?usp=sf_link) (*optional*; link also on Canvas; due tonight for extra credit)
# - Brian OH now **Friday 2-3 PM** (CSB 114; syllabus has been updated)

# **Q&A**
# 
# Q: What will be the length of the exam?  
# A: I haven't written it yet, but similar to E1.
# 
# Q: Would we only use the import command with objects or are there other instances?  
# A: There are other things we can import. We'll discuss this after the second midterm!
# 
# Q: So does a default value just mean defining the value within the parentheses of a function?  
# A: Yes - that's how you define one. Then, when you *execute* that function, the default value will be used without you having to pass a value to that parameter.
# 
# Q: Where I can get more resources to study?  
# A: In addition to class notes, coding labs, assignments, and prior exams, there is also the coures [textbook](https://shanellis.github.io/pythonbook/content/intro.html), which has additional practice problems (and answer keys). There is also [pythontutor](https://pythontutor.com/), which allows you to visualize your code. The Internet also has additional practice problems, youtubue has tutorial videos, etc.  
# 
# Q: Why are there parentheses after methods even if we don't write things inside? For example: some_list.lower() or some_list.upper().  
# A: The parentheses indicate that code should be executed. There will always be parentheses after functions and methods. *Sometimes* there are parameters we want to control. We would then specify those within the parentheses. This is true for methods and functions.
# 
# Q: Is there a database or website we can refer to when encountering errors?  
# A: There's not one site. Understanding what error messages mean is a skill practiced over time. The debugging lecture explains each of them. But, googling your error message can sometimes be helpful if you're unsure of what it means.
# 
# Q: How do we know when to import an object?  
# A: We'll disuss this in a coming lecture in more detail, but when the functionality is not yet available in your current namespace.
# 
# Q: is there a way to check each step a function. Normally for a loop or conditional I can write a print statement and check if it works, but it seems I can't check to see if a part of a function works without running the whole thing.  
# A: You can define the function and comment out parts you aren't ready to test yet. Then, you would execute the function and see if the output is what you expected. `print()` statements can still be helpful here. Then, you can uncomment/finish writing the function, re-define it, and retest it.
# 
# Q: What is the main difference between the functions and classes?  
# A: Functions do not store attributes. They are just functions. Classes store attributes and methods, which are attached to the object type.
# 
# Q: How to better study and prepare for the upcoming midterm? What topics to focus on?  
# A: We'll discuss this in the review, but the midterm will focus on what we've covered since the first midterm. It will be dictionaries, a lot of functions, and some classes.
# 

# **Global vs. local variables**
# 
# - **global** - a variable defined in your notebook
# - **local** - a variable defined within a function

# 1. These two namespaces cannot "see" one another
# 2. Functions only have access to the variables defined within them *or* those passed in as parameters

# In[22]:


## common error we've seen
output_val = 0

def sum_values(input_list):
    for value in input_list:
        try: 
            output_val += value
        except:
            continue
    
    return output_val


# In[23]:


# this code will error
sum_values(['a', 1, 10])


# #### Clicker Question (Warm-up)
# 
# Would you rather...
# 
# - A) have **24h for the exam** and **no class or office hours Friday** (exam would be released before class Fri; due Sat at 8AM)
# - B) have **~60h for the exam** but **have class and office hours Friday** (exam would be released Fri afternoon; due Mon before class at 8AM)

# ### Objects Summary
# 
# - Objects allow for data (attributes) and functions (methods) to be organized together
#     - methods operate on the object type (modify state)
#     - attributes store and return information (data) about the object (maintain state)
# - `dir()` returns methods & attributes for an object
# - Syntax:
#     - `obj.method()`
#     - `obj.attribute`
# - `date` and `datetime` are two types of objects in Python

# ## Classes

# <div class="alert alert-success">
# <b>Classes</b> define objects. The <code>class</code> keyword opens a code block for instructions on how to create objects of a particular type.
# </div>

# Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.

# ## Example Class: Dog

# In[1]:


# Define a class with `class`. 
# By convention, class definitions use CapWords (Pascal)
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self, n_times=2):
        return self.sound * n_times


# In[3]:


an_instance = Dog()
an_instance.speak()


# A reminder:
# - **attributes** maintain the object's state; they lookup information about an object
# - **methods** alter the object's state; they run a function on an object

# **`class`** notes:
# 
# - classes tend to use **CapWords** convention (Pascal Case)
#     - instead of snake_case (functions and variable names)
# - `()` after `Dog` indicate that this is callable
#     - like functions, Classes must be executed before they take effect
# - can define **attributes** & **methods** within `class`
# - `self` is a special parameter for use by an object
#     - refers to the thing (object) itself
# - like functions, a new namespace is created within a Class
# 

# In[25]:


# Initialize a dog object
george = Dog()


# In[26]:


# george, has 'sound' attribute(s) from Dog()
george.sound


# In[27]:


# george, has 'Dog' method(s)
# remember we used `self`
george.speak()


# #### Clicker Question #5
# 
# Which of the following statements is true about the example we've been using? 

# In[28]:


class Dog():
    
    sound = 'Woof'
    
    def speak(self, n_times=2):
        return self.sound * n_times


# - A) `Dog` is a Class, `sound` is an attribute, and `speak` is a method. 
# - B) `Dog` is a function, `sound` is an attribute, and `speak` is a method. 
# - C) `Dog` is a Class, `sound` is a method, and `speak` is an attribute. 
# - D) `Dog` is a function, `sound` is an method, and `speak` is an attribute. 

# ### Using our Dog Objects

# In[29]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# In[30]:


# take a look at this
pack_of_dogs


# In[31]:


type(pack_of_dogs)


# In[32]:


# take a look at this
type(pack_of_dogs[0])


# In[33]:


for dog in pack_of_dogs:
    print(dog.speak())


# ## Instances & self

# <div class="alert alert-success">
# An <b>instance</b> is particular instantiation of a class object. <code>self</code> refers to the current instance. 
# </div>

# In[34]:


# Initialize a dog object
george = Dog()


# From our example above:
# 
# - Dog is the Class we created
# - `george` was an _instance_ of that class
# - self just refers to whatever the _current_ instance is

# #### Clicker Question #6
# 
# How many instances of `Dog()` are created below and how many times does the `speak()` method execute?

# In[35]:


pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

counter = 1

for doggie in pack_of_dogs:
    if counter <= 2:
        print(doggie.speak())
        counter += 1
    else:
        break


# - A) 2 instances, 2 method executions
# - B) 2 instances, 4 method executions
# - C) 4 instances, 2 method executions
# - D) 4 instances, 4 method executions
# - E) ¯\\\_(ツ)\_/¯

# ## Instance Attributes
# 
# An instance attribute specific to the instance we're on. This allows different instances of the same class to be unique (have different values stored in attributes and use those in methods).

# In[36]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# This creates four different `Dog` type objects and stores them in a list. But, up until now...every `Dog` was pretty much the same.

# <div class="alert alert-success">
# Instance attributes are attributes that we can make be different for each instance of a class. <code>__init__</code> is a special method used to define instance attributes. 
# </div>

# ## Example Class: Dog Revisited
# 
# - Two trailing underscores (a `dunder`, or double underscore) is used to indicate something Python recognizes and knows what to do every time it sees it.
# - Here, we use `__init__` to execute the code within it every time you initialize an object.

# In[37]:


class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# In[38]:


# Initialize a dog
# what goes in the parentheses is defined in the __init__
gary = Dog(name = 'Gary') 


# In[39]:


# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute


# In[40]:


# Check gary's methods
gary.speak()


# #### Clicker Question #7
# 
# Edit the code we've been using for the Class `Dog` to include information about the breed of the Class Dog in `NewDog`?

# In[4]:


# EDIT CODE HERE
class NewDog():
    
    sound = 'Woof'
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self, n_times=2):
        return self.sound * n_times


# In[ ]:


my_dog = NewDog('Lexi', 'Italian Greyhound')
my_dog.breed
my_dog.speak(6)


# In[42]:


## We'll execute here
lexi = NewDog(name='Lexi', breed='Italian Greyhound')
print(lexi.sound, lexi.name, lexi.breed)
lexi.speak(n_times=4)


# - A) I did it!
# - B) I think I did it!
# - C) So lost. -_-

# ## Class example: Cat

# In[43]:


cat_object = Cat(name='Shannon')
cat_object.name


# In[44]:


# Define a class 'Cat'
class Cat():
    
    sound = "Meow"
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# ## Instances Examples

# In[45]:


# Define some instances of our objects
pets = [Cat('Jaspurr'), Dog('Barkley'), 
        Cat('Picatso'), Dog('Ruffius')]


# In[46]:


for pet in pets:
    print(pet.name, ' says:')
    print(pet.speak())


# #### Clicker Question #8
# 
# What will the following code snippet print out?

# In[47]:


class MyClass():
    
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score
    
    def check_score(self):        
        if self.score <= 65:
            return self.email
        else:
            return None


# In[48]:


student = MyClass('Rob', 'rob@python.com', 62)
student.check_score()


# - A) True
# - B) 'Rob'
# - C) False 
# - D) 'rob@python.com'
# - E) None

# **Course Announcements** (Wed 11/3)
# 
# **Due Dates**
# - CL6 due tonight 
# - E2 released this Friday (~5PM); due **Mon at 8AM**
# 
# **Notes**
# - CL5 and mid-course survey scores posted
# - Posts with code on campuswire *must* be private to TAs & Instructors
#     - going forward; points will be deducted and/or student will be submitted to AIO
#     - if you answer a post with code in it to help a fellow student, you will NOT be in trouble

# **Mid-course Survey Summary**
# 
# - N=270 (out of possible 378; 71% response rate)
# - Getting Help: 
#     - Coding Labs: have to wait too long; encouraging you to ask the person next to you before staff 
#     - Campuswire: if you feel you're not getting help, be sure question is marked as "Unresolved"
#     - Being told to Google: this is part of the process! (We've seen progress here.)

# - Office hours: more on Th/Fri *and* more zoom
#     - Brian moved his office hours from Mon to Fri
#     - Prof now holding additional 10min slots on Thurs 3-4 by appt only
#         - see link to sign up on Canvas
#         - please come ready to ask questions
#         - please cancel if you can't make it

# - Harder/more examples please
#     - be sure to check answer keys after coding labs
#     - have already started implementing this in lectures
#     - [additional practice problems](https://shanellis.github.io/pythonbook/content/intro.html) (With answer keys)

# **E2 Notes**
# - will be released Fri @ ~5PM; will be **due Mon at 8AM**
#     - there WILL be lecture *and* office hours on Friday
# - 8 Questions: 
#     - Part I: Methods and Debugging (3Qs; 3.5 pts)
#     - Part II: Functions (3 Qs; 4.4 pts)
#     - Part III: Classes (2 Qs; 4.5 pts)
# - Practice E2 is *way* longer than the real E2
#     - Answer key will be posted on Thursday
#     - Revew/Practice notebooks also available on course website and in Exam-Prep folder on datahub
# - Review Friday: bring questions!

# **Q&A**
# 
# Q: Can you just use any word other than self while creating the method? Also why the dunder  
# A: Theoretically, yes, you could use any word other than `self`. In practice, we're going to use `self`, as the python community all kind of "agrees" that this is what we'll do. And the dunder around `__init__` indicates that this is a special "magic" method...with `__init__` specifically defining instance attributes.
# 
# Q: I find the challenge in CL6 is particularly difficult, so I just wonder if we are going to have similar questions in E2?  
# A: You could have one question on E2 similar to the challenge on CL6...but it would be the last question on the exam and the most difficult overall. It would also have partial credit attached, so even if you didn't figure it out completely, you could earn partial points.
# 
# Q: I understood that attributes are variables defined inside a class and an object is defined by a class. Is an object a special type of variable that can contain multiple variables inside it?   
# A: That's one aspect of a new object type (meaning a new `class` of object)! It can also have methods defined within it. Making it "more" than just a way to store multiple variables.
# 
# Q: Is there a specific time that exam 2 will be released on Friday afternoon?  
# A: After Brian's OH for sure; likely around 5PM. A campuswire post will be sent when posted.
# 
# Q: what happens if i answer this participation quiz two days after actual class time? Does it still count for participation?  
# A: If you respond while the lecture is still included in the drop-down menu, you'll receive credit.
# 
# Q: within a class, can you only define an instance attribute (or write def __init__) once?  
# A: Yes, you only want to define it once; however, you can define as many intributes as you want within that `__init__` 
# 
# Q: Why is the object "date" from the date example in last Friday's lecture all lowercase, rather than uppercase, like "Date?"  
# A: Great question! While CapWords is convention, the developers of the `date` type object did not follow convention. I think `Date` would be better!
# 
# Q: Where do we commonly use global namespaces? Do we use local namespaces in other forms of coding in addition to functions? Also, for instances do we ALWAYS use self as the first parameter?  
# A: You use the global namespace any time you define a variable/function/class in a jupyter notebook. You create a separate local name space any time you define a new function or class. And yup! `self` will always be first in instance attribute definition.

# ### Example: `ProfCourses()`
# 
# Let's put a lot of these concepts together in a more complicated example...
# 
# What if we wanted some object type that would allow us to keep track of Professor Ellis' Courses? Well...we'd want this to work for any Professor, so we'll call it `ProfCourses`.
# 
# We would likely want an object type and then helpful methods that allow us to add a class to the course inventory and to compare between courses.

# In[53]:


class ProfCourses():
    
    # create three instance attributes
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof


# In[54]:


ellis_courses = ProfCourses('Ellis')
print(ellis_courses.n_classes)
print(ellis_courses.prof)


# **`add_class()` method**

# In[55]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    # add method that will add classes as a dictionary
    # to our attribute (classes)...which is a list
    def add_class(self, course_name, quarter, n_students):
        
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        # increase value store in n_classes
        # by 1 any time a class is added
        self.n_classes += 1


# In[58]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')
print(ellis_courses.n_classes)

# add a class
ellis_courses.add_class('COGS18', 'fa20', 363)
ellis_courses.add_class('new class', 'fa20', 100)

# see output
print(ellis_courses.n_classes)
ellis_courses.classes


# **`compare()` method**

# In[1]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    def add_class(self, course_name, quarter, n_students):
        
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        self.n_classes += 1
        
     
    # add method to compare values in classes
    def compare(self, attribute, direction='most'):
    
        fewest = self.classes[0]
        most = self.classes[0] 
        
        for my_class in self.classes:
            if my_class[attribute] <= fewest[attribute]:
                fewest = my_class
            elif my_class[attribute] >= most[attribute]:
                most = my_class
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output


# In[3]:


ellis_courses = ProfCourses('Ellis')

ellis_courses.add_class('a','fa21',200)


# In[60]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_class('COGS108', 'sp21', 311)
ellis_courses.add_class('COGS18', 'sp21', 430)
ellis_courses.add_class('COGS108', 'wi21', 431)
ellis_courses.add_class('COGS18', 'wi21', 99)
ellis_courses.add_class('COGS18', 'fa20', 363)
ellis_courses.add_class('COGS108', 'fa20', 447)
ellis_courses.add_class('COGS18', 'su20', 88)
ellis_courses.add_class('COGS108', 'sp20', 469)
ellis_courses.add_class('COGS108', 'sp19', 825)

# see the courses
print(ellis_courses.n_classes)
ellis_courses.classes


# In[65]:


# make comparison among all courses
# returns the class with the most students
ellis_courses.compare('n_students')


# In[64]:


# return the class with the fewest students
ellis_courses.compare('n_students', 'fewest')


# **extending the functionality of the `compare()` method**

# In[66]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    def add_class(self, course_name, quarter, 
                  n_students, n_exams, n_assignments):
        
        # add in additional key-value pairs
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students,
                             'n_exams' : n_exams,
                             'n_assignments' : n_assignments})
        self.n_classes += 1
        
     
    def compare(self, attribute, direction='most'):
    
        fewest = self.classes[0]
        most = self.classes[0] 
        
        for my_class in self.classes:
            if my_class[attribute] <= fewest[attribute]:
                fewest = my_class
            elif my_class[attribute] >= most[attribute]:
                most = my_class
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output


# In[67]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_class('COGS108', 'sp21', 311, 0, 4)
ellis_courses.add_class('COGS18', 'sp21', 430, 2, 5)
ellis_courses.add_class('COGS108', 'wi21', 431, 0, 4)
ellis_courses.add_class('COGS18', 'wi21', 99, 2, 5)
ellis_courses.add_class('COGS18', 'fa20', 363, 2, 5)
ellis_courses.add_class('COGS108', 'fa20', 447, 0, 6)
ellis_courses.add_class('COGS18', 'su20', 88, 3, 5)
ellis_courses.add_class('COGS108', 'sp20', 469, 0, 6)
ellis_courses.add_class('COGS108', 'sp19', 825, 0, 5)
ellis_courses.add_class('COGS18', 'fa19', 301, 2, 4)

# see the courses
print(ellis_courses.n_classes)


# In[68]:


# return the class with the most exams
ellis_courses.compare('n_exams', 'most')


# In[69]:


# return the class with the fewest assignments
ellis_courses.compare('n_assignments', 'fewest')


# **Improving & updating this code**
# - account for ties in `compare()`
# - edit code in `compare()` to make the `for` loop and following conditional more intuitive
# - add a method to put dictionary in time order
# - etc.

# ### Classes Review
# 
# - `class` creates a new class type
#     - names tend to use CapWords case
#     - can have attributes (including instance attributes) and methods
#         - `obj.attribute` accesses data stored in attribute
#         - `obj.method()` carries out code defined within method 
# 

# - instance attributes defined with `__init__`
#     - `__init__` is a reserved method in Python
#     - This "binds the attributes with the given arguments"
#     - `self` refers to current instance

# - to create an object (instance) of a specified class type (`ClassType`):
#     - `object_name = ClassType(input1, input2)`
#     - `self` is not given an input when creating an object of a specified class

# ## Everything in Python is an Object!

# ### Data variables are objects

# In[70]:


print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))


# ### Functions are objects

# In[71]:


print(isinstance(sum, object))
print(isinstance(max, object))


# In[72]:


# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)


# ### Class definitions & instances are objects

# In[76]:


class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()
print(isinstance(MyClass, object))
print(isinstance(my_instance, object))


# ## Object-Oriented Programming

# <div class="alert alert-success">
# <b>Object-oriented programming (OOP)</b> is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
# </div>