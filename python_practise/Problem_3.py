##  Source: https://prepinsta.com/accenture/coding/

"""
Question 3:

def ProductSmallestPair(sum, arr)

The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair

NOTE

    Return -1 if array is empty or if n<2
    Return 0, if no such pairs found
    All computed values lie within integer range

Example

Input

sum:9

Arr:5 2 4 3 9 7 1

Output

2

Explanation

Pair of least two element is (2, 1) 2 + 1 = 3 < 9, Product of (2, 1) 2*1 = 2. Thus, output is 2

Sample Input

sum:4

Arr:9 8 3 -7 3 9

Sample Output

-21

"""
##########################  Mine Code ###############

main_sum = int(input("Enter the summ:"))
length = int(input("Enter the length of array:" ))

if length < 2:
    print("-1")

lst = []
contents = []
for i in range (0,length):
    cont = input("Enter the elements of array : ")
    contents.append(cont)

contents.sort()
print(contents)
j = contents[0]
k = contents[1]
j = int(j)
k = int(k)

if (j+k) <= main_sum:

    prod = j*k
    print(prod)
else:
    print("0")


################  Source Code  ################

n = int(input())
sum1 = int(input())
arr = list(map(int, input().split()))
if n < 2:
    print('-1')
arr = sorted(arr)
for i in range(n-1):
    if arr[i] + arr[i+1] < sum1:
        print(arr[i] * arr[i+1])
        break
else:
    print('0')