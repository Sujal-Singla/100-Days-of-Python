inventory = {}
exit = 1
print("1. Add Product")
print("2. Updating Stock")
print("3. Search Product")
print("4. Remove Product")
print("5. Display Inventory")
print("6. Calculate present Inventory value")
print("7. List product with low stock")

def addproduct():
	product_id = input("Enter the product ID: ")
	name = input("Enter product name: ")
	category = input("Enter category: ")
	quantity = int(input("Enter quantity: "))
	price = float(input("Enter price: "))
	inventory[product_id] = {
	"name": name,
	"category": category,
	"quantity": quantity,
	"price": price
	}
	print("product added successfully.")

def searchProduct():
	search_id = input("Enter the product id to search: ")
	if search_id in inventory:
		product = inventory[search_id]
		print(product)
	else:
		print("Product not found")

def updateProduct():
	product_id = input("Enter product ID: ")
	if product_id in inventory:
		new_quantity = int(input("Enter new quantity: "))
		inventory[product_id]["quantity"] = new_quantity
		print("Stock Update Successfully.")
	else:
		print("Product not found")


def removeProduct():
	product_id = input("Enter product ID: ")
	if product_id in inventory:
		del inventory[product_id]
		print("Product removed successfully...")
	else:
		print("Product not fount")


def displayProduct():
	for product_id, product in inventory.items():
		print(product_id)
		print(product["name"])
		print(product["category"])
		print(product["quantity"])
		print(product["price"])

def calValue():
	total = 0
	for product in inventory.values():
		total += product["quantity"]*product["price"]
		print(f"Stock Value: ₹{total:.2f}")


def lowStock():
	for product_id, product in inventory.items():
		if product["quantity"] < 5:
			print(product_id, product["name"], product["quantity"])

while(exit != 0):
	choice = int(input("Enter the operation to perform on stocks: "))
	match choice:
		case 1:
			addproduct()
		case 3:
			searchProduct()
		case 2:
			updateProduct()
		case 4:
			removeProduct()
		case 5:
			displayProduct()
		case 6:
			calValue()
		case 7:
			lowStock()
		case 8:
			exit = 0
		case _:
			print("Invalid number entered")
