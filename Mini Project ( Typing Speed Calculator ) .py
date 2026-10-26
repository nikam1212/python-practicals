
import time
import random

sentences = [
    "Python is a simple and powerful programming language.",
    "Practice makes a person perfect.",
    "Programming improves logical thinking and problem solving.",
    "Technology makes our daily life easier.",
    "Learning Python is fun and interesting."
]

print("===================================")
print("       TYPING SPEED TEST")
print("===================================")

sentence = random.choice(sentences)

print("\nType the following sentence:\n")
print(sentence)

input("\nPress Enter when you are ready to start...")

print("\nStart typing!")
start_time = time.time()

typed_text = input()

end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

if time_taken == 0:
    time_taken = 0.01

# Calculate typing speed
words = len(typed_text.split())
time_minutes = time_taken / 60
wpm = words / time_minutes

# Calculate accuracy
correct_chars = 0

for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_chars += 1

if len(sentence) > 0:
    accuracy = (correct_chars / len(sentence)) * 100
else:
    accuracy = 0

# Display results
print("\n========== RESULTS ==========")
print("Time taken:", round(time_taken, 2), "seconds")
print("Words typed:", words)
print("Typing speed:", round(wpm, 2), "WPM")
print("Accuracy:", round(accuracy, 2), "%")
print("Correct characters:", correct_chars)
print("Incorrect or missing characters:",
      max(len(sentence), len(typed_text)) - correct_chars)

if accuracy >= 90:
    print("Excellent typing!")
elif accuracy >= 70:
    print("Good job! Keep practicing.")
else:
    print("Keep practicing to improve.")

print("=============================")
