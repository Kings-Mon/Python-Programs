#            -: Armstrong Number :-           #

# [ An Armstrong number (also known as a narcissistic number, pluperfect digit, or pluperfect number) is a number that is the sum of its own digits each raised to the power of the number of digits.]

# ===================================================================================================================================================================================================== #

# 1. Brute Force Approach :-

num = input("Enter your number : ")
sum = 0

for digit in range(len(num)):
    sum = int(num[digit])**len(num)

if (int(num) == sum):
    print("It's an Armstrong number.")
else:
    print("It's not an Armstrong number")

# ==================================================================== #

# 2. Using a Function :-
     
def is_armstrong_number(num):
    num_str = str(num)
    order = len(num_str)
    total_sum = sum(int(digit) ** order for digit in num_str)
    return total_sum == num

num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# ==================================================================== #
    
# 3. Using Recursion : -

def calculate_armstrong_sum(num_str, order, index):
    if index == len(num_str):
        return 0
    return int(num_str[index]) ** order + calculate_armstrong_sum(num_str, order, index + 1)

def is_armstrong_number(num):
    num_str = str(num)
    order = len(num_str)
    total_sum = calculate_armstrong_sum(num_str, order, 0)
    return total_sum == num

num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# ======================================================================= #