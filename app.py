print("hello world")
 
age = 20
age = 50
price = 19.6
first_name = "Sayem"
is_online = False
print(age)

name = input("What is your name?  ")
print("Hello  "  + name)

birth_year = input("enter your birth year: ")
age = 2022 - int(birth_year)
print(age)

int()
float()
bool()
str()

first = input("First: ")
second = input("Second: ")
sum = int(first) + int(second)
print(sum)

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("sum: " + str(sum))

course = "python for beginners"
print(course.upper())
print(course)

course = "python for beginners"
print(course.find ("y"))

course = 'python for beginners'
print(course.replace('for', '4'))
course = 'python for beginners'
print(course.replace('x' , '4'))

course = 'python for beginners'
print('python' in course)

#Arithmetic oparation

print(10+3)
print(10-3)
print(10*3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x +  3
x += 3
x -= 3
x *= 3

#oparator precedence
x =(10 + 3) * 2
print(x)

#comparison operators
x = 3 > 2
print(x)
x = 3 >= 2 
print(x)
x = 3 < 2
print(x)
x = 3 <= 2
print(x)
x = 3 == 2
print(x)
x = 3 != 2 
print(x)

# Logical operators
price = 25
print(price > 10 and price < 30) # and (both)
price = 5
print(price > 10 or price <30) # or [at least one]
price = 5
print(not price > 10)  # not [any value we give it]

# If Statement 
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # [20,30]
    print("It's a nice day")
elif temperature > 10: # [10,20]
    print("It's a bit cold day")
else:
    print("It's cold")
    print("Done")

weight = int(input("weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "k":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs: " + str(converted))

# While loops
 
i = 1 
while i <= 10:
    print(i * '*')
    i = i + 1

# Lists

names = ["Jhon", "Bob","Mosh","Sam" ,"Mary" ]
print(names)
print(names[2])
print(names[-3])
names[1] = "Jon"
print(names[0:3])

# List Methods

numbers = [1,2,3,4,5,6,7]
numbers.append(7)
print(numbers)

numbers = [1,2,3,4,5,6,7]
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)

numbers = [1,2,3,4,5,6,7]
print( 1 in numbers)
print(10 in numbers)
print(len(numbers))

# For Loops;52 min

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)


i = 0 
while i < len(numbers):
    print(numbers[i])
    i = i + 1


# The range() Function 

numbers = range(5 ,10,2)
for number in range(5):
    print(number)

# Tupels
numbers = (1,2,3,4,5,5)
print(numbers)


    























