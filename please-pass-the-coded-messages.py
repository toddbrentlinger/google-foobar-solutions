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

Single output value with increasing list length:
[6] -> %3 [0] -> 0
6

[6,4] -> %3 [0,1] -> 1
6

[7,6,4] -> %3 [1,0,1] -> 2
6

[7,6,4,2] -> %3 [1,0,1,2] -> 4 % 3 = 1 
762

[7,6,4,1] -> %3 [1,0,1,1] -> 4 % 3 = 1 

[] -> [8,6,3,0] -> %3 [2,0,0,0]
630

[] -> [9,6,4,3,1] -> %3 [0,0,1,0,1]
963

- Create copy of list
- Sort copied list in descending order
- Create new list of remainder=value%3
- If sum of remainder list % 3 == 0, return all digits
- if " == 1
    - from least to greatest
        - If %3 == 1
            - Return all digits except current digit
- if " == 2
    - from least to greatest
        - If %3 == 2
            - Return all digits except current digit
    - 2 remainder values of 1 need to be omitted
    - from least to greatest
        - If 2 remainder values equal 1
            - Return all digits with 2 remainder values omitted
- If reach this point, return 0


96431 -> sum=23 remainder=sum % 3 = 2
9643- -> 23-1 % 3 != 0
964-1 -> 23-3 % 3 != 0
96-31
9-431 -> 23-6 % 3 != 0
-6431 -> 23-9 % 3 != 0

964-- -> 23-1-3 % 3 != 0
96-3- -> 23-1-4 % 3 == 0 Return 963
96--1
9-43-
9-4-1
9--31
_6431

- Test if all digits sum % 3 == 0
- If not, check if any single digit satisfies (from least to greatest)
- If not check if any two digits satisfies (from least to greatest)
- Continue until after checking for single digit

[] -> [7,4,4] -> %3 [1,1,1]
744

[] -> [7,4,4,3] -> %3 [1,1,1,0]
7443

[3,1,4,1] -> [4,3,1,1] -> %3 [1,0,1,1]
4311

[3,1,4,1,5,9] -> [9,5,4,3,1,1] -> %3 [0,2,1,0,1,1]
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

6 digits:
954311 = 23 % 3 = 2
If any digit % 3 == 2
    use all but that single digit since the rest
    should sum to value that is divisible by 3
5 % 3 == 2
Return 9-4311

5 digits:
95431- (skip '1')
954-11
95-311
9-4311
-54311

4 digits: 954311
9543--
954-1- *1
954--1 *1
95-31- *2
95-3-1 *2
9-431- *3
9-43-1 *3
9-4-11
9--311
-5431- *4
-543-1 *4
-54-11
-5-311
--4311
954311

95--11
954-1-
95-31-
9-431-
954311
9--311

3 digits:
9---11

2 digits:
9----1

1 digit:
9-----

"""

from copy import deepcopy

def solution(l):
    # Create deep copy of list sorted in descending order
    listCopy = deepcopy(l)
    listCopy.sort(reverse=True)

    # Sum all values and get remainder of 3
    remainderSum = 0
    for i in listCopy:
        remainderSum += i
    remainderSum %= 3

    # If remainder of sum of numbers is 0, all digits make up number divisible by 3.
    # If remainder is greater than 0, try to remove least number of digits with the lowest
    # value until remainder of sum of numbers if equal to zero.
    # Start finding any values whose remainder is max possible value (ex. for %3 max value is 2).
    # If still need to reduce sum of numbers further, decrement new remainder to compare (ex. from 2 to 1)
    # and find any values to remove.
    # Continue until remainder of sum of numbers is 0 OR no more possible numbers to remove.
    # Only need to check max (n-1) times, where n = divisible-by factor. Example: for %3, only need to find numbers 
    # with remainder 2 and then 1.

    # Initialize currRemainder to remainder needed to remove
    currRemainder = remainderSum
    while currRemainder > 0 and remainderSum > 0:
        # From right-left (min to max digit), find first instance of value % 3 == currRemainder
        for i in range(len(listCopy) - 1, -1, -1):
            if listCopy[i] % 3 == currRemainder:
                # Remove index
                del listCopy[i]
                # Subtract from remainderSum
                remainderSum -= currRemainder
                # Break out of for loop if remainderSum is less than currRemainder
                if remainderSum < currRemainder:
                    break
        # Decrement currRemainder
        currRemainder -= 1

    # Return 0 if there is still some leftover remainderSum
    # OR no digits to join (listCopy lenght is zero)
    if remainderSum > 0 or len(listCopy) == 0:
        return 0
    
    # Converts list of numbers -> list numbers as strings -> joined into single string -> converted to number
    return int(''.join(map(str, listCopy)))

def unit_test(list, expectedOutput):
    output = solution(list)
    if output != expectedOutput:
        print(f'Test Failed!:\nList: {list}\nExpected Output: {expectedOutput}\nOutput: {output}')
    else:
        print('Test Passed!')

if __name__ == '__main__':
    unit_test([6,3,9,1,4], 963) # 963
    unit_test([3,1,4,1,5,9], 94311) # 94311
    unit_test([3,1,4,1], 4311) # 4311
    unit_test([4,4,7,3], 7443) # 7443
    unit_test([4,7,4], 744) # 744
    unit_test([3,6], 63) # 63
    unit_test([2,6], 6) # 6
    unit_test([6], 6) # 6
    unit_test([2], 0) # 0 
    unit_test([], 0) # 0
    unit_test([9,9,9,9,9,9,9,9,9], 999999999)