#example1
a = ' Jason '
b = ' Odeleye '

try:
    print("My first name is",a,"and my last name is",b,c)

except:
    print("c is not defined")

finally:
    print("TRY and EXCEPT statement executed")

#example2
age = int(input("Enter your age: "))
try:
    if age < 18:
        raise ValueError
    else:
        print("This age is valid")

except ValueError:
    print("This age is not valid")