class Employee:
    def __init__(self, char_1, str_1):
        self.id= char_1
        self.name= str_1
    def display(self):
        print(self.id)
        print(self.name)

emp = Employee(1, "programmer")
emp.display()

del emp.id
try:
    print(emp.id)
except AttributeError as a:
    print(f"Error: {a}- AttributeError")
except Exception as x:
    print(f"Error: {x}")

del emp
try:
    emp.display()
except NameError as b:
    print(f"Error: {b}- NameError")
except Exception as x:
    print(f"Error: {x}")

