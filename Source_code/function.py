def func(num_1: int, num_2: int):
    num_3: int= num_1*num_2
    print(num_3)
    print(f"running file status is, {__name__}")

if __name__== "__main__":
    func(4, 5)
    print("This is form function file.")