#!/usr/bin/env python
# coding: utf-8

# RSA Encoder

# In[6]:


# Inputs
p = 33
q = 11
e = 17
x = None


# In[11]:


# Other values needed for RSA
n = p*q
print("n =", n)
phi = (p-1)*(q-1)
print("phi =", phi)
d = modular_inverse(e, phi)
print("d =",d)


# In[3]:


def modular_inverse(b, a):
    mod = a
    #a = 640 # mod number
    #b = 49 # number to find inverse
    q = a // b # quotient
    r = a % b # remainder
    s1 = 1
    s2 = 0
    s3 = 1
    t1 = 0
    t2 = 1
    t3 = t1 - q*t2

    while (not r==0):
        a = b
        b = r
        q = a // b
        r = a % b
        s1 = s2
        s2 = s3
        s3 = s1 -q*s2
        t1 = t2
        t2 = t3
        t3 = t1 - q*t2
    if t2 < 0:
        t2 += mod
    return t2


# In[12]:


y = mod_exponent(x, e, n)
print(y)


# In[5]:


def mod_exponent(x, e, n):
    h = bin(e)
    h = h[2:]

    y = x

    for idx in range(1, len(h)):
        y = (y*y)%n

        if h[idx] == "1":
            y = (y*x)%n

    return y


# In[ ]:




