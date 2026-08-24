subject1 = float(input("Enter marks for Subject 1: "))

subject2 = float(input("Enter marks for Subject 2: "))

subject3 = float(input("Enter marks for Subject 3: "))


total = subject1 + subject2 + subject3

average = total / 3


print("\n===== STUDENT SCORECARD =====")

print("Subject 1: ", f"{subject1:.2f}")

print("Subject 2: ", f"{subject2:.2f}")

print("Subject 3: ", f"{subject3:.2f}")

print("-----------------------------")

print("Total Marks: ", f"{total:.2f}")

print("Average: ", f"{average:.2f}")

print("=============================")