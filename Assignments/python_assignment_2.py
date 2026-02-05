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
#Maximum of three numbers

def q11(num1, num2, num3):

    if(num1 >= num2 and num1 >= num3):
        return num1
    
    elif(num2 >= num3 and num2 >= num1):
        return num2

    else:
        return num3


number_q11_1 = float(input("Enter the first number: "))
number_q11_2 = float(input("Enter the second number: "))
number_q11_3 = float(input("Enter the third number: "))

print("Maximum of the 3 numbers entered by you is: ", q11(number_q11_1, number_q11_2, number_q11_3), end = "\n\n")

#q12
#Grade calculator using if-elif

def q12(marks):

    if(marks >= 90 and marks <= 100):
        return 'A'
    
    elif(marks >=75 and marks < 90):
        return 'A-'
    
    elif(marks >= 65 and marks < 75):
        return 'B'
    
    elif(marks >= 50 and marks < 65):
        return 'B-'
    
    elif(marks >= 30 and marks < 50):
        return 'C'
    
    elif(marks < 30 and marks >= 0):
        return 'F'
    
    else:
        return "Invalid marks entered!!"

marks = float(input("Enter marks obtained by you in a subject: "))

print("Grade obtained by you is:", q12(marks), end = "\n\n")

#q13
#Multiplication Table

def q13(num):

    k = 10

    for i in range(1, k + 1):
        print(num, "*", i, "=", num*i)


number_q13 = int(input("Enter an integer whose multiplication table you want: "))

q13(number_q13)

print("\n")

#q14
#Factorial using while

def q14(num_q14):

    i = 1
    result = 1

    while(i <= num_q14):

        result *= i
        i += 1
    
    return result

number_q14 = int(input("Enter the number whose factorial you want: "))

print("Factorial of", number_q14, ":", q14(number_q14), end = "\n\n")


#q15(IMPORTANT)
#Count digits of a number

import itertools

def q15(num_q15):

    num_digit = 0

    num_q15 = abs(num_q15) #This line makes the code work for negative integers as well


    for i in itertools.count(1):

        if(num_q15 % (10 ** i) == num_q15):

            num_digit = i
            break

#I wanted to make a loop which starts at 1 and then goes on till infinity until break condition is satisfied... the above loop didnt work
#So now i tried to find ways online to make such a loop.. which gave me the idea to use use the itertools library
#itertools.count function helps to create a infinite counter in a loop starting from 1 till infinity until break condition is satisfied..

    return num_digit

number_q15 = int(input("Enter a number: "))

print("Number of digits in the number:", q15(number_q15))

#Method-2 for question_15 (better than method-1)

def q15_M2(num_q15_M2):

    num_Digit_M2 = 1

    num_q15_M2 = abs(num_q15_M2)

    while(num_q15_M2 // 10 != 0):

        num_q15_M2 //= 10
        num_Digit_M2 += 1
    
    return num_Digit_M2

number_q15_m2 = int(input("Enter a number: "))

print("No. of digits:", q15_M2(number_q15_m2), end = "\n\n")

#Method-3(More simple than M1,M2)

#q16
#Reverse a number

#q17
#Prime number check

def q17(num_q17):

    if(num_q17 == 1 or num_q17 == 0):
        return "is NOT a prime number "

    elif(num_q17 == 2):
        return "is a prime number"
    
    for i in range(2, num_q17):

        if(num_q17 % i == 0):
            return "is NOT a prime number"

        else:
            if(i == (num_q17 - 1)):
                return "is a prime number"

            else:
                continue


number_q17 = int(input("Enter a number: "))
print(number_q17, q17(number_q17), end = "\n\n")


#q18
#Search element using for-else

list_q18 = [10,20,30,40,50,60]

num_search = int(input("Enter the number you want to search for in the list: "))

for i in list_q18:
    

    if i == num_search:

        position = list_q18.index(i) + 1
        print(num_search, "was found at position =", position, "in the list", end = "\n\n")
        break

else:
    print(num_search, "was not found in the list!!", end = "\n\n")

#Code for q18 can be improved by using enumerate instead of index fn for list
        
        




    




        

















