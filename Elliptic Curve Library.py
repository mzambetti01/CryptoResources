#!/usr/bin/env python
# coding: utf-8

# # Equation inputs for entire library

# In[3]:


# f(x) inputs
# ---------- ---------- ---------- ----------
# y^2 = x^3 + a*x + b mod p
a = 2
b = 3
p = 17


# # Calculating Points on Elliptic Curve
# 
# ## Section Below calculates all points on elliptic curve

# In[ ]:





# In[ ]:





# # Order of Alpha Calculator
# ## Section below calculates order of a given alpha

# In[4]:


# Inputs# Module specific Inputs
# ---------- ---------- ---------- ----------
alpha = (5, 3)

# Calculating all multiples of alpha
# ---------- ---------- ---------- ----------
old_point = alpha
new_point = alpha
multiples = [None, alpha]
for mult in range(2, p+2):
    old_point = new_point
    try:
        new_point = point_adder(old_point, alpha, p)
        multiples.append(new_point)
    except ZeroDivisionError:
        break
print(multiples)
print(len(multiples))

# Determining if alpha generates the group
# ---------- ---------- ---------- ----------
if (len(multiples) != len(group)):
    print("alpha is not a primitive since it does not generate the group")
else:
    for point in multiples:
        if not point in group:
            print("alpha is not a primitive since it does not generate the group")
            break
    print("alpha is a primitive since it generates the group")


# # Addition Calculator for ECC
# ## Below adds two points on an elliptic curve

# In[9]:


# Module specific Inputs
# ---------- ---------- ---------- ----------
x1, y1 = (14, 2)
x2, y2 = (14, 6)
a = 2
b = 3
p = 17
s = None
print(point_adder((x1, y1), (x2, y2), p))


# In[8]:


def point_adder(point1, point2, p):
    x1, y1 = point1
    x2, y2 = point2
    # Calculating S
    if ((x1 == x2) and (y1 == y2)) or (x1==x2):
        d = (2*y1) % p
        d = modular_inverse(d, p)
        s = ((3*(x1*x1)+a)* d) % p
    else:
        d = (x2 - x1) % p
        d = modular_inverse(d, p)
        s = ((y2 - y1)*d) % p
    x3 = (s*s - x1 - x2) % p
    y3 = (s*(x1 - x3) - y1) % p
    return (x3, y3)


# # Multiplication Calculator for ECC
# ## Below multiplies a point and k on an elliptic curve

# In[6]:


# Module specific Inputs
# ---------- ---------- ---------- ----------
point = (8, 10)
k = 20
a = 4
b = 20
p = 29
print(ecc_multiplier(k, point, p))


# In[4]:


def ecc_multiplier(k, point, p):
    old_point = point
    new_point = point
    for mult in range(2, k+1):
        old_point = new_point
        try:
            new_point = point_adder(old_point, point, p)
        except ZeroDivisionError:
            break
    return new_point


# # Functions Used (RUN FIRST)

# ## Modular Inverse Calculator

# In[5]:


# Inverse of b in mod a
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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




