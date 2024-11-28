print("Enter 'c' to convert from celsius to Fahrenheit")
print("Enter 'f' to convert from Fahrenheit to Celsius")
choice=input("enter your choice:")
if choice=='c':
    celsius=float(input("Enter Temperature in Celsius:"))
    fahrenheit=(celsius*9/5)+32
    print('%.2f Celsius is:%0.2f Fahrenheit' %(celsius,fahrenheit))
elif choice=='f':
    fahrenheit=float(input("Enter Temperature in Fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print('%.2f fahrenheit is:%0.2f celsius' %(fahrenheit,celsius))
else:
    print('Invalid Input')
    
