t = str(input("Enter a word (any, but not shorter than 6 characters)): "))

while len(t) < 6:
    t = str(input("Please retype the word because it is too short: "))

mid = len(t) // 2
rez = t[4:mid:2]

print("The line after the cut:", rez)
