string = "Python programming is the best course to learn"
a = len(string)
print("The length of string is", a)
print(f"{string[0:5]}")
print(f"{string[-10:-1]}")
b=string.replace("Python","DUT")
print(b)
print(string.index("best"))
print(string.isupper())
print(string.replace('', ' ').split())