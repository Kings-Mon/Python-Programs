# Some Basic Uses of 'if-else' statements :-
# ========================================================================================== #

# Check if x is < or > some digit
x = 10 
if x < 50:
    print("x is less than 50.")

# ===================================== #
    
x = 10 
if x < 50:
    print("x is less than 50.")
print("End the program.")

# ===================================== #

x = 10 
if x < 50: print("x is less than 50.")

# ===================================== #

x = 10
if x < 50: 
    if x == 10:
        print("x is equal to 10")
    print("x is less than 50")
print("End of the program.")

# ===================================== #

x = 0
if x == 5:
    print("x equals to 5.")
elif x > 5:
    print("x is less than 5!")
else:
    print("x is greater than 5!")
print("Done!")

# ========================================================================= #

# Can you vote?
age = 20
if age < 18:
    print("You can't vote!")
else:
    print("You can vote!")
print("Done!!")

# Alternatively, 

age = 15
print("You can't vote!") if age < 18 else print("You can vote!")
print("Okey!!")

# ========================================================================= #

#Odd / Even
numbers = int(input("Enter a number : "))
if numbers == 0:
    print("Zero can be Odd or Even.")
elif numbers % 2 == 0:
    print("It is an Even Number.")
else:
    print("It is an Odd Number.")

# ========================================================================= #

# Divisible by 2 or 3 
x = int(input("Enter the value of x: "))
if x % 2 == 0 & x % 3 == 0:
    print("x is divisible by 2 and 3.")
elif x % 2 == 0:
    print("x is divisible by 2.")
elif x % 3 == 0:
    print("is divisible by 3.")
else:
    print("x is not divisible by 2 or 3!")
print("Done!")

# ========================================================================= #

# Eligibility for an Exam
age = 32
nationality = "Indian"
if age > 18 and age < 30 and nationality == "Indian":
    print("You are eligible for the exam.")
else:
    print("You are not eligible!")

# ===================================== #

age = 25
nationality = "American"
if age > 18 and age < 30 and nationality == "Indian":
    print("You are eligible for the exam. Exam fee is 1500.")
elif age > 18 and age < 30 and nationality == "American":
    print("You are eligible for the exam. Exam fee is $50.")
else:
    print("You are not eligible!")

# ========================================================================= #

# True / False
x = True
if not x:
    print("x is False")
else:
    print("x is True")

# ===================================== #
    
# Uses of 'f' string 
name = 'King'
if not name:
    print("No name.")
else:
    print(f"The name is {name}.")

# ===================================== #
    
names = ['King','Queen','Prince']
if not names:
    print("No name.")
else:
    print(f"There are total {len(names)} names.")

# ========================================================================= #
