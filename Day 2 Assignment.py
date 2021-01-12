#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to remove duplicates from a list

# In[1]:


a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# 2. Write a Python program to get the difference between the two lists

# In[5]:


list1 = [1, 3, 5, 7, 9,10]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)


# 3. Write a Python program to get the frequency of the elements in a list

# In[4]:


import collections
my_list = [30,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)


# 4. Write a Python program to compute the similarity between two lists.

# In[6]:


from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ",list(counter1 - counter2))
print("Color2-Color1: ",list(counter2 - counter1))


# In[ ]:




