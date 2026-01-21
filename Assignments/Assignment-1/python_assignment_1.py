#q1

def q1(num_chocolate, num_children):
  result = num_chocolate // num_children
  remainder = num_chocolate % num_children
  return(["No of chocolates distributed to each child: " + str(result), "No of chocolates left: " + str(remainder)])


answer = q1(48,6)
print(answer)

#q2

def average(m1, m2, m3):
  average = ((m1+m2+m3)/3)
  return average

result = average(72, 81, 69)
print("Average marks: ", result)

#q3

def calc(num):
  square = num**2
  cube = num**3
  return(["Square: " + str(square), "Cube: " + str(cube)])


num = float(input("Enter a number: "))
result = calc(num)
print(result)

#q4

def add(bill):
  total = sum(bill)
  return total

list1 = [245, 315, 180]
answer = add(list1)
print("Total bill amount: ", answer)

#q5

def convert_time(video_length):
  hours = video_length // 60
  minutes = video_length % 60
  return([str(hours) + "hours", str(minutes) + "minutes"])

time = convert_time(185)
print(time)

#q6

def salary_inc(salary):
  new_salary = 1.1 * salary
  return new_salary

salary_final = salary_inc(32000)
print("Salary after increment: ", salary_final)

#q7

def distance(speed, time):
  total_distance = speed * time
  return total_distance

result = distance(60, 2.5)
print("Total distance travelled: ", result, "km")

#q8

def calc(num_pens, num_pen_eachbox):
  num_box = num_pens // num_pen_eachbox
  pens_left = num_pens % num_pen_eachbox
  return(["No of full boxes: " + str(num_box), "No of pens left unpacked: " + str(pens_left)])

answer =  calc(145, 12)
print(answer)

#q9

def convert_temp(temp):
  t_f = (((9*temp) / 5) + 32)
  return t_f

temp_f = convert_temp(30)
print("30°C = ", temp_f, end = "°F\n")

#q10

def calc(cost_per_unit, num_unit):
  total = cost_per_unit * num_unit
  return total

answer = calc(6, 275)
print("Total bill amount: ₹" + str(answer))

#q11

def convert(road_len):
  road_len_km = road_len // 1000
  road_len_rem = road_len % 1000
  return (["The length of the road is " + str(road_len_km) + "km " + str(road_len_rem) + "m"])

result = convert(3750)
print(result)

#q12

def SI(p,t,r):
  simple_int = ((p*t*r) / 100)
  return simple_int

result = SI(8000, 2, 5)
# print("The simple interest is ₹", result) .. A space comes after rupee symbol in the print statement written with this comment!!
print("The simple interest is ₹" + str(result))

#q13

def calc(dist_total, time_total):
  avg_speed = dist_total / time_total
  return avg_speed

result = calc(120,3)
print("Average speed: " + str(result) + "km/hr")

#q14

def percent(marks_obt, total_marks):
  percent_obt = ((marks_obt / total_marks) * 100)
  return percent_obt

marks_percent = percent(412,500)
print("Percentage obtained: " + str(marks_percent) + "%")


#The round function-- can be used to round-off the percentage..--
#print("Percentage obtained: " + str(round(marks_percent, 2)))
#By using the round function-- output is 82.4%

#q15

def calc(num_pages, num_page_per_day):
  num_days_req = num_pages // num_page_per_day
  pages_left = num_pages % num_page_per_day

  return(["Number of days required: " + str(num_days_req), "Number of pages left on last day: " + str(pages_left)])

answer = calc(240, 18)
print(answer)

#q16

def convert(amount_dollar):
  amount_rupee = amount_dollar * 83
  return amount_rupee

final_amount = convert(125)
print("125$ = " + "₹" + str(final_amount))

#q17

def calc(num_toys_total, num_days):
  num_toys_per_day = num_toys_total // num_days
  num_toys_left = num_toys_total % num_days
  return(["Toys produced per day: " + str(num_toys_per_day), "Extra toys left: " + str(num_toys_left)])

answer = calc(950, 7)
print(answer)

#q18

def calc(num):
  result = num ** 4
  return(str(num) + "^4 = " + str(result))

answer = calc(5)
print(answer)

#q19

def convert_sec(num_hours, num_minutes):
  num_sec1 = num_hours * 3600
  num_sec2 = num_minutes * 60
  result = num_sec1 + num_sec2
  return("Total time = " + str(result) + "seconds")

answer = convert_sec(2, 45)
print(answer)

#q20

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result1 = num1 / num2
result2 = num1 // num2

print(str(num1) + "/" + str(num2) + "=" + str(result1))
print(str(num1) + "//" + str(num2) + "=" + str(result2))
print("Type of result1(division) =", type(result1))
print("Type of result2(floor division) =", type(result2))

#Floor division of 2 integers -- type is int
#Floor division of 1float,1int or 2 float -- type is float..
#Since here while taking input, number is typecasted to become float... the output for both type-fn comes float

#If both input typecasted as int.. then type of result2(floor division becomes --- int!)

#Note-- dont use list as a variable name.. as it is a keyword.
#Note-- if you use end with print statement then add a \n ... otherwise output of next question(here happened between q9 and q10) would come in same line..