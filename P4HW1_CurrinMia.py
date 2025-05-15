# Mia Currin
# P4HW1
#4/30/25
# Using loops for grade average




# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))
scores = []
print()

# Create loop using "if" and "while" to collect scores
for i in range(1, num_scores + 1):
    while True:
        try:
            score = int(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:     #sets valid range
                scores.append(score)
                break
            else:            #evaluates and notifies user of invalid input
                 print()
                 print("INVALID Score entered!!!!")
                 print("Score should be between 0 and 100")
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")

print()
print("----------------Results--------------------")

# Find and display the lowest score
min_score = min(scores)
print("Lowest score  :", min_score)

# Remove the lowest score from the list
scores.remove(min_score)
print("Modified List :", scores)

# Calculate and display the average score
if scores:
    average_score = sum(scores) / len(scores)
else:
    average_score = 0
print("Scores Average:", average_score)

# Determine and display the letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("Grade         :", letter_grade)

print("---------------------------------------------")
