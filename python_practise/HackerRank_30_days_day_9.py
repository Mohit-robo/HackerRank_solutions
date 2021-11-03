"""
Objective
Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.

Recursive Method for Calculating Factorial

Function Description
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following paramter:

    int n: an integer

Returns

    int: the factorial of

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of

.

Input Format

A single integer,
(the argument to pass to factorial).
"""



##### Solution_1 ####

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num


#### Solution_2 #####

def factorial(n):
    return math.factorial(n)

#### Solution_3 ####

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
