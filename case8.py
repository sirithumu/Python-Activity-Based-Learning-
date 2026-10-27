print("TEXT COMPRESSION USING CHARACTER RUNS")

text = input("Enter a string: ")

if text == "":
    print("Invalid input")
else:
    compressed = ""
    count = 1

    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count = count + 1
        else:
            compressed = compressed + text[i] + str(count)
            count = 1

    compressed = compressed + text[-1] + str(count)

    print("Compressed string:", compressed)
