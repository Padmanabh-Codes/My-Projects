x = None
while True:
    def farhenite(n):
        F = ((n*9)/5 + 32)
        print(F)
    def celcius(n):
        C = ((n-32)*5)/9
        print(C)
    try:
        x=int(input('Do You want to convert Celcius to Farhenite? or Farhenite to Celcius? press 1 or 2 respectively.' \
    'If you want to exit, press 0. '))
    except ValueError:
        print("Please enter a number")
        continue
    if x==1:
        n = input('Please Enter a number: ')
        try:
            n=int(n)
            farhenite(n)
            continue
        except ValueError:
            print("Please enter a number properly: ")
            continue
    elif x==2:
        n = input('Please enter a number: ')
        try:
            n = int(n)
            celcius(n)
            continue
        except:
            print("please enter a number properly: ")
            continue
    elif x==0:
        print("Thanks for using!")
        break
    else:
        print("Please enter a number from the given options")
