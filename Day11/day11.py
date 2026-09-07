num = int(input("Enter the  number of skills you want: "))

reqSkills = set()
for i in range(num):
	skill = input(f"Enter required skill {i+1}: ").strip().lower()
	reqSkills.add(skill)

num1 = int(input("Enter the number of skills the candidate have: "))
presentSkills = set()
for i in range(num1):
	skill = input(f"Enter there skills {i+1}: ").strip().lower()
	presentSkills.add(skill)

print("---------- SKILL REPORT ----------")
print("Required Skills : ", reqSkills)
print("Matching Skills : ", reqSkills.intersection(presentSkills))
print("Missing Skills  : ", reqSkills.difference(presentSkills))
print("Extra Skills    : ", presentSkills.difference(reqSkills))
if reqSkills == presentSkills:
	print("Candidate Status: ELIGIBLE")
else:
	print("Candidate Status: NOT ELIGIBLE")
print("----------------------------------")
