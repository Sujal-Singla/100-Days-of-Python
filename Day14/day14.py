frequency = {}
events = input("Enter Events: ").split()
total = 0
login = 0
logout = 0
error = 0
mostFrequent = ""
highestCount = 0
for e in events:
	event = e.lower()
	if event not in frequency:
        	frequency[event] = 1
	else:
        	frequency[event] +=1
	if(frequency[e]>highestCount):
		mostFrequent = e
		highestCount = frequency[e]

	total = total + 1
	if(event == "error"):
		error= error+ 1
	if(event == "logout"):
		logout = logout + 1
	if(event == "login"):
		login = login + 1

errorPercentage =  (error/total)*100
print("-------- SERVER EVENT REPORT ---------")
print("Total Events      : ", total)
print("Successful Logins : ", login)
print("Logouts           : ", logout)
print("Errors            : ", error)
print("Most Frequent     : ", mostFrequent)
print("Error Percentage  : ", errorPercentage)
print("---------------------------------------")


