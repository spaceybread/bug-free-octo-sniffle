from sympy import mod_inverse

def extd(ea, lam):
    return mod_inverse(ea, lam)

def gcd3(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd3(b, a % b)
        
def lcm3(a, b):
    return int((abs(a * b))/(gcd3(a, b)))

def prime(n):
    p = [True for i in range(n+1)]
    
    p_n = 2
    while (p_n**2 < n):
        if (p[p_n] == True):
            for i in range(p_n**2, n + 1, p_n):
                p[i] = False
        
        p_n = p_n + 1
    
    return p

def largestTwoPrime(arr):
    p = 0
    q = 0
    c = 0
    for i in range(len(arr)):
        if arr[len(arr) - 1 - i] == True:
            if c == 0:
                p = len(arr) - 1 - i
                c = c + 1
            else:
                q = len(arr) - 1 - i
                return [p, q]


pri = 1000
#pick pri such that pri**2 >> m
#leave room for error, pri is the upper limit, it is not always the largest prime that will be used


out = largestTwoPrime(prime(200))

p =  out[0] # prime
q =  out[1] # prime

n = p * q
#part of the public key

lamA = lcm3(p - 1, q - 1)#lcm of (p - 1) and (q - 1)
# can use extended euler algorithm to find LCM from the gcd

e = 2**16 + 1 # weird number
# e > 2, less than lamA, and must be coprime with, again, lamA

d = extd(e, lamA) #modular mulitplicative inverse of e mod lamA
# this is the private key

print(p, q, n, lamA, e, d)
print()

m = 31415 #this is the message, in my case I will just use some random number and not actual text

c = (m**e) % n
#encrypted text

m_c = (c**d) % n
#decrypted text

print(m, c, m_c, m == m_c)

#if m == m_c, this system works
