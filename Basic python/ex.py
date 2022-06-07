number = input ("type a integer number and press enter: ")
number = int(number)

if number >= 0:
    print(number, "is a positive")
else:
    print(number,"is a negative number")

print("program terminated")

# Compare number
n1 = 20 
n2 = 30
n3 = 25

if n1 > n2:
    max_n = n1 
else:
    max_n = n2
if n3 > max_n:
    max_n = n3

print("Maximum :" , max_n)

n1 = 50
n2 = 60
n3 = 65

if n1 < n2:
    max_n = n1
else:
    max_n = n2
if n3 > max_n:
    max_n = n3
    

print("Maximun: " , max_n)

# Leap Year

year = int(input("Enter a year: "))
if year % 4 == 0 and  year % 100 != 0: 
    print(year ,"is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(year,"is a leap year") 
else:
    print(year,"is not a leap year")
    




    


    




