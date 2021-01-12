#!/usr/bin/env python
# coding: utf-8

# # Assignment-I
#  
# 

# In[6]:


x=5
a=x**2+5*x+6
b=2*x+5
c= a/b
print(c)


# In[7]:


x=5
a=2*x-3
b=x+9
c= a*b
print(c)


# In[1]:


x=5
a=2*x-3
b=x-9
c=a*b
print (c)


# In[ ]:



print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hytu76E' and username=='bank_admin':
        print('Access granted')
    
        break
    else:
        print('Access denied. Try again.')
        count += 1


# In[ ]:





# In[ ]:





# In[ ]:




