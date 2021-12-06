"""   Time Conversion     """

### https://www.hackerrank.com/challenges/time-conversion


################### Solution 1 

"""

stng = "06:00:00PM"

yes =  stng.endswith('PM')
in_stng = int(stng[0:2])

# print(type(in_stng))
if yes and in_stng < 12 :
    in_stng += 12 

if not yes and in_stng == 12 :
    in_stng = 0 

new_stng = str(in_stng)

last_stng = stng[2:-2]
final_stng =  new_stng + last_stng 
print(final_stng)

"""

############## Solution 2

"""
import re

stng = "06:00:00PM"
times = re.search(r"(?P<hh>..):(?P<mm>..):(?P<ss>..)(?P<ampm>..)",stng)
    hour = times.group('hh')
    
    if times.group('ampm') == 'PM':
        if hour == '12':
            hr = '12'
        else:
            hr = str(int(hour) + 12)
        
    else:
        if hour == '12':
            hr = '00'
        else:
            hr = hour
    print (hr + ':' + times.group('mm') + ':' + times.group('ss'))

"""