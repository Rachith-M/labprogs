goalstate = {"A":"0", "B":"0"}
roomstate = {"A":"0", "B":"0"}
location = input("Enter the location of the vaccum cleaner (A or B): ")
cost = 0
for room in roomstate:
    state = input(f"Enter the state of room {room} (0 for clean and 1 for dirty): ")
    roomstate[room] = state
print("\nGoal state: ",goalstate)
print("Initial room state: ",roomstate)
print("Vaccum is at: ",location)

if roomstate!=goalstate:
    if location=="A":
        if roomstate["A"] == "1":
            roomstate["A"] = "0"
            cost+=1
            print("Room A was dirty -> Cleaned (cost = 1)")
            
        if roomstate!=goalstate:
            print("Move from A->B (cost = 1)")
            cost+=1
            if roomstate["B"] == "1":
                roomstate["B"] = "0"
                cost+=1
                print("Room B was dirty -> Cleaned (cost = 1)")
    elif location == "B":
        if roomstate["B"] == "1":
            roomstate["B"] = "0"
            cost+=1
            print("Room B was dirty -> Cleaned (cost = 1)") 
        if roomstate!=goalstate:
            print("Move B->A (cost = 1)")
            cost+=1
            if roomstate["A"] == "1":
                roomstate["A"] = "0"
                cost+=1
                print("Room A was dirty -> Cleaned (cost = 1)")
    else:
        print("Invalid Start location!")
        
else:
    print("All rooms are already cleaned!")

print("The total cost is: ",cost)
print("The final room state is: ",roomstate)      
