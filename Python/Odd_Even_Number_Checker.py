def odd_even(x): #Made a function called 'odd_even'
    while True:
        try:  #used try/except so that the code doesn't blow up but rather continues working
            x= int(x)
            break
        except ValueError:  #ValueError Class
            print('Error, Please put a number ')
            break
    y = x%2
    if y==0:
        print("The number ",x," you entered is Even")
    else:
        print("The number ",x," you entered is Odd")

z = input("Do you want to use it ? Y/N")
if z == 'Y':
    while True:
        x=input("Please enter your number to check if it is odd or even : ")
        odd_even(x)
elif z == 'N':
    print("Thank You!")
    quit
else:
    print("Please select Y/N") #CodeByPadmanabh
