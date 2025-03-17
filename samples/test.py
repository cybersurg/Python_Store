'''
word = "AliBinamhfodh"
for letter in word:
    print(letter, end="*")

'''

'''
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
'''
'''
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

'''

'''
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end=" ")

'''

'''

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, ":else")

print()


for i in range(0, 3):
    print(i)
else:
    print(i, "else")

'''

'''for i in range (1, 11):
    if i % 2 != 0:
        print(i)
        
'''

'''
x = 1
while x < 11:
    if x % 2 !=0:
        print(x)
    x += 1

'''

'''
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break

    print(ch, end="")

'''
'''
for digit in "0165031806510":

    if digit == "0":
        print("x", end="")
        # Line of code.
        continue
    print(digit, end="")
'''
'''

mlist = [3,1,-2]
print(mlist[mlist[-1]])
'''
'''
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c)
print(d)
print(e)
print(c + d + e)
'''
'''
alist = [[0,1,2,3] for i in range(2)]
print(alist[1][0])

'''
'''
var = 1
while var < 10:
    print("$")
    var = var << 1
'''
'''
#revers the list
vals = [0,1,2]
vals[0], vals[2] = vals[2], vals[0]
'''

'''
nums = [1,2,3]
vals = nums
del vals[1:2]
print("nums: ", nums)
print("vals: ", vals)
'''
'''
x = 1
x = x == x
print(x)
'''
'''
hlist_1 = [1,2, 3]
hlist_2 = []
for v in hlist_1:
    hlist_2.insert(0, v)
print(hlist_2)
'''
''''
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)'
'''
'''
t = [[3-i for i in range (3)] for j in  range (3)]
s = 0
for i in range(3):
    s += t [i][i]

print(s)
'''

'''
for i in range(1):
    print("#")
else:
    print("#")
'''

var = 0 
while var < 6:
    var += 1
    if var % 2 ==0:
        continue
    print("#")