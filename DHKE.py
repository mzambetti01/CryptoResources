# Setting the parameters
alpha = 2
p = 467
a = 228
b = 57

# x^e mod n
def mod_exponent(x, e, n):
    h = bin(e)
    h = h[2:]

    y = x

    for idx in range(1, len(h)):
        y = (y*y)%n

        if h[idx] == "1":
            y = (y*x)%n

    return y

# KA
k_A = mod_exponent(alpha, a, p)
print(k_A)

# KB
k_B = mod_exponent(alpha, b, p)
print(k_B)

# KAB
ab = a*b
k_AB = mod_exponent(alpha, ab, p)
print(k_AB)

