#!/usr/bin/env python
# coding: utf-8

# ## Python program to create a simple Calculator

# #### Two steps to build calculator program
# #### 1. Functions for operations
# #### 2. User input & print result

# 

# ## Step-1: Create functions

# ### Function to add two numbers

# In[13]:


# Function to add two numbers
def add(num1,num2):
    return num1+num2

# Function to Substract two numbers
def sub(num1,num2):
    return num1-num2

# Function to multiply two numbers
def multiply(num1,num2):
    return num1*num2

# Function to divide two numbers
def divide(num1,num2):
    return num1/num2

# Function to Average of two numbers
def avg(num1,num2):
    return (num1+num2)/2


# ## Step-2: Create User input & Print result

# In[18]:


print("Please select an operation:\n" \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiply\n" \
      "4. Division\n" \
      "5. Average\n")

select = int(input("Select an operation from 1 to 5:"))
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

# Print the result
if select==1:
    print(number1,"+",number2,"= ",add(number1,number1))
elif select==2:
    print(number1,"-",number2,"= ",sub(number1,number2))
elif select==3:
    print(number1,"*",number2,"= ",multiply(number1,number2))
elif select==4:
    print(number1,"/",number2,"= ",divide(number1,number2))
elif select==5:
    print("(",number1,"+",number2,")","/","2","= ",avg(number1,number2))
else:
    print("Invalid operation! Pls select again!")


# In[ ]:




