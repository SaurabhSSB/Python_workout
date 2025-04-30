try:
    num_1= int(input("Enter the first number:- "))
    num_2= input("Enter the second number:- ")
    num_3= num_1 * int(num_2)
    print(num_3)
    if(num_1< 10):
        num_4= num_1 + num_2
        print(num_4)
except TypeError as a:
    print(f"{a}- TypeError")
except ZeroDivisionError as b:
    print(f"{b}- ZeroDivisionError")
except ValueError as c:
    print(f"{c}- ValueError")
except Exception as x:
    print(f"Error: {x}")
finally:
    print("Program executed successfully.")