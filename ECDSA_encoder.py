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

# Key Generation of ECDSA

# 1 - using elliptic curve E with mod p and coefficients a and b
# y^2 = x^3 + ax + b mod p
a = 2
b = 2
p = 17
# 2 - choose random int d with 0 < d < q
d = 10
# 3 - computer B =  d * A
A = (5, 1)
q = 19
B = ecc_multiplier(d, A, p)
print("B =", B)
# Keys are
k_pub = (p, a, b, q, A, B)
k_pr = (d)
print("k_pub =", k_pub)
print("k_pr =", k_pr)
print("this part is correct")

# ECDSA Signature Generation
# given message x, private key d and pub key (p, a, b, q, A, B)

# 1 - choose random k_E such that 0 < k_E < q
k_E = 13
# 2 - compute R = k_E * A
R = ecc_multiplier(k_E, A, p)
print("R =", R)
# 3 - let r be the x-coordinate of R, x_R
r, y_R = R
# Compute s = ((h(x) + d*r) * k_E_inv) mod q
h_x = 4
k_E_inv = modular_inverse(k_E, q)
s = ((h_x + d*r) * k_E_inv) % q

print("(r, s) =",(r,s))

# ECDSA singature verification
# given message x, signature s and pub keu (p, a, b, q, A, B)

# 1 - compute the inverse of s: w = s^-1 mod q
w = modular_inverse(s, q)
# 2 - comput aux value u_1 = w* h_x mod q
u_1 = (w * h_x) % q
# 3 - compute aux value u_2 = w * r mod q
u_2 = (w * r) % q
# 4 - compute P = u_1 * A + u_2 * B
point1 = ecc_multiplier(u_1, A, p)
point2 = ecc_multiplier(u_2, B, p)
P = point_adder(point1, point2, p)
print("w =", w)
print("u_1 =", u_1)
print("u_2 =", u_2)
print("P =", P)

