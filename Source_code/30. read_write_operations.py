f= open("Real.txt", "w")
f.write("This is the right thing to do.")
f.close()
f= open("Real.txt", "a")
f.write("\nIs this the right thing to do?")
f.close()
f= open("Real.txt", "r")
a= f.read()
print(a)
f.close()
f= open("Real.txt", "r")
for line in f:
    print(line)
f.close()
f= open("Real.txt", "r")
words= 0
for line in f:
    token= line.split(" ")
    print(f"The total no. of words are {len(token)} and the line is {line}")
    print(f"and the token is {token}")
    words= words+ len(token)
print(f"\nTotal no. of words in Real.txt file is {words}.")
f.close()
with open("Real.txt", "r") as f:
    print (f.readlines())

print(f.closed)