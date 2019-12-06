#!/usr/bin/env python
# coding: utf-8

# In[15]:


a="family"
b="good" 
print(a,end="\n")
print(b)


# In[16]:


a="family"
b="good" 
print(a,end="\t")
print(b)


# In[17]:


a="family"
b="good" 
print("\"a\"")


# In[24]:


def print_twice(s1, s2):
    s1=apple
    s2=pine

    print(s1)
    


# In[25]:


c = 66
cAsChr = chr(c)
print(cAsChr)


# In[27]:


floatNum = 55.0

print(floatNum)
print(intNum)
print(type(floatNum))


# In[33]:


floatNum = 55
intNum = int(str(floatNum ))
print(floatNum)
print(intNum)
print(type(floatNum))
print(type(intNum))


# In[35]:


score = int(input("請輸入成績"))
if score >= 60:
    print("成績及格!")


# In[38]:


score=int(input("score:"))
if score >= 70:
    print("pass")
else:
    print("no pass")


# In[39]:


a = input("a: ")
b = input("b: ")
if a > b:
    print("max: ", a)
else: 
    print("max: ", b)


# In[40]:


score = int(input("score: "))
if score >= 90:
    print('Grade is: A')
elif score >= 80:
    print('Grade is: B')
elif score >= 70:
    print('Grade is: C')
elif score >= 60:
    print('Grade is: D')
else:
    print('Grade is: F')


# In[ ]:


ID = input()
year = int(ID[1:3])
if year < 4:
    print("Graduated")
elif year <= 7 and year >= 4:
    if year == 7:
        print("Freshman")
    elif year == 6:
        print("Sophomore")
    elif year == 5:
        print("Junior")
    elif year == 4:
        print("Senior")
else:
    print("Not Registered Yet")


# In[3]:


sequences = [0, 1, 2, 3, 4, 56]
for i in sequences:
    print(i)


# In[9]:


lis = [0, 1, 2, 3, 4,8,5,7]
for i in lis:
    print(i)


# In[11]:


theBeatles = ['John Lennon', 'Paul McCartney', 'Ringo Starr', 'George Harrison']
for i in range(len(theBeatles)):
    print(theBeatles[i])
#theBeatles[i] = i 元素
#len()= list 長度


# In[12]:


theBeatles = ['John Lennon', 'Paul McCartney', 'Ringo Starr', 'George Harrison']
for beatle in theBeatles:
    print (beatle)


# In[14]:


for i in range(10):
    print(i, end=" ")
    
print() #換行
for i in range(20, 2, -2):
    print(i, end=" ")


# In[ ]:




