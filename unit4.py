#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print("\t", i*j) # j == 9時，換行
        else:
            print("\t", i*j, end = '') # j < 9時，不換行


# In[5]:


for i in "Hey yushan":
    if i == "u":
        break
    print(i)


# In[6]:


for i in "Hey yushan":
    if i == "u":
        continue
    print(i)


# In[7]:


i = 1
while i <= 10:
    print(i, end=" ")
    i = i + 1


# In[10]:


sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum, end= " ")


# In[11]:


sequences = [0, 1, 2, 3, 4, 5]
i = 0
while 1: #判斷條件值為1, 代表迴圈永遠成立
    print(sequences[i], end = " ")
    i = i + 1
    if i == len(sequences):
        print("No elements left.")
        break


# In[12]:


i = 0
while i < 10:
    i = i + 1
    if i == 4:
        continue
    print (i, end = " ")


# In[13]:


i = 10
while i > 0:
    i = i - 1
    if i == 4:
        continue
    print(i, end = " ")


# In[ ]:




