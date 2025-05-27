d_1= {"a": 123, "b": 456, "c": 789}
print(dict["a"])

for key in d_1:
    print(f"Key: {key}, Value: {d_1[key]}")

for x,y in d_1.items():
    print(f"Key: {x}, Value: {y}")

s= "a" in d_1
print(s)

d_1["d"]= 101112
del d_1["b"]
print (d_1)

d_1.clear()
print(d_1)