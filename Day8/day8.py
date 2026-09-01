firstName = input("Enter first name").strip().lower()
lastName = input("Enter last name").strip().lower()
dob = (input("Enter the birth year"))
num = (input("Enter the optional number"))
print("--------- USERNAME SUGGESTIONS ---------")
print("1. ", firstName + "." + lastName)
print("2. ", firstName + lastName)
print("3. ", firstName + dob)
print("4. ", firstName + "." + lastName + num)
print("----------------------------------------")


