marks = []

for i in range(1, 4):
    mark = int(input("Enter marks for exam " + str(i) + ": "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid Marks")

else:
    average = sum(marks) / 3

    print("Average Marks:", average)

    if marks[0] < marks[1] < marks[2]:
        print("Performance Trend: Improving")

    elif marks[0] > marks[1] > marks[2]:
        print("Performance Trend: Declining")

    elif marks[0] == marks[1] == marks[2]:
        print("Performance Trend: Constant")

    else:
        print("Performance Trend: Fluctuating")

