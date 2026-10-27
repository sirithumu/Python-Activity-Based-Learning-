print("FOOD WASTE MONITORING SYSTEM")

prepared = float(input("Enter food prepared in kg: "))
wasted = float(input("Enter food wasted in kg: "))

if prepared <= 0 or wasted < 0 or wasted > prepared:
    print("Invalid input")
else:
    consumed = prepared - wasted
    percentage = (wasted / prepared) * 100

    print("Food consumed:", round(consumed, 2), "kg")
    print("Food waste percentage:", round(percentage, 2), "%")

    if percentage <= 10:
        print("Low food waste")
    else:
        print("High food waste")
