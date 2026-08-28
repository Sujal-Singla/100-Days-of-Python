food = float(input("Enter the value you spend on food"))
travel = float(input("Enter the value you spend on Travel"))
books = float(input("Enter the value you spend on Books"))
internet = float(input("Enter the value you spend on Internet"))
stationary = float(input("Enter the value you spend on Stationary"))
subtotal = food + travel + books + internet + stationary
discount = 0.05
tax = 0.10
amountAfterDiscount = subtotal - subtotal*discount
amountAfterTax = subtotal - (amountAfterDiscount*tax);
print("==============================")
print("        EXPENSE BILL          ")
print("==============================")
print("Food: ", food)
print("Travel: ",travel)
print("Books: ", books)
print("Internet: ", internet)
print("Stationery: ", stationary)

print("Subtotal: ",subtotal)
print("Discount: ", subtotal*discount)
print("Tax: ", tax*(amountAfterDiscount))
print("Final Amount: ", amountAfterTax)
print("==============================")

