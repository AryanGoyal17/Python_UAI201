#q1

def q1(num):

    if(num > 0):
        return "Positive"
    
    elif(num < 0):
        return "Negative"
    
    else:
        return "Neither positive nor negative(Number = 0)"
    

number = float(input("Enter a number: "))

print("Number entered by you is", q1(number), end = "\n\n")

#q2

def q2(age):

    if(age >= 18):
        return "Eligible to vote"
    
    else:
        return "NOT eligible to vote"

age = int(input("Enter your age: "))

print("You are", q2(age), end = "\n\n")

#q3

def q3(num1, num2):
    
    if(num1 > num2):
        return num1
    
    elif(num1 < num2):
        return num2

    else:
        return "Both the numbers are equal"

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Maximum of", number1, "and", number2, ":", q3(number1, number2), end = "\n\n")

#q4

def q4(num):
    
    if(num % 2 == 0):
        return "Even"
    
    else:
        return "Odd"

number = int(input("Enter a number: "))

print(number, "is", q4(number), end = "\n\n")

#q5

#Printing 1 to n using for loop

n_q5 = int(input("Enter n: "))

for i in range(1, n_q5 + 1):
    print(i, end = " ")

print("\n")

#q6

#Printing 1 to n using while loop

n_q6 = int(input("Enter n: "))

i = 1

while(i <= n_q6):
    print(i, end = " ")
    # i++ (this doesnt exist in python)
    i += 1

print("\n")

#q7

#Sum of first n natural numbers

n_q7 = int(input("Enter n: "))

sum = 0

for i in range(1, n_q7 + 1):
    sum += i
    i += 1

print("Sum of first", n_q7, "natural numbers:", sum, end = "\n\n")

#q8

#Skip character 'h' using continue

string = input("Enter a string: ")

for i in string:

    if(i == 'h'):
        continue

    print(i, end = " ")

print('\n')

#q9

#Stop printing at 3 using break

n_q9 = int(input("Enter n: "))

for i in range(1, n_q9 + 1):

    if(i == 3):
        break

    print(i, end = " ")

print("\n")

#q10

#Print weekday using match-case

day_number = int(input("Enter the number of weekday: "))

match day_number:

    case 1:
        print("Day-1: Monday", end = "\n\n")
    
    case 2:
        print("Day-2: Tuesday", end = "\n\n")

    case 3:
        print("Day-3: Wednesday", end = "\n\n")

    case 4:
        print("Day-4: Thursday", end = "\n\n")

    case 5:
        print("Day-5: Friday", end = "\n\n")

    case 6:
        print("Day-6: Saturday", end = "\n\n")

    case 7:
        print("Day-7: Sunday", end = "\n\n")

    case _:
        print("Invalid day number entered!!", end = "\n\n")

#q11









