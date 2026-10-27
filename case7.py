correct_answers = ["A", "B", "C", "D", "A"]
score = 0

for i in range(5):
    answer = input("Enter answer for question " + str(i + 1) + ": ")
    answer = answer.upper()

    if answer == correct_answers[i]:
        score = score + 1

print("Marks Obtained:", score)
print("Maximum Marks: 5")
