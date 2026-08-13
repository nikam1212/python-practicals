feedback = input("Enter Your Feedback :") 

print(" customer feedback report ".upper().center(50))
print("----------------------------------------".center(50))


print("Original Feedback :".title())
print(feedback.center(50))

print("----------------------------------------".center(50))
print("feedback summary :".upper().center(50))

print("Total Characters :".len(feedback))
print(len(feedback.split()))
print(feedback.count(" "))
print(feedback.count("!"))

print(feedback)

print(feedback.lower())
print(feedback.upper())
print(feedback.title())
print(feedback.swapcase())
print(feedback.strip())
print(feedback.capitalize())