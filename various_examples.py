# Various types of exercies examples
# ========================================================================= #

#Swap two numbers
a = input("Enter value of a = ")
b = input("Enter value of b = ")

temp = a
a = b
b = temp

print("a = ", a)
print("b = ", b)

# ========================================================================= #

# Sum of the Number
num = input("Enter a number: ")

total_sum = 0
for digit in num:
    total_sum += int(digit)

print(f"Sum of the digits is: {total_sum}")

# ========================================================================= #

# Life Span
age = int(input("Enter your age : "))

years_left = 100 - age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left, if you live 100 years.")

# ========================================================================= #

# Virtual Toss
import random

side = random.randint(0,1)
print(side)

if side == 1:
    print("Head!")
else:
    print("Tail!")

# ========================================================================= #
    
# Who will pay the bill?
import random

name = input("Enter everybody's name sepereated by comma: ")
names_list = name.split(",")
print(names_list)
#length = len(names_list)
#random_choice = random.randint(0, length-1)
selected_selected = random.choice(names_list)
print(f"{selected_selected} will pay the bill.")
#Kingshuk,Somyadip,Debarun,Souragnik

# ========================================================================= #

# Enter an element in a matrix
row1 = ['😏', '😏', '😏']
row2 = ['😎', '😎', '😎']
row3 = ['🥱', '🥱', '🥱']
matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Enter the position where you want to hide (Eg-23): ")
if len(position) == 2 and position.isdigit():
    row_num = int(position[0]) - 1
    column_num = int(position[1]) - 1

    if 0 <= row_num < len(matrix) and 0 <= column_num < len(matrix[0]):
        row_selected = matrix[row_num]
        row_selected[column_num] = 'X'
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid position.")
else:
    print("Invalid input. Please enter a valid position.")

# ========================================================================= #
    
# Maximum Number in a list
numbers = input("Enter the numbers seperated by space : ")
num_list = numbers.split()

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

max_number = num_list[0]
for num in num_list:
    if num > max_number:
        max_number = num
print(f"The Maximum number is : {max_number}")

# ========================================================================= #