"""
Problem Statement: https://www.hackerrank.com/challenges/30-scope/problem
"""

## Solution:
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
    def computeDifference(self):
        
        for i in range(len(self.__elements)):
            for j in range (len(self.__elements)):
                absolute = abs(self.__elements[i] - self.__elements[j])
                if absolute > self.maximumDifference:
                    self.maximumDifference = absolute

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()