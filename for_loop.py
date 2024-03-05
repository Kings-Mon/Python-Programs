# Some Basic Uses of 'for' loop
# ========================================================================= #

for i in range(1, 10, 2):
    print(i)
print("Done!")

# ===================================== #

for i in range(5, 0, -1):
    print(i)
print('Done!')

# ===================================== #

for i in reversed(range(1, 6, 1)):
    print(i)
print('Done!')

# ========================================================================= #

#Sum #Subtract
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(f"Sum of the first {n} numbers is {sum}.")

# ========================================================================= #

# Name Print
name = "Kingshuk"
for c in name:
    print(c, end=' ')

# ========================================================================= #
    
name = "Kingshuk"
for c in name[::-1]:
    print(c, end=' ')

# ========================================================================= #

# Word Count
sentence = 'My name is Kingshuk, I am a Engineering Student.'
count = 0
for i in sentence.split():
    count += 1
print(f"There are {count} words in the sentence.")

# ========================================================================= #

# Name Print from List
cars = ['Audi', 'BMW', 'Toyota']
for i in range(len(cars)):
    print(cars[i])

# ===================================== #
    
cars = ['Audi', 'BMW', 'Toyota']
[print(car) for car in cars]

# ===================================== #

fav_languages = ['Python', 'Java', 'C', 'Ruby']
for language in fav_languages:
    if 'Python' == language:
        print("I like Python.")
        break
else:
    print("I don't like Python!")

# ========================================================================= #

# Printing Dictionary
course = {'name': 'Python', 'user': 'Kingshuk'}
for x in course:
    print(course[x])

# ===================================== #
    
course = {'Name': 'Python', 'User': 'Kingshuk'}
for a,b in course.items():
    print(a, b)

# ========================================================================= #
    
# Number Print
numbers = list(range(0, 100))
for number in numbers:
    if number > 50:
        break
    print(number, end=' ')

# ===================================== #
    
for i in range(5):
    if i == 2 or i == 4:
        continue
    print(i)

# ========================================================================= #

# Printing from given list
list1 = [1,2,3]
list2 = [4,5,6]

for x in list1:
    for y in list2:
        print(x, y)
    print( )

# ========================================================================= #
    
# Add of all Even numbers
total = 0
for i in range(1,101,1):
    if i % 2 == 0:
        total += i
print(total)

# ========================================================================= #

#char+10
name = 'Apple'
print (name)
for i in name:
    print(chr(ord(i)+10), end = '')

# ========================================================================= #
    
#Infinite for loop
items = [0]
for item in items:
    print(item)
    items.append(item)

# ========================================================================= #