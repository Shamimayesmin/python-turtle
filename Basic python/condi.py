print("hello  from my side")
print("this is shamima")
a = 5
b = 6
result = a+b
print(a+b)

my_money = 30 
rickshaw_fare = 40
my_money >= rickshaw_fare

a = 5 
b = 3
c = a-b
print(c)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[1])
print(numbers[9])
print(numbers[4])

today = "Tuesday"
today == "Tuesday"

saarc = ["Bangladesh","India","Afganistan","Butan","Nepal","Pakistan","Sri Lanka"]
print(saarc)
print(saarc[3])
print(saarc[0])
print("number of countries in SAARC: ", len(saarc))

saarc = ["Bangladesh","Afganistan","Butan","Nepal","India","Pakistan","Sri Lanka"]  
country = input("enter the name of the country: ")
if country in saarc:
    print(country, "is a member of SAARC")
    print("program terminated")

saarc = ["Bangladesh","Afganistan","Butan","Nepal","India","Pakistan","Sri Lanka"]  
country = input("enter the name of the country: ")
if country in saarc:
    print(country, "is a member of SAARC")
else:
    print(country, "is not a member of SAARC")

    print("program terminated")

marks =input("please enter your marks:  ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "F"
print("your grade is", grade)




