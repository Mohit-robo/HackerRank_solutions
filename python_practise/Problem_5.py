
##  Source: https://prepinsta.com/accenture/coding/

'''
Question 5 :

char*MoveHyphen(char str[],int n);

The function accepts a string “str” of length ‘n’, that contains alphabets and hyphens (-). Implement the function to move all hyphens(.) in the string to the front of the given string.

NOTE:- Return null if str is null.

Example :-

    Input:
        str.Move-Hyphens-to-Front
    Output:
        -MoveHyphenstoFront

Explanation:-

The string “Move-Hyphens -to-front” has 3 hyphens (.), which are moved to the front of the string, this output is “— MoveHyphen”

Sample Input

    Str: String-Compare

Sample Output-

    -StringCompare


'''

import re

############  Solution _1 ###########

### Uncomment to try this.......



input_string = input("Please Enter the statement with hyphens : ")

new_string = ''.join(char for char in input_string if char.isalnum())

hyphen_count = 0

for i in input_string:
    if i in "-":
        hyphen_count +=1

print("-"*hyphen_count, new_string)



###### Solution _2  ###########


input_string = input("Please Enter the statement with hyphens : ")

new_string = ''.join(filter(str.isalnum,input_string))
hyphen_count = 0

for i in input_string:
    if i in "-":
        hyphen_count +=1

print("-"*hyphen_count, new_string)


########  Solution_3  ###########


input_string = input("Please Enter the statement with hyphens : ")

new_string = re.sub(r"[^a-zA-Z0-9]","",input_string)

hyphen_count = 0

for i in input_string:
    if i in "-":
        hyphen_count +=1

print("-"*hyphen_count, new_string)


#########  Source_ Solution ########

inp = input()
count = 0
final = ""
for i in inp:
    if i == '-':
        count+=1
    else:
        final+=i
print("-"*count,final)