import random

# Set the parameters for NTRU
n = 503
q = 2048
p = 3

# Generate the public and secret keys
# Generate the public and secret keys
def generate_keys():

    f = [0] * n
    g = [0] * n
    while True:
        # Generate random ternary polynomials f and g
        f = [random.choice([-1, 0, 1]) for i in range(n)]
        g = [random.choice([-1, 0, 1]) for i in range(n)]
        
        # Check that gcd(poly_eval(f, 1), q) = 1 and gcd(poly_eval(g, 1), q) = 1
        if gcd(poly_eval(f, 1), q) == 1 and gcd(poly_eval(g, 1), q) == 1:
            break
    
    # Compute the public and secret keys
    h = poly_mul(f, g)
    h = poly_mod(h, q)
    public_key = poly_mul(h, poly_random(n, p))
    secret_key = g
    
    return public_key, secret_key

# Encrypt a message
def encrypt(message, public_key):
    m = poly_eval([int(c) for c in message], 1)
    r = poly_random(n, p)
    e = poly_mul(public_key, r)
    e = poly_mod(e, q)
    e = poly_add(e, m)
    e = poly_mod(e, q)
    return e

# Decrypt a message
def decrypt(ciphertext, secret_key):
    c = ciphertext
    f = secret_key
    cf = poly_mul(c, f)
    cf = poly_mod(cf, q)
    cf = [round(ci / q) for ci in cf]
    m = poly_sub(c, poly_mul(cf, f))
    m = [round(mi / p) for mi in m]
    message = "".join([str(int(mi)) for mi in m])
    print(message)
    return message

# Compute the greatest common divisor of two numbers
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Evaluate a polynomial at a given point
def poly_eval(p, x):
    y = 0
    for i in range(len(p) - 1, -1, -1):
        y = y * x + p[i]
    return y

# Multiply two polynomials
def poly_mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i in range(len(p)):
        for j in range(len(q)):
            r[i + j] += p[i] * q[j]
    return r

# Add two polynomials
def poly_add(p, q):
    r = [0] * max(len(p), len(q))
    for i in range(len(p)):
        r[i] += p[i]
    for i in range(len(q)):
        r[i] += q[i]
    return r

# Subtract two polynomials
def poly_sub(p, q):
    r = [0] * max(len(p), len(q))
    for i in range(len(p)):
        r[i] += p[i]
    for i in range(len(q)):
        r[i] -= q[i]
    return r

# Generate a random polynomial of given degree with coefficients in the range [-p/2, p/2]
def poly_random(degree, modulus):
    return [random.randint(-modulus//2, modulus//2) for i in range(degree)]

# Reduce a polynomial modulo a given modulus
def poly_mod(p, modulus):
    return [pi % modulus for pi in p]



public_key, secret_key = generate_keys()
message = "This is a test, 123!__?"
#ciphertext = encrypt(message, public_key)
#plaintext = decrypt(ciphertext, secret_key)
print("Public key:", public_key)
print("Secret key:", secret_key)

#print("Ciphertext:", ciphertext)
