n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    tid = int(input("Enter transaction ID: "))
    transactions.append(tid)

repeated = []

for tid in transactions:
    if transactions.count(tid) > 1 and tid not in repeated:
        repeated.append(tid)

if repeated:
    print("Repeated Transactions:", repeated)
else:
    print("No Repeated Transactions Found")

