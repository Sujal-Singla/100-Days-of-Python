print("==============================")
print("       AGE REPORT             ")
print("==============================")
age = int(input("Current Age: "))
nextYear = age + 1
adult = False
student = False
internship = False
if(age>18):
	adult = True
	student = True
	internship = True

print("Next year: ", nextYear)
print("Adult: ", adult)
print("Student: ", student)
print("Eligible For Internship: ", internship)
print("==============================")
