#                    -:  Fibonacci Series  :-

# [ The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. ]
# ======================================================================================================================================================================================================= #

terms = int(input("Enter the the number of terms: "))
n1, n2 = 0, 1

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(f"Fibonacci Sequence: \n {n1}")
else:
    for term in range(terms):
        print(n1, end=' ')
        n = n1 + n2
        n1 = n2
        n2 = n
    print('')

# ======================================================================================= #

# Alternate Code :-
def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = fibonacci(terms)
print("Fibonacci Sequence: ")
print(result)

# ======================================================================================= #

# Alternatively, 
def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = fibonacci_recursive(terms)
print("Fibonacci Sequence:")
print(result)

# =========================================================================================== #