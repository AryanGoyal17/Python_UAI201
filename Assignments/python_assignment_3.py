#q1

list_q1 = [123, "python", 3.7]
print(list_q1, end = "\n\n")

#q2

list_q2 = []

int_input = input()
list_q2_elem = int_input.split()

for i in list_q2_elem:
    list_q2.append(int(i))

print(list_q2, end = "\n\n")

#q3

list_q3 = ["Physics", "C", "ED", "Manpro", "Chemistry"]

for i in list_q3:
    print(i)

print("\n")

#q4

list_q4 = ["banana", "apple", "mango", "tomato", "berry"]
print(list_q4[0])
print(list_q4[2], end = "\n\n")

#q5

print(list_q4[-1], end = "\n\n")

#q6

list_q6 = []

input_q6 = input()
list_q6_elem = input_q6.split()

for i in list_q6_elem:
    list_q6.append(i)

print("First:", list_q6[0])
print("Last:", list_q6[-1], end = "\n\n")

#q7

print(list_q4[1:3], end = "\n\n")

#q8

print(list_q4[-3:], end = "\n\n")

#q9

list_q9 = []

input_q9 = input()
list_q9_elem = input_q9.split()

for i in list_q9_elem:
    list_q9.append(i)

print(list_q9[2:], end = "\n\n")

#q10

list_q10_a = [1,2,3]
list_q10_b = ["python", "c"]

print(list_q10_a + list_q10_b, end = "\n\n")

#q11

list_q11 = [1,2,3]
print(list_q11 * 2, end = "\n\n")

#q12

list_q12_a = []
list_q12_b = []

input_a = input("List1: ")
input_b = input("List2: ")

list_q12_elem1 = input_a.split()
list_q12_elem2 = input_b.split()

for i in list_q12_elem1:
    list_q12_a.append(i)

for i in list_q12_elem2:
    list_q12_b.append(i)

print(list_q12_a + list_q12_b, end = "\n\n")

#q13

list_q13 = ['python', 'c', 'java', 'php']
print('cpp' in list_q13, end = "\n\n")

#q14

list_q14 = [1, 2, 3, 4, 5]
print(6 not in list_q14, end = "\n\n")

# q15


