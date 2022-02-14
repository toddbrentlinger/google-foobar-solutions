"""
 0 0's first digit: 0, 3,6,9
 3 If second digit % 3 == 0
 6 AND first digit % 3 == 0
 9 Is divisible by 3
-- 
12 10's first digits: 2,5,8
15 If 2digit % 3 == 1 AND (1digit + 1) % 3 == 0
18 Is divisible by 3
21 20's first digits: 1,4,7
24 If 2digit % 3 == 2 AND (1digit + 2) % 3 == 0
27 Is divisible by 3
30 30's first digits: 0, 3,6,9
33
36
39
42 40's first digits: 2,5,8
45
48
51
...
99
---
102 100's 2digits: 2,5,8
105 If all but last digit (ex.10 of 105) % 3 == 1
108 AND (last digit + 1) % 3 == 0
111 110's 2digits: 1,4,7
114 If all but last digit (ex.11 of 114) % 3 == 2
117 AND (last digit + 2) % 3 == 0

    - Save remainder of all but last digit % 3
    - If (last digit + remainder) % 3 == 0
        - Is divisible by 3

120 120's 2digits: 3,6,9
123
126
129
...
996
999
---
1002
1005
1008

[] -> [8,6,3,0]
630

[] -> [9,6,3,1]
963

[] -> [7,4,4]
744

[] -> [7,4,4,3]
7443

[3,1,4,1] -> [4,3,1,1]
4311

[3,1,4,1,5,9] -> [9,5,4,3,1,1]
94311

Test highest possible number to lowest possible number
954311 X
95431_ X adjust until different value (skip next '1')
954_11 X
95_311 X
9_4311 O Return number converted from these indices

_54311 
_5431_ skip next '1'
_54_11
_5_311
__4311
__431_ skip next '1'
__4_11
___311
___31_ skip next '1'
____11
____1_ skip next '1'
end loop

Variables:
StartIndex: Index of current max digit being tested.
SkipIndex: Index of digit to be skipped.
Test all digits from StartIndex to last index, not including the SkipIndex.

If sum of all digits is divisible by 3, whole number is divisible by 3

"""

def solution(L):
    # List length cached to not repeatedly call len(L)
    listLength = len(L)
    # Index of current max digit being tested
    startIndex = 0
    # Index of digit to be skipped
    skipIndex = listLength
    
    # Sort list in descending order
    L.sort(reverse=True)

    # If sum of all digits is divisible by 3, whole number is divisible by 3.
    # Test all digits from StartIndex to last index, not including the SkipIndex.

    while startIndex < listLength:
        sum = 0
        for i in range(startIndex, listLength):
            if i != skipIndex:
                sum += L[i]
        if sum % 3 == 0:
            pass

        startIndex += 1

    # If reach this point, no match was found. Return 0.
    return 0
