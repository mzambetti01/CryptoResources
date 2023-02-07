# Inputs
# y^2 = x^3 + a*x + b
a = 1
b = 6
p = 11
Q= (3, 1)
k_PrA = 7
k_PrB = 3

# Alice
k_PubA = A = ecc_multiplier(k_PrA, Q, p)
print("k_PubA =", k_PubA)
# Bob
k_PubB = B = ecc_multiplier(k_PrB, Q, p)
print("k_PubB =", k_PubB)

# Adjusting for specific problem
B = (5,9)

# Alice
T_ab = ecc_multiplier(k_PrA, B, p)
print("Alice: T_ab =", T_ab)

# Bob
T_ab = ecc_multiplier(k_PrB, A, p)
print("Bob: T_ab =", T_ab)

# Multiplying point 'point' k times in mod p
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

# Adding Point 1 and point 2 in mod p
def point_adder(point1, point2, p):
    x1, y1 = point1
    x2, y2 = point2
    # Calculating S
    if (x1 == x2) and (y1 == y2):
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
