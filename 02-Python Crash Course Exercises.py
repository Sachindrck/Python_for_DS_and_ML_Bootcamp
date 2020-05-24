#!/usr/bin/env python
# coding: utf-8

# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7 ** 4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[3]:


s = "Hi there Sam!"


# In[4]:


list(s.split())


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[6]:


planet = "Earth"
diameter = 12742


# In[7]:


"The diameter of {} is {} kilometers.".format(planet, diameter)


# ** Given this nested list, use indexing to grab the word "hello" **

# In[10]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[14]:


lst[3][1][2][0]


# In[14]:





# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[15]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[22]:


d['k1'][3]['tricky'][3]['target'][3]


# In[22]:





# ** What is the main difference between a tuple and a list? **

# In[23]:


# 1
# Tuple is immutable
# List is mutable
# 2
# Tuples have fixed length
# list have variable length


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com    
# **So for example, passing "user@domain.com" would return: domain.com**

# In[33]:


def domainGet(email):
    return list(email.split('@'))[1]

def userName(email):
    return list(email.split('@'))[0]


# In[34]:


userName('sachindrck25@gmail.com')


# In[31]:


domainGet('user@domain.com')
domainGet('sachindrck25@gmail.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[16]:


def findDog(s):
    list_words = s.split()     
    
    for word in list_words:
        if word == 'dog' or word == 'Dog':
            return True
    return False


# In[19]:


findDog('Is there a Dogs here?')


# In[20]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[21]:


def countDog(s):
    list_words = s.split()     
    
    counter = 0
    for word in list_words:
        if word == 'dog' or word == 'Dog':
            counter += 1
    return counter


# In[22]:


countDog('This dog runs faster than the other dog dude!')


# In[23]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[29]:


seq = ['soup','dog','salad','cat','great']


# In[30]:


x = filter(lambda word: word[0] == 's', seq)
list(x)


# In[ ]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[31]:


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 'No Ticket'
    elif speed <= 80:
        return 'Small Ticket'
    else:
        return 'Big Ticket'
    


# In[32]:


caught_speeding(91,True)


# In[33]:


caught_speeding(81,True)


# In[34]:


caught_speeding(81,False)


# # Great job!
