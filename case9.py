print("STUDENT MARKS MATRIX ANALYSIS")

marks = []

for i in range(3):
    print("Enter marks for Student", i + 1)
    student_marks = []

    for j in range(3):
        mark = int(input("Enter marks for Subject " + str(j + 1) + ": "))

        if mark < 0 or mark > 100:
            print("Invalid marks")
            quit()

        student_marks.append(mark)

    marks.append(student_marks)

print("\nStudent Results")

for i in range(3):
    total = sum(marks[i])
    average = total / 3

    print("Student", i + 1)
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))

