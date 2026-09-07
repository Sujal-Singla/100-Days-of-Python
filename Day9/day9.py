print("========== PLAYLIST MANAGER ==========");
print("1. Add Song")
print("2. Remove Song")
print("3. Search Song")
print("4. Display Playlist")
print("5. Reverse Playlist")
print("6. Clear Playlist")
print("7. Exit")
exit = 0
playList = []
while(exit != 1):
	num = int(input("Enter choice "))
	match num:
		case 1:
			song = input("Enter song ")
			playList.append(song)
		case 2:
			element = input("song to remove ")
			if element in playList:
				playList.remove(element)
				print("Element removed\n")
			else:
				print("Song Not found")
		case 3:
			element = input("song to remove ")
			if element in playList:
				print(element, " found")
			else:
				print("Song not found")
		case 4:
			for songs in playList:
				print(songs)
		case 5:
			playList.reverse()
			print(playList)
		case 6:
			playList.clear()
			print("List cleared, no song in the list")
		case 7:
			print("Exited")
			exit = 1
