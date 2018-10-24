# Name: Wonbin Song
# hw3.py

##### Template for Homework 3, exercises 1 -  ######

from math import *
import random


# ********** Exercise 1 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
    
def is_divisible(m,n):
    if(n==0) :
        print("Divisor cannot be 0")
    elif (m % n == 0):
        return True
    else:
        return False
        
# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?

print(is_divisible(10, 5))
print(is_divisible(18, 7))
print(is_divisible(42, 0))

# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####

def not_equal(m,n):
    if (m==n):
        return False
    else:
        return True
    
# Test cases for not_equal
##### YOUR CODE HERE #####

print(not_equal(10,10))
print(not_equal(1,10))
# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####

def multadd(a,b,c):
    return a*b+c

multadd(2,4,3)

## 2 - Equations
##### YOUR CODE HERE #####

angle_test = multadd(cos(pi/4), 1/2, sin(pi/4))
celing_test = multadd(log(12,7), 2, ceil(276/19))

# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

print("sin(pi/4) + cos(pi/4)/2 is:") 
print(angle_test)

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

print("ceiling(276/19) + 2 log_7(12) is:")
print(celing_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

def rand_divis_3():
    n = random.randint(0,100)
    print ("Random Number:", n)
    if (n % 3 == 0):
        print ("Divisible by 3?")
        return True
    else:
        print ("Divisible by 3?")
        return False

# Test Cases
##### YOUR CODE HERE #####

print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
