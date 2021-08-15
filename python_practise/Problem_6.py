
##  Source: https://prepinsta.com/accenture/coding/

'''
A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

You are required to implement the following function.

Int NumberOfCarries(int num1 , int num2);

The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

Assumption: num1, num2>=0

Example:

    Input
        Num 1: 451
        Num 2: 349
    Output
        2

Explanation:

Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.

Sample Input

Num 1: 23

Num 2: 563

Sample Output

0

'''
############ Solution #############

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")


def NumberOfCarries(n1,n2):

    count=0

    carry = 0

    if len(n1) <= len(n2):

        l= len(n1)-1

    else:

        l = len(n2)-1

    for i in range(l+1):

        temp = int(n1[l-i])+int(n2[l-i])+carry

        if len(str(temp))>1:

            count+=1

            carry = 1

        else:

            carry = 0

    return count+carry

print(NumberOfCarries(num_1,num_2))
