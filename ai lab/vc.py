goalstate = {"A":"0","B":"0"}
roomstate = {"A":"0","B":"0"}
cost = 0
location = input("Enter the location of vaccum cleaner (A or B): ")
for room in roomstate:
    state = input(f"Enter the state of the room {room} (0 for clean and 1 for dirty): ")
    roomstate[room] = state
print("Goal state: ",goalstate)
print("Room state: ",roomstate)
print("Location of vaccum cleaner: ",location)
if roomstate!=goalstate:
    if location == 'A':
        if roomstate['A'] == '1':
            roomstate['A'] = '0'
            cost+=1
            print("Room  A was dirty and has now been cleaned (cost = 1)")
        
        if roomstate!=goalstate:
            print("Moving from A to B (cost = 1)")
            cost+=1
            if roomstate['B'] == '1':
                roomstate['B'] = '0'
                cost+=1
                print("Room B was dirty and has now been cleaned (cost = 1)")
    
    elif location == 'B':
        if roomstate['B'] == '1':
            roomstate['B'] = '0'
            cost+=1
            print("Room B was dirty and has been cleaned (cost = 1)")

        if roomstate!=goalstate:
            print("Moving from B to A (cost = 1)")
            cost+=1
            if roomstate['A'] == '1':
                roomstate['A'] = '0'
                cost+=1
                print("Room A was dirty and has been cleaned (cost = 1)")
    
    else:
        print("Invalid start location!")
else:
    print("All rooms are already cleaned!")

print("Final room state: ",roomstate)
print("Performance measurement (total cost): ",cost)