# Leap Year
# =========================================================================== #

year = int(input("Enter an year : "))

if year <= 0:
    print("Invalid Year!")
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's a Leap Year.")
else:
    print("It's not a Leap Year.")

# ===================================== #

# Alternative Way,
year = int(input("Enter an year : "))

if year <= 0:
    print("Invalid Year!")
elif year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            ("Not a Leap Year.")
    else: 
        print("Leap Year.")
else:
    print("Not a Leap Year.")

# =========================================================================== #