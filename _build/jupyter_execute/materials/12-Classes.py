#!/usr/bin/env python
# coding: utf-8

# **Course Announcements (Wed 2/8)**
# 
# Due Dates:
# - **CL6** due tonight (11:59 PM)
# - **A3** due tomorrow (Thurs 2/10; 11:59 PM)
# 
# Notes:
# - mid-course EC posted
# - reminder about interactions with staff
# - Code Style guide has been posted
# - **A4** released this afternoon (due Mon 2/28)
# - **E1**
#     - regrades submitted so far have been addressed
#     - **E1 Q10**: if the only thing wrong was a typo in your string, you should have had autograder credit returned and been deducted only 0.05 points for typo; submit a regrade request if not the case
# - **E2** plan
#     - Review: next Wed in class (2/16)
#     - Exam released: next Thursday (2/17; 3 PM)
#     - No lecture next Friday
#     - Exam due: Sunday 2/20 (11:59 PM)

# **Mid-course Survey Summary** 
# - N=283
# - Approximate hours spent:
#     - A1: 2
#     - A2: 3
#     - E1 Studying: 3
#     - E1 Completing: 2.5
# - A2/E1 more difficult than A1
# - Coding labs maybe a bit too long
# - if you asked a question, should have gotten a response via Campuswire DM/email

# In[29]:


# question asked at the end of class Wednesday
# "Could you please explain what does random.choice function mean in A3 Q16?"
import random

random.choice([1, 2, 3, 4])


# **Q&A**
# 
# Q: In class we saw that using car['model'] and car.get('model') produced the same result for a dictionary. If they are effectively the same, what would be the reason to use the get method over simply using square braces?  
# A: While python *tries* to prioritize having *one* way to do things, it sometimes falls short. This is one case where there are two equivalent ways. As fair as I'm concerned, pick one and stick to it for consistency...whichever is more readable for you.
# 
# Q: I am still not sure about where the return statement should be in a loop. Can you go over that again?  
# A: The return statement should be placed where/when you want the output to return. If you want it to return the first time through your loop (typically you don't want this), the `return` statement would be indented within the loop. If you want it to `return` once the loop terminates, it would be after the loop and at the same level of indentation as the loop. This is a great question for office hours if still confused.
# 
# Q: I tried the same example and I defined the list of vowels inside the function yet it still said there was an error with the list of vowels being defined before assignment, but when I just rewrote my code it was fine, so does python get overwhelmed or need to restart sometimes?  
# A: No, you likely hadn't re-executed the cell after moving the list inside the function? 
# 
# Q: Will the codes changed in class by instructor be updated in our lecture notes? It seems like it doesn't, but I'd like to have it.   
# A: The updated notes from the previous class are posted to the course website before the next day's class.
# 
# Q: Can I append 2 lists together somehow? Do we need to know algorithms for the upcoming exam?  
# A: Yes - if you want to take two lists and turn them into one list, you can use the `+` operator. And, the algorithms notes do not introduce any new topics, but help solidify understanding of functions + loops, so it may be good to review, but there is nothing new topic-wise in that lecture.

# **Course Announcements (Fri 2/11)**
# 
# Due Dates:
# - **CL6** due (again) next Wednesday (11:59 PM)
# - **E2** due next Sunday (2/20; released 2/17)
# - **A4** due Mon 2/28
# 
# Note: 
# - E2 Practice Exam released on datahub
# - CL7-9 due dates pushed back by a week (Canvas and Syllabus have been udpated)

# **Q&A**
# 
# Q: How do I put a conditional, loop, or try/except in a method?   
# A: The same way you would inside a function. Only difference is if you want to refer back to an attribute from the class you would need `self.` before the name of the attribute.
# 
# Q: I think I'm still confused about what purpose creating our own classes/objects have. Why wouldn't we just create those functions (like the speak function/method in the Dog class we talked about today in lecture) within our code without having to define a new class altogether? Is it only because it makes some operations easier later in our code?  
# A: Great question. A few things: 1) It allows you to organize things that work together together. 2) It allows you to avoid repeating yourself. Specifically, imagine a class with four methods, all of which need to reference the attribute `this_thing`. Rather than defining `this_thing` separately in four different functions, you'd create teh attribute once (in the class) and then reference in each method as needed. 3) ...and we won't get to this in this intro class is classes allow for inheritance, meaning they allow for one class to "inherit" the attributes from another class. This allows you to design code that has a hierachical structure...that functions do not as easily allow for.
# 
# Q: Can you go over the classes notes again and give us a challenging questions, please?   
# A: Yup - we'll be doing this today (and likely Monday).
# 
# Q: Why is it okay if sometime there is an empty parentheses after the defined function?   
# A: This indicates that you want to execute the method with default parameters or that there is no input to the function/method. If you wanted to chance the value for any parameters, you'd need to specify it within the parentheses.
# 
# Q: When do we place values inside the parentheses of methods? I've noticed that with certain methods, we simply indicate the object in the beginning and then specify the method type after the period (my_list.reverse()) but sometimes we place values inside the parentheses. Just not sure when which is done.   
# A: See above for similar question...but stuff goes in there when you want to pass in values to the parameters of the method.
# 
# Q: Why is checking the documentation for something useful?  
# A: So you know what it does/how to use it. Googling also useful for this.
# 
# Q: Whats the difference between method and class?  
# A: A class defines a new object type. These objects can have methods attached to them. So, by definition, methods are defined *within* classes.
# 
# Q: I am really confused on using 'counter' in functions. I am not sure what it means when it is 0 and how it works in the functions?  
# A: `counter` is a variable that allows you to "keep track" of how many times a loop has iterated. For example, if `counter` is zero before the loop and inside the loop you have `c=ounter = counter + 1`, after that loop runs the first iteration counter will store the value 1 (`0 + 1`) ...indicating that that line of code has executed. The next time through counter would store 2, and so on. Happy to discuss/explain this in office hours!
# 
# Q: Do you make classes or do classes exist and you use them?  
# A: Both! For example, we `import`ed the `date` object type. That class has already been defined and we used it...but we can also define our own and use them.
# 
# Q: Is object and class kind of the same thing?  
# A: Yup - we define a new `class` which allows us to create a new object of that class type.
# 
# Q: How do you concatenate after an integer? '\n' after an integer ?   
# A: If you want to concatenate...you probably need to typecast the integer to a string using `str()` and then concatenate from there...but seeing your specific use case may be helpful. Feel free to ask on campuswire with more specifics!

# **Black History Month**: Foundational Fridays
# - 1960s: [Katherine G. Johnson](https://www.nytimes.com/2020/02/24/science/katherine-johnson-dead.html) and [Dorothy Vaughan](https://scientificwomen.net/women/vaughan-dorothy-103) (NASA) 
#     - helped calculate flight path to the moon 
#     - "rigorously educated, supremely capable yet largely unheralded"
#     - "teaching herself and her staff the programming language of FORTRAN"
#     - each is featured in "Hidden Figures"
# - 1969: [Clarence "Skip" Ellis](https://medium.com/@mayborn_unt/clarence-skip-ellis-the-first-black-ph-d-in-computer-science-6ccae49b148) - first black man to earn his PhD in CS from UIUC (note: ACM was founded in 1947)
#     - worked at Bell Laboratories, IBM, and Xerox
#     - worked on the team developing the world’s first personal computer (PC) and its related interfaces and software
#     - 1992 - Professor at University of Colorado Boulder 
#     - In a 2003 survey, he was the *only* full black prof at the 50 largest US research universities (one of four black profs in total...among 1,332 faculty)

# **Course Announcements (Mon 2/14)**
# 
# Due Dates:
# - **CL6** due (again) Wednesday (11:59 PM) - *NO* new CL this week
# - **E2** due Sunday (2/20; 11:59 PM); released Thursday 2/17 3PM
# - **A4** due Mon 2/28
# 
# Notes:
# - No lecture this Friday (exam) OR next Monday (holiday)

# **Q&A** (Mon 2/14)
# 
# Q: I was wondering if we can include 'if' and 'else' inside a class?   
# A: Absolutely - this would typically happen within a method inside a class.
# 
# Q: If we already spent over an hour on the coding lab and finished most of the questions, can we just turn that in for this week?  
# A: Yup. Now, of course understanding the material throughout the lab is important for the exam, so I encourage you to be sure you've looked over it again as your understanding increases. And, if you do that and edit your code prior to Wednesday's deadline, mine as well submit the most recent/completed lab.
#  
# Q: Also, what's the use of doing self.(insert parameter) = parameter?  
# A: This allows you to define an instance attribute with the input from the user, specifying the value for the attribute on creation of an instance of the ojbect.
# 
# Q: Do we only use self.*input parameter* when using the __init__ and then in other methods we would just use the variable names without the self. ?  
# A: When defining attributes, yes. Note that when referring to an attribute within a method `self.` will always be before the attribute name (regardless of whether it is a class or instance attribute).
# 
# Q: Can there be a method within a method?  
# A: There *could* but that's not good code design typically.
# 
# Q: Where are class objects stored overall?   
# A: When defined in a notebook, they are stored in your namespace (same place as variables and functions are stored)
# 
# Q: When a word is in blue in Python, does that just mean it's a name of some specific procedure (e.g., function names) or data type (e.g., class names)?  
# A: Yup. 
# 
# Q: When would we need a return statement for class methods?  
# A: When you want the method to return that output/be able to store it in a variable.
# 
# Q: why do we need to put self in front of the parameters? what does that do?  
# A: This refers to the attributes for *that particular instance* of the object. These values could differ from one object to another (see example in class today and how the attribute's value changes as we use the object).
# 
# Q: if we did not declare a parameter inside '__init__' and instead declared the parameter in another method inside the class, can we use call the parameter in a 3rd method?  
# A: Nope. Each method has its own namespace. If you want to use the attribute/parameter in more than one method, best to define it as either a class or instance attribute.
# 
# Q: I'm a little confused on the purpose of __init__, since I thought we always had to use it, but some of the examples didn't. Is it just there when we want to have attributes that will be different for each instance (like the dog's breeds)? But doesn't need to be used if all the instances will be the exact same?  
# A: Yup - neither class nor instance attributes are *required*. Class attributes are for things that will be consistent/the same for every object of that type (sound of a dog). Instance attributes are for things that could take different values for each insetance of that object type (breed/name of a dog). Neither is required; both are allowed within a class.
# 
# Q: When referring to instances, is self always the parameter we need to use?  
# A: Yes - we will always use `self`. (For a more complete answer, *theoretically* you could use a different word, but the Python community has settled on `self`, so we'll use `self` and you'll see `self` if you look up others' code on the Internet.)
# 
# Q: is the purpose of instance attributes being that they can be edited whereas class attributes can not?  
# A: That's one way to think of them. The other difference is that instance attributes' values can/will differ for each instance of the object created...whereas class attributes will not. 
# 
# Q: Up to which question in A4 will cover the material in E2?
# A: Theoretically, all of it is fair game on A4...but the questions on the exam will not be as involved/difficult as the CarInventory or Bots questions from A4. 
# 
# Q: For the final project, do we use the same code and build on it from A3 or do we start a completely new code?  
# A: We'll discuss this in a week or so. Either is allowed...but you'll be required to write *additional* code on top of any code used from the assignment.
# 
# Q: What’s the different between functions and classes  
# A: Functions stand on their own, take input, carry out some operators and return output. Classes on the other hand can have functions defined *within them* (methods), but they *also* allow you to define attributes that are part of the class. This allows you to organize your code better.
# 
# Q: Also, could you give an example of how to use try and except inside a class since I am still confused about that.   
# A: See below...in this example, I've decided to add a `lbs` instance attribute and use this within the speak method. If it's a larger dog (>50 pounds), the dog will bark more times (`n_times * 2`). If it's smaller, it will only bark `n_times`. However...if someone tried to store a non-numeric value...that would cause the `try` to error...if we didn't have the `except`. Here, instead of getting an error, we `print` out a message to the user.

# In[94]:


class Dog():
    
    sound = 'Woof'
    
    def __init__(self, name, lbs):
        self.name = name
        self.lbs = lbs
    
    def speak(self, n_times=2):
        try: 
            if int(self.lbs) > 50:
                return self.sound * n_times * 2
            elif int(self.lbs) <= 50:
                return self.sound * n_times
        except:
            print('Expecting lbs to be numeric. Please edit the lbs attribute.')


# In[91]:


# small dog
lexi = Dog('Lexi', 14)
lexi.speak()


# In[92]:


# big dog
greg = Dog('Greg', 65)
greg.speak()


# In[93]:


# would cause error if we didn't have try/except
sparky = Dog('Sparky', 'small')
sparky.speak()


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

# In[1]:


# A date, stored as a string
date_string = '29/09/1988'
print(date_string)


# In[2]:


# A date, stored as a list of number
date_list = ['29', '09', '1988']
date_list


# In[3]:


# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)


# In[4]:


# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary


# Ways to organize data (variables) and functions together. 

# ### Example Object: Date

# In[5]:


# Import a date object
from datetime import date


# In[6]:


get_ipython().run_line_magic('pinfo', 'date')


# In[7]:


# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)


# In[8]:


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

# In[9]:


# Get the day attribute
my_date.day


# In[10]:


# Get the month attribute
my_date.month


# In[11]:


# Get the year attribute
my_date.year


# ### Date - Methods
# 
# These are _functions_ that *belong* to and operate on the object directly.

# **methods** modify the object's state

# In[12]:


# Method to return what day of the week the date is
my_date.weekday()


# In[13]:


# Reminder: check documentation with '?'
get_ipython().run_line_magic('pinfo', 'date.weekday')


# It's also possible to carry out operations on multiple date objects.

# In[14]:


# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)


# In[15]:


# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365, "years") #in years


# ### Listing Attributes & Methods : `dir`

# In[ ]:


# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.


# In[16]:


## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)


# #### Clicker Question #2
# 
# Given the code below:

# In[ ]:


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

# In[17]:


# Define a class with `class`. 
# By convention, class definitions use CapWords (Pascal)
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self, n_times=2):
        return self.sound * n_times


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

# In[18]:


# Initialize a dog object
george = Dog()


# In[19]:


# george, has 'sound' attribute(s) from Dog()
george.sound


# In[20]:


# george, has 'Dog' method(s)
# remember we used `self`
george.speak()


# #### Clicker Question #5
# 
# Which of the following statements is true about the example we've been using? 

# In[39]:


# edited clicker question due to student question at ~23min
class Dog():
    
    sound = 'Woof'
    
    def speak(self, separator, n_times=2):
        return (self.sound + separator) * n_times


# In[42]:


gary = Dog()
gary.speak(separator='-')


# - A) `Dog` is a Class, `sound` is an attribute, and `speak` is a method. 
# - B) `Dog` is a function, `sound` is an attribute, and `speak` is a method. 
# - C) `Dog` is a Class, `sound` is a method, and `speak` is an attribute. 
# - D) `Dog` is a function, `sound` is an method, and `speak` is an attribute. 

# ### Using our Dog Objects

# In[21]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# In[22]:


# take a look at this
pack_of_dogs


# In[23]:


# take a look at this
type(pack_of_dogs[0])


# In[33]:


for dog in pack_of_dogs:
    print(dog.speak(n_times=4))


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

# In[37]:


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

# In[ ]:


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

# In[43]:


class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# In[44]:


# this will error now; no name provided
george = Dog()


# In[45]:


# Initialize a dog
# what goes in the parentheses is defined in the __init__
gary = Dog(name='Gary') 


# In[46]:


# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute


# In[47]:


# Check gary's methods
gary.speak()


# #### Clicker Question #7
# 
# Edit the code we've been using for the Class `Dog` to include information about the breed of the Class Dog in `NewDog`?

# In[48]:


# EDIT CODE HERE
class NewDog():
    
    sound = 'Woof'
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self, n_times=2):
        return self.sound * n_times


# In[53]:


## We'll execute here
lexi = NewDog('Lexi', 'Italian Greyhound')
lexi.breed


# - A) I did it!
# - B) I think I did it!
# - C) So lost. -_-

# ## Class example: Cat

# In[54]:


# Define a class 'Cat'
class Cat():
    
    sound = "Meow"
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# ## Instances Examples

# In[55]:


# Define some instances of our objects
pets = [Cat('Jaspurr'), Dog('Barkley'), 
        Cat('Picatso'), Dog('Ruffius')]


# In[56]:


for pet in pets:
    print(pet.name, ' says:')
    print(pet.speak())


# #### Clicker Question #8
# 
# What will the following code snippet print out?

# In[59]:


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


# In[61]:


student = MyClass(name='Rob', email='rob@python.com', score=62)
student.check_score()


# - A) True
# - B) 'Rob'
# - C) False 
# - D) 'rob@python.com'
# - E) None

# ## Code Style: Classes
# 
# - CapWords for class names
# - one blank line between methods/functions

# **Good Code Style**

# In[1]:


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


# **Code Style to Avoid**

# In[ ]:


class my_class(): # uses snake case for name
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score   # no blank lines between methods  
    def check_score(self):        
        if self.score <= 65:
            return self.email
        else:
            return None


# ### Example: `ProfCourses()`
# 
# Let's put a lot of these concepts together in a more complicated example...
# 
# What if we wanted some object type that would allow us to keep track of Professor Ellis' Courses? Well...we'd want this to work for any Professor, so we'll call it `ProfCourses`.
# 
# We would likely want an object type and then helpful methods that allow us to add a class to the course inventory and to compare between courses.

# In[62]:


class ProfCourses():
    
    # create three instance attributes
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof


# In[63]:


ellis_courses = ProfCourses('Ellis')
print(ellis_courses.n_courses)
print(ellis_courses.prof)


# **`add_class()` method**

# In[96]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof
    
    # add method that will add courses as a dictionary
    # to our attribute (courses)...which is a list
    def add_course(self, course_name, quarter, n_students):
        
        =.append({'course_name': course_name, 
                             'quarter' : quarter, 
                             'n_students': n_students})
        # increase value store in n_courses
        # by 1 any time a class is added
        self.n_courses += 1


# In[97]:


ellis_courses = ProfCourses('Ellis')


# In[101]:


ellis_courses.courses


# In[102]:


ellis_courses.add_course('COGS18', 'fa20', 363)


# In[104]:


ellis_courses.courses


# In[66]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a class
ellis_courses.add_course('COGS18', 'fa20', 363)

# see output
print(ellis_courses.courses)
ellis_courses.n_courses


# **`compare()` method**

# In[105]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof
    
    def add_course(self, course_name, quarter, n_students):
        
        self.courses.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        self.n_courses += 1
            
    # add method to compare values in courses
    def compare(self, attribute, direction='most'):
    
        fewest = self.courses[0]
        most = self.courses[0] 
        
        for my_course in self.courses:
            if my_course[attribute] <= fewest[attribute]:
                fewest = my_course
            elif my_course[attribute] >= most[attribute]:
                most = my_course
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output


# In[106]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_course('COGS18', 'fa20', 363)
ellis_courses.add_course('COGS108', 'fa20', 447)
ellis_courses.add_course('COGS18', 'su20', 88)
ellis_courses.add_course('COGS108', 'sp20', 469)
ellis_courses.add_course('COGS108', 'sp19', 825)

# see the courses
print(ellis_courses.n_courses)
ellis_courses.courses


# In[107]:


# make comparison among all courses
# returns the class with the most students
ellis_courses.compare('n_students')


# In[108]:


# return the class with the fewest students
ellis_courses.compare('n_students', 'fewest')


# **extending the functionality of the `compare()` method**

# In[115]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof
    
    def add_course(self, course_name, quarter, 
                   n_students, n_exams, n_assignments):
        
        # add in additional key-value pairs
        self.courses.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students,
                             'n_exams' : n_exams,
                             'n_assignments' : n_assignments})
        self.n_courses += 1
             
    def compare(self, attribute, direction='most'):
    
        fewest = self.courses[0]
        most = self.courses[0] 
        
        for my_course in self.courses:
            if my_course[attribute] <= fewest[attribute]:
                fewest = my_course=
            elif my_course[attribute] >= most[attribute]:
                most = my_course
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output


# In[116]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_course('COGS18', 'fa20', 363, 2, 5)
ellis_courses.add_course('COGS108', 'fa20', 447, 0, 6)
ellis_courses.add_course('COGS18', 'su20', 88, 3, 5)
ellis_courses.add_course('COGS108', 'sp20', 469, 0, 6)
ellis_courses.add_course('COGS108', 'sp19', 825, 0, 5)
ellis_courses.add_course('COGS18', 'fa19', 301, 2, 4)

# see the courses
print(ellis_courses.n_courses)


# In[117]:


# return the class with the most exams
ellis_courses.compare('n_exams', 'most')


# In[118]:


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

# In[109]:


print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))


# ### Functions are objects

# In[110]:


print(isinstance(sum, object))
print(isinstance(max, object))


# In[111]:


# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)


# ### Class definitions & instances are objects

# In[112]:


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
