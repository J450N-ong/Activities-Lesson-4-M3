try:
    num1,num2 = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1 / num2
    print("Result is",result)

except ZeroDivisionError:
    print("Division between zero is not possible")

except SyntaxError:
    print("Comma was missing between the two numbers")

except:
    print("Wrong input")

finally:
    print("Multiple Except Statements executed")