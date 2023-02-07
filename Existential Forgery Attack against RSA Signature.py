#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Inputs from Bob
k_pr = d = None
k_pub = (n, e) = (9797, 131)


# In[9]:


# Oscar Attack
# 1. choose signature
s = 117
# 2. choose message
x = (s**e) % n


# In[10]:


# Verification
# x' = s^e mod n
# basically x = x'
print(x)


# In[ ]:




