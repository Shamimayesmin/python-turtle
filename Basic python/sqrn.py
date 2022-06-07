
while True:
    n = input("enter a positive number: ")
    n = int(n)
    if n < 0:
        print('we only allow positive number. plese try again. ')
        continue
    if n == 0:
        break
    print("square of" ,n,'is', n*n )

