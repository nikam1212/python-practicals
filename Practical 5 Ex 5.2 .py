rows = 5
columns = 20

for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * columns)
    else:
        print("*" + " " * (columns - 2) + "*")
