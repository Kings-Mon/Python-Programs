# This code will print numbers from 1 to n, but for multiples of 3, it will print "Fizz" instead of the number, and for multiples of 5, it will print "Buzz". For numbers that are multiples of both 3 and 5, it will print "FizzBuzz".

# ===================================================================================================================================================================================================================================== #

numbers = int(input("Enter the upper limit : "))
for number in range(1, numbers):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# ============================================================ #
        
# Alternate code:-
        
number = int(input("Enter the upper limit : "))
result = ['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(1, number)]
print('\n'.join(map(str, result)))

# ============================================================ #

# Another Alternate Version :- 

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

try:
    upper_limit = int(input("Enter the upper limit: "))
    fizzbuzz(upper_limit)
except ValueError:
    print("Please enter a valid integer.")

# ============================================================================================================================== #