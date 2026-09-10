teams = {}
points = 0
print("===============Operation===============")
print("1. Add Team")
print("2. Display Teams")
print("3. Exit")
print("4. Sort by points")
print("5. Sort by scores")
print("=======================================")

def addTeam():
	teamNumber = int(input("Enter the team number: "))
	teamName = input("Enter the team Name: ")
	wins = int(input("Enter the teams wins: "))
	loses = int(input("Enter the team losses: "))
	runsScored = int(input("Enter the runs scored: "))
	teams[teamNumber] = {
	"TeamName":teamName,
	"Wins": wins,
	"Losses": loses,
	"runScored": runsScored,
	"Points": wins*2
	}
	print("Team Added Successfully")

def display():
	for number in teams.items():
		print(number)

def sortByPoints():
	sortedTeams = sorted(teams.values(), key=lambda team:(-team["Points"], -team["runScored"]))
	print("\n----------- TOURNAMENT STANDINGS -----------")
	position = 1
	for team in sortedTeams:
		print( f"{position}. {team['TeamName']} " f"Points: {team['Points']} " f"Runs: {team['runScored']}" )
		position += 1
		print("--------------------------------------------")


def sortByScores():
	sortedTeams = sorted(teams.values(), key=lambda team:-team["runScored"])
	print("\n----------- TOURNAMENT STANDINGS -----------")
	position = 1
	for team in sortedTeams:
		print( f"{position}. {team['TeamName']} " f"Points: {team['Points']} " f"Runs: {team['runScored']}" )
		position += 1
		print("--------------------------------------------")


exit = 0
while(exit != 1):
	num = int(input("Enter the thing you want to do: "))
	match num:
		case 1:
			addTeam()
		case 2:
			display()
		case 3:
			print("Exited Successfully")
			exit = 1
		case 5:
			sortByScores()
		case 4:
			sortByPoints()
		case _:
			print("Invalid Number")
