# Some Basic Uses of 'while' loop
# ========================================================================= #

while True:
    line = input("Enter a line (or press 'k'): ")
    if line == 'k':
        break
    print(line)

# ========================================================================= #

# Check if string is in the list or not
fruits = ['appels', 'banana', 'lichi', 'strawberry']
fruit_len = len(fruits)
index = 0

while index < fruit_len:
    if fruits[index] == 'orange':
        print("Orange is avilable.")
        break
    index += 1
else:
    print("Orange is not avilable!")

# =================================================== #

list1 = ['a','b','c']
list2 = [1,2,3]

i = 0
while i < len(list1):
    j = 0
    while j < len(list2):
        print(list1[i], list2[j])
        j += 1
    print( )
    i += 1
print('Done!')

# ========================================================================== #

# Infinite while Loop
item = 0
while True:
    print(item)

# =================================================== #

n = 100
while True:
    print(n)
    n -= 1

# ========================================================================== #