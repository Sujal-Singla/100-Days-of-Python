text = input("Enter text :")

digits = 0
alpha = 0
for char in text:
	if char.isdigit():
		digits += 1


for char in  text:
	if char.isalpha():
		alpha += 1

vowels = "aeiouAEIOU"
vowels = [char for char in text if char in vowels]
consonents = 0
for char in text:
	if char.isalpha() and char not in vowels:
		consonents += 1


spaces = 0
for char in text:
	if char.isspace():
		spaces += 1

special = 0
for char in text:
	if not char.isalnum() and not char.isspace():
		special += 1

print("------------- TEXT REPORT -------------")
print("Characters          : ", len(text))
print("Characters No Space : ", len(text.replace(" ","")))
print("Words               : ",len(text.split()))
print("Vowels              : ", len(vowels))
print("Consonants          : ", consonents)
print("Digits              : ", digits)
print("Special Characters  : ", special)
print("Spaces              : ", spaces)
print("----------------------------------------")
