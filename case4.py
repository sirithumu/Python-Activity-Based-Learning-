budget = float(input("Enter your budget: "))
total = 0

if budget <= 0:
    print("Invalid Budget")

else:
    valid = True

    for i in range(1, 4):
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid Input")
            valid = False
            break

        total = total + (price * quantity)

    if valid:
        print("Total Shopping Cost:", total)

        if total <= budget:
            print("Shopping is within budget")
        else:
            print("Budget exceeded")

