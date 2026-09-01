text = input("Enter feedback: ")

words = ["bad", "hate", "angry"]

for word in words:
    text = text.replace(word, "****")

print("Filtered feedback:", text)

