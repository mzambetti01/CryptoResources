# Givens
p = 31
q = 37
e = 17
y = 2
n = p*q

# Need to solve for
d = None     # modular inverse of e
dp = None
dq = None
xp = None
xq = None
cp = None
cq = None
x = None

# Values needed for computation
phi = eulers_phi_function(p, q)
d = modular_inverse(e, phi)
print("Phi:", phi)
print("Modular Inverse of e:", d)
Phi: 1080
Modular Inverse of e: 953

def eulers_phi_function(p, q):
    return (p-1)*(q-1)
    
def modular_inverse(b, a):
    mod = a
    q = a // b
    r = a % b
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

dp = d % (p-1)
dq = d % (q-1)
print("dp is:", dp)
print("dq is:", dq)
dp is: 23
dq is: 17

# xp = y ^ (dp) mod p
# xq = y ^ (dq) mod q
xp = mod_exponent(y, dp, p)
xq = mod_exponent(y, dq, q)
print("xp is:", xp)
print("xq is:", xq)
xp is: 8
xq is: 18

def mod_exponent(x, e, n):
    h = bin(e)
    h = h[2:]
    y = x
    for idx in range(1, len(h)):
        y = (y*y)%n
​
        if h[idx] == "1":
            y = (y*x)%n
    return y

cp = modular_inverse(q, p)
cq = modular_inverse(p, q)
x = ((q*cp)*xp + (p*cq)*xq) % n
print("cp is:", cp)
print("cq is:", cq)
print("dp is:", dp)
print("X is:", x)
cp is: 26
cq is: 6
dp is: 23
X is: 721
