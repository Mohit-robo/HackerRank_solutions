'''
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

    int scores[n]: points scored per game

Returns

    int[2]: An array with the numbers of times she broke her records. Index 

is for breaking most points records, and index

    is for breaking least points records.

Input Format

The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective values of .

Link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records

'''

## Solution 1
def breakingRecords(scores):
    high_ = scores[0]
    high_count = 0
    for i in range (len(scores)):
        if scores[i] > high_:
            high_count += 1
            high_ = scores[i]
    
    low_ = scores[0]
    low_count = 0

    for i in range (len(scores)):
        if scores[i] < low_:
            low_count += 1
            low_ = scores[i]

    return (high_count,low_count)
  
## Solution 2:
def breakingRecords(s):
    highest_score = 0
    lowest_score = 0
    count_highest = 0
    count_lowest = 0
    for i in range(len(s)):
        if i == 0:
            highest_score = lowest_score = s[i]
        elif s[i] > highest_score:
            highest_score = s[i]
            count_highest += 1
        elif s[i] < lowest_score:
            lowest_score = s[i]
            count_lowest += 1
    
    return (count_highest, count_lowest)
