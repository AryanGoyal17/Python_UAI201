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




