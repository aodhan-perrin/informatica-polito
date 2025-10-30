tickets = 100
transactions = 0

while tickets > 0:
    cart = int(input("insert no. of tickets (max 4) -> "))

    if cart <= 4:
        tickets -= cart
        transactions += 1

        print(f"{cart} tickets purchased.")
    elif cart > tickets:
        print(f"theater too full: {tickets} seats remaining")
    else:
        print("error: no more than 4 tickets per person")

print(f"transactions: {transactions}")