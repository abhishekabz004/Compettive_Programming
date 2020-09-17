'''
QUESTION link: https://www.hackerearth.com/problem/algorithm/substring/description/

'''

import re

def numberOfSubstrings(n) :
    #print("n",n)
    return int(n * (n+1) / 2)


def findAllSubstrings(s, n): 
    count = 0
    subcount = 0
    for i in range(n): 
        if bool(re.match('^[AaBbCc]+$', s[i])):
            subcount += 1
        else:
            count += numberOfSubstrings(subcount)
            subcount = 0
    count += numberOfSubstrings(subcount)
    return count
  

T = int(input())
while T != 0:
    T -= 1
    string = input()
    print(findAllSubstrings(string, len(string)) )
