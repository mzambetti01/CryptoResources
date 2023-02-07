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

# DSA Alg - 1.1

# 1 - generate prime p
p = 59
# 2 - generate prime divisor q of p-1
q = 29
# 3 - Find alpha with ord(alpha) = q
alpha = 3
# 4 - choose a random int d (0 <d < q)
d = 23
# 5 - compute beta = alpha^d mod p
beta = (alpha**d) % p
print("beta =",beta)

# DSA Alg - 1,2

# Keys are:
k_pub = (p, q, alpha, beta)
k_pr = (d)
print("k_pub =", k_pub)
print("k_pr =", k_pr)

# DSA Alg - 2

# Given message x, private key d and pub key = (p, q, alpha, beta)
# Choose ephemeral key, k_E, 0 < k_E < q
k_E = 13
# Compute r = (alpha^k_E mod p) mod q
r = ((alpha**k_E) % p) % q
# Compute s = ((SHA(x) + d*r) * k_E^-1) mod q
SHA_x = 2
k_E_inv = modular_inverse(k_E, q)
s = ((SHA_x + d*r) * k_E_inv) % q
# Signatur = (r, s)
print("(r,s) =",(r,s))

# DSA Alg - 3 (Verification)

# Given message x, signature (r,s) and pub key (p, q, alpha, beta)
# 1 - compute inverse of s: w = s^-1 mod q
w = modular_inverse(s, q)
print("w =", w)
# 2 - computer auxilery value u_1 = w * SHA(x) mod q
u_1 = (w*SHA_x) % q
print("u_1 =", u_1)
# 3 - compute auxilery value u2 = w * r mod q
u_2 = (w * r) % q
print("u_2 =", u_2)
# 4 - compute v = ((alpha^u1 * beta^u2) mod p) mod q
v = (((alpha**u_1) * (beta**u_2)) % p) % q
print("v = ", v)

