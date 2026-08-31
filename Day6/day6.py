num = int(input("Enter starting number: "))
endNum = int(input("Enter ending number: "))
maxMul = int(input("Enter maximum multiplier: "))

for i in range(num, endNum+1):
	print(f"----- TABLE OF {i} -----")
	for j in range(maxMul+1):
		print(f"{i}*{j} = {i*j}")


