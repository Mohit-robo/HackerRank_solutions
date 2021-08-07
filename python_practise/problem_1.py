
##  Source: https://prepinsta.com/accenture/coding/
 
"""
Question_1:

def differenceofSum(n. m) .......

The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.

Assumption:

    n>0 and m>0
    Sum lies between integral range

Example

Input
n:4
m:20
Output
90

Explanation :

    Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
    Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
    Difference 150 – 60 = 90

Sample Input
n:3
m:10
Sample Output
19


"""

####################  Mine Code  ################


def sum_of_nos(n,m):
    global sum1,sum2
    sum1 = 0
    sum2 = 0
    sum_all = m //  2 * (m+1)
    print("Sum of all",sum_all)

    for i in range (m+1): 
        if i % n == 0:
            sum1 += i
        else:
            sum2 +=i
           
           
    print("Sum of Difference:",abs(sum2-sum1))

n = int(input("Value of n: "))
m = int(input("Value of m: "))
sum_of_nos(n,m)


########################  Source's Code ###################

n = int(input())
m = int(input())
sum1 = 0
sum2 = 0
for i in range(1,m+1):
    if i % n == 0:
        sum1+=i
    else:
        sum2+=i
print(abs(sum2-sum1))