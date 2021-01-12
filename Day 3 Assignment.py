#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python function to find the Max of three numbers.

# In[3]:


def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(5, -2, 10))


# 2. Write a Python function that checks whether a passed string is palindrome or not

# In[8]:


def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# 3. Write a Python function that accepts a string and calculate the number of uppercase letters and
#    lowercase letters

# In[10]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('My self learning a New Language Python')


# 4. Write a Python function to sum all the numbers in a list

# In[12]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0,5,16,7)))


# 5. Write a Python function to multiply all the numbers in a list

# In[15]:


def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((2, 2, 3, 10, 9)))


# 6. Write a Python function that takes a list and returns a new list with unique elements of the first list

# In[17]:


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,2,3,3,3,33,44,44,5]))


# In[ ]:




