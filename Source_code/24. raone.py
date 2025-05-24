"""
This module prints pattern according to the input given by the user.
"""

def pattern( num: int)-> None:
    """
    This function prints a pattern given number of times.
    :param num: integer number of times to print
    :return: None
    """
    for  i in range(1, num+1):
        print( "*" * i)

# using try-except to handle potential value-error from the user input
try:
    # Enter the number.
    a= int( input( "Enter the number of times you want the pattern:- "))
    # Print the pattern using the function pattern.
    pattern(a)
except ValueError as e:
    print(f"Error: {e}")