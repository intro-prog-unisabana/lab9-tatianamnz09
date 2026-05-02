from aircraft import Aircraft
 
model = input("Enter aircraft model:\n")
plane = Aircraft(model)
 
while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")
    parts = command.split()
    action = parts[0].upper()
 
    if action == "X":
        break
    elif action == "A":
        feet = int(parts[1])
        plane.climb(feet)
    elif action == "D":
        feet = int(parts[1])
        plane.descend(feet)
 
print(f"Final altitude: {plane.altitude} feet")