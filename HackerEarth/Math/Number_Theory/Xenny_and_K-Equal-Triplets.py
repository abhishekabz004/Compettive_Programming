'''
QUESTION link: https://www.hackerearth.com/problem/algorithm/xenny-and-k-equal-triplets/

'''


import math

def gcd(a,b): 
      
    # Everything divides 0  
    if (b == 0): 
         return a 
    return gcd(b, a%b) 

def nCr(n, r): 
    num = 1
    den = 1
    prod = 1

    for i in range(r):
        num *= (n-i)
        den *= (r-i)
        if i % 10 == 1:
            prod *= (num/den)
            num = 1
            den =1
    prod *= (num/den)

    return math.floor(prod)

t = int(input())

while t != 0:
    t -= 1
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    num = nCr(array.count(k), 3)
    den = nCr(len(array), 3)
    num = int(num)
    den = int(den)
    hcf = gcd(num,den)
    num = num//hcf
    den = den//hcf
    output = str(num)
    output += "/"
    output += str(den)
    print (output)

