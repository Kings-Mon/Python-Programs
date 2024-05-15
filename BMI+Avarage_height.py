# Body Mass Index (BMI) :-
# ======================================================================================= #

weight = input('Enter weight in Kg: ')
height = input('Enter height in meter: ')

bmi = int(weight) / float(height) ** 2

print(f'Body Mass Index = {int(bmi)}')

weight = float(input('Enter weight in Kg: '))
height = float(input('Enter height in meter: '))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f'Body Mass Index (BMI) is {bmi} and you are Underweight.')
elif bmi < 25:
    print(f'Body Mass Index (BMI) is {bmi} and you have a Normal Weight.')
elif bmi < 30:
    print(f'Body Mass Index (BMI) is {bmi} and you are Overweight.')
elif bmi < 35:
    print(f'Body Mass Index (BMI) is {bmi} and you are Obese.')
else:
    print(f'Body Mass Index (BMI) is {bmi} and you are Crinically Obese.')

# ======================================================================================= #
# Avarage Height
    
height = input("Enter all heights in cm (space seperated) : ")
height_list = height.split()

count = 0
for height in height_list:
    count += 1
print(f"Total {count} heights provided.")

for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for person in height_list:
    total += person

average = total / count
print(f"Average of the heights : {average}cm\nRound off. - {round(average)}cm")

# ======================================================================================= #