'''
Given an array of integers and a positive integer k, determine the number of (i,j)pairs where i<j and ar[i]+ar[j] is divisible by k.

For example,

ar = [1,2,3,4,5,6]  and k=5. 

Our three pairs meeting the criteria are [1,4],[2,3] and [4,6].

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

    n: the integer length of array ar
    ar: an array of integers
    k: the integer to divide the pair sum by

Returns
- int: the number of pairs

Input Format

The first line contains
space-separated integers, and .
The second line contains space-separated integers, each a value of

Constraints

    2<=n<=100
    1<=k<=100
    1<=ar[i]<=100

Sample Input

STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

Sample Output

 5

Link: https://www.hackerrank.com/challenges/divisible-sum-pairs

'''
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(0,n):
            if (ar[i]+ar[j]) % k == 0 and i < j:    
                count += 1
    return count
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
