# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:46:38 2023
@author: HP
"""

'''#GCD using Euclid's Algorithm (good approach)
def gcd(m,n):
    if n>m:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        dif=m-n
        #return(gcd(max(dif,n),min(dif,n)))
        return(gcd(dif,n))
#print(gcd(25,15))

#GCD using Euclid's Algorithm (better approach)
def gcd(m,n):
    if n>m:
        (m,n)=(n,m)
    while m%n!=0:
        dif=m-n
        (m,n)=(max(dif,n),min(dif,n))
        #return(gcd(dif,n))
    return n'''

#GCD using Euclid's Algorithm (even better approach)
def gcd(m,n):
    if n>m:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        dif=m-n
        (m,n)=(max(dif,n),min(dif,n))
        return(gcd(m%n,n))
#This algorithm takes time proportional to number of digits in m(greater number)
print(gcd(25,15))