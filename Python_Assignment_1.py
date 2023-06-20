#!/usr/bin/env python
# coding: utf-8

# # Q1
# 
# <p> 
# 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# 
# <h5>
# 1 : *  -> Multiplication operator
# 
# 2 : 'hello' -> String value
# 
# 3 : -87.8   -> Float value
# 
# 4 : -  -> Subtract operator
# 
# 5 : /  -> Div operator
# 
# 6 : +  -> addition operator 
# 
# 7 : 6  -> Integer Value   
# 
# <h5/>
# 
# <p/>

# # 2. What is the difference between string and variable?
# 
# 
# <h5>
# 
# A Variable is a store of information used to assigning a value, and a String is a type of information you would store in a Variable. A String is usually words, enclosed with "".
#     
# Note : string should be written in single quote , double quote , quote. 
#        Name : 'Yasin'
# 
# example :
# 
# String  x = "Yasin"
# 
# here x is variable and type of value it stores is in string 
# 
# <h5/>

# # 3. Describe three different data types.
# 
# <h5>
# 1 - Integer data type. ex :1,10,-20
# 
# 2 - floating number. ex : values with decimal (20.5,-1.3)
# 
# 3 - Boolean.   ex : True or False 
# 
# 4 - List.
# Lists are just like the arrays, declared in other languages which is a ordered collection of data. It is very flexible as the items in a list do not need to be of the same type. ex- [20,'yasin',True]
# 
# <h5/>

# # 4. What is an expression made up of? What do all expressions do?
# 
# <h5>
# An expression in Python is a combination of operators and operands.
# 
# An example of expression can be : x = x + 10. In this expression, the first 10 is added to the variable x. After the addition is performed, the result is assigned to the variable x.
# 
# ex
# 
# x = 25          a statement
# 
# x = x + 10      an expression
# 
# 
# <h5/>

# # 5 This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 
# 
# <h5>
# spam = 10          --- #is a statement
# 
# x = spam + 10      --- #is an expression
# 
# print(x) 
# 
# output : 20
# 
# <h5/>

# # 6. After running the following code, what does the variable bacon contain?
# 
# <h5>
# 
# bacon = 22
# 
# bacon + 1
# 
# print(bacon) 
# 
# O/P : 23
# 
# <h5/>

# In[1]:


bacon = 22
bacon + 1
print(bacon)


# # 7. What should the values of the following two terms be?
# <h5>
# '''
# 
# 'spam' + 'spamspam'   = O/P  'spamspamspam'
# 
# 'spam' * 3            = O/P  'spamspamspam'
# 
# 
# '''
# <h5/>

# In[2]:


a = 'spam' + 'spamspam'
print(a)


# In[3]:


b = 'spam' * 3
print(b)


# # 8. Why is eggs a valid variable name while 100 is invalid?
# <h5>
# '''
# 
# Ans : Because varible name must start with alphabet or _ underscore. eggs is valid variable name and 100 is invalid.
# 
# '''
# <h5/>

# # 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# <h5>
# '''
# 
# The int() , float() , and str( ) functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.
# 
# 
# '''
# <h5/>

# # 10. Why does this expression cause an error? How can you fix it?
# <h5>
# '''
# 
# 'I have eaten' + 99 + 'burritos.'
# 
# Type error : can only concatenate str (not "int") to str.
# 
# How can we fix it?
# 
# changing 99 int value to string value just by giving '99' in qoutes.
# 
# '''
# <h5/>
# 

# In[4]:


e = 'I have eaten' + 99 + 'burritos.'


# In[5]:


d = 'I have eaten '  +  '99'   + ' burritos.'    # check output


# In[6]:


print(d)


# In[ ]:




