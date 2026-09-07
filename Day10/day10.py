checkpoint = []
for i in range(3):
	x,y = map(int, input(f"Enter the coordinate {i+1} (x y): ").split())
	checkpoint.append((x,y))


horizontal = 0
vertical = 0

for i in range(len(checkpoint) - 1):
	current = checkpoint[i]
	nextPoint = checkpoint[i+1]

	horizontal += abs(nextPoint[0] - current[0])
	vertical += abs(nextPoint[1] - current[1])

print("\n----------- ROUTE SUMMARY -----------")
print("Checkpoints :", checkpoint)
print("Start       :", checkpoint[0])
print("End         :", checkpoint[-1])
print("Horizontal  :", horizontal)
print("Vertical    :", vertical)
print("-------------------------------------")
