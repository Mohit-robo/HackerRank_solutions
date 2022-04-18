'''
You are given a list nums, write a program to rotate the list nums towards right if k is positive or towards left if k is negative.
(see explanation more description)

Input is managed for you.
Input:
[1, 2, 3, 4, 5]
3

Output:
[3, 4, 5, 1, 2]

Explanation:

Since k is 3 which is positive we will perform a right rotation.
On first rotation [1,2,3,4,5] will become [5,1,2,3,4]
On second rotation [5,1,2,3,4] will become [4,5,1,2,3]
On third rotation [4,5,1,2,3] will become [3,4,5,1,2]

For -3 
[1,2,3,4,5] will do left rotation and become [4,5,1,2,3]

'''

nums = list(map(int, input().split()))
k = int(input())
def shift (L,k):

    if k > 0:
        a = k % len(L)

        return L[-a:] + L[:-a]
    else:
        a = k % len(L)

        return L[a:] + L[:a]

print(shift(nums,k))
