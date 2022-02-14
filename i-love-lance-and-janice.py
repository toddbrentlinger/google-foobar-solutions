"""
Letter ASCII
a 97
m 109
z 122

a z 97 122 +25
b y 98 121 +23 = 25 - 2*('b'-'a')
c x 99 120 +21 = 25 - 2*('c'-'a')
...
k p 107 112 +5
l o 108 111 +3 = 25 - 2*('l'-'a') = 25-2*11 = 3
m n 109 110 +1 = 25 - 2*('m'-'a') = 25-2*12 = 1
n m 110 109 -1 = 25 - 2*('n'-'a') = 25-2*13 = -1
o l         -3
p k         -5
...
x c         -21
y b         -23 = 25 - 2*('y'-'a') = 25-2*24 = -23
z a         -25

Simplification:
   25    - 2*(X - 'a')
'z'-'a'  - 2*(X - 'a')
z  - a   - 2X + 2a
z  + a   - 2X
"""

def iLoveLanceAndJanice(s):
    convertedStr = ''
    
    for c in s:
        # ASCII code for current char in string list
        currCharCode = ord(c)
        # If current char within 'a'-'z'
        if currCharCode >= 97 and currCharCode <= 122:
            # Change ASCII code
            currCharCode += 25 - 2 * (currCharCode - 97)
            # Add char with new ASCII code
            convertedStr += chr(currCharCode)
        else: # Else add char unchanged
            convertedStr += c
    
    return convertedStr

def iLoveLanceAndJanice01(s):
    aCode = ord('a') # 97
    zCode = ord('z') # 122
    convertedStr = ''

    for c in s:
        # ASCII code for current char in string list
        currCharCode = ord(c)
        # If current char within 'a'-'z'
        if currCharCode >= aCode and currCharCode <= zCode:
            # Change ASCII code
            currCharCode += 25 - 2 * (currCharCode - aCode)
            # Add char with new ASCII code
            convertedStr += chr(currCharCode)
        else: # Else add char unchanged
            convertedStr += c
    
    return convertedStr

if __name__ == '__main__':
    print(iLoveLanceAndJanice('vmxibkgrlm'))