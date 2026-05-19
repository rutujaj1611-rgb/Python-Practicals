t = (10, 20, 30, 40, 50)

print("Tuple:", t)

# Slicing
print("t[1:4] =", t[1:4])
print("t[:3] =", t[:3])
print("t[2:] =", t[2:])
print("t[-3:] =", t[-3:])
print("t[::-1] =", t[::-1])   # Reverse

#Tuple methods
t2 = (1, 2, 2, 3, 2)

# count()
print("Count of 2:", t2.count(2))

# index()
t3 = (10, 20, 30, 40)
print("Index of 30:", t3.index(30))