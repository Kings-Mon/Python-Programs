# L O V E   C A L C U L A T E R

'''This script takes two names as input, converts them to lowercase, counts the occurrences of letters in the phrase "true love" within the combined name, and calculates a compatibility score. Finally, it prints out the score.
### Keep in mind this is just a fun and simplistic implementation and does not reflect any actual scientific measure of love compatibility. '''

# ================================================================================================================================================================================================================================= # 

name1 = input("Type your name - ")
name2 = input("Type his/her name - ")

combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))

if 10 > love_score > 90:
    print(f"Your love score is {love_score} and you go together like coke and mentos!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score} and your are alright together.")
else:
    print(f"Your love score is {love_score}")

# ======================================================================================================= #
    
# Another Approach :-
    
def calculate_love(name1, name2):
    combined_name = (name1 + name2).lower()
    total = 0

    # Count occurrences of letters in 'true love'
    true_love = "true love"
    for letter in true_love:
        total += combined_name.count(letter)

    # Calculating compatibility score
    score = total % 101

    return score

def main():
    print("Welcome to the Love Calculator!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    love_score = calculate_love(name1, name2)
    print(f"The love compatibility between {name1} and {name2} is {love_score}%.")

if __name__ == "__main__":
    main()

# ======================================================================================================================== #