
'''
Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem

Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it.
She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. 
You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, . She wants to find segments summing to Ron's birth day,  
with a length equaling his birth month, . In this case, there are two segments meeting her criteria:  and .

Function Description:

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s):

    s: an array of integers, the numbers on each of the squares of chocolate
    d: an integer, Ron's birth day
    m: an integer, Ron's birth month

Input Format

The first line contains an integer , the number of squares in the chocolate bar.
The second line contains  space-separated integers , the numbers on the chocolate squares where .
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.

Output Format

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

Sample Input 0

5
1 2 1 3 2
3 2

Sample Output 0

2

Explanation 0

Lily wants to give Ron  squares summing to . The following two segments meet the criteria:
image

Sample Input 1

6
1 1 1 1 1 1
3 2

Sample Output 1

0

Explanation 1

Lily only wants to give Ron  consecutive squares of chocolate whose integers sum to . There are no possible pieces satisfying these constraints:
image

Thus, we print  as our answer.

Sample Input 2

1
4
4 1

Sample Output 2

1

Explanation 2

Lily only wants to give Ron  square of chocolate with an integer value of . Because the only square of chocolate in the bar satisfies this constraint, we print  as our answer.

'''

## Solution 1:
def birthday(s, d, m):
    count_ = 0
    for i in range (0,len(s)):
        if sum(s[i:i+m]) == d:    
                count_ += 1 
    return count_ 

## Solution 2:
  def birthday(s,d,m):
    count_ =0
    add = sum(s[:m])
    if add==d:
        count_ +=1
    for i in range(m,len(s)):
        add= add+s[i]-s[i-m]
        if add==d:
            count_+=1
    return count_
  
n = int(input().strip())

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])

result = birthday(s, d, m)
print(result)
  
