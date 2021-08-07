

##  Source: https://prepinsta.com/accenture/coding/
 
"""
Question 2:

def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest largest element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

    All array elements are unique
    Treat the 0th position a seven

NOTE

    Return 0 if array is empty
    Return 0, if array length is 3 or less than 3

Example

Input

arr:3 2 1 7 5 4

Output

7

Explanation

    Second largest among even position elements(1 3 5) is 3
    Second largest among odd position element is 4
    Thus output is 3+4 = 7

Sample Input

arr:1 8 0 2 3 5 6

Sample Output

8

"""




##################  Mine  #################
length  = int(input("Enter the length of array :"))

lst = []

for ele in range(0,length):
    contents = input("Values here : ")
    lst.extend(contents)

    odd_num = lst[1::2]
    odd_num.sort()
        
    even_num = lst[0::2]
    even_num.sort(reverse=True)

print("lst = ",lst)

print("odd = ",odd_num)
small_2nd = odd_num[1]
small_2nd = int(small_2nd)
print("small_2nd = ",small_2nd)

print("even_num = ",even_num)
large_2nd = even_num[1]
large_2nd = int(large_2nd)

print("large_2nd = ",(large_2nd))

final = small_2nd + large_2nd
print("Final_sum = ",final)


#################### PrepInsta ###################
length = int(input())
arr = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(length):
    if i % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])
even_arr = sorted(even_arr)
odd_arr = sorted(odd_arr)
print(even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])