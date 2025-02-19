item = input("what is the item want to buy? ")
price = float(input("what is the price of the item ? "))
quantity = int(input("How much quantity you are bought ?"))

total = price * quantity

print(f"You are bought {quantity} item of {item} and the total amount you paid for ${total}")