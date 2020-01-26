'''
Author Name: Brandon Eisele
Date: 1/19/2020
Program Name: Assign1Drone
Purpose: Simulation of drone movement using keyboard keys in a 3d environment
'''

#Variables
directions = ["North", "East", "South", "West"]
droneXPos = 0
droneYPos = 0
droneZPos = 0
droneDirection = 0
userInput = 0

#Sets drone position based on given inputs
def setDronePos(newX, newY, newZ):
    global droneXPos
    global droneYPos
    global droneZPos
    droneXPos = newX
    droneYPos = newY
    droneZPos = newZ

#Sets drone direction based on given input
def setDroneDirection(LoR):
    global directions
    global droneDirection
    if LoR == "Left":
        if droneDirection == 0:
            droneDirection = 3
        else:
            droneDirection = droneDirection - 1
    elif LoR == "Right":
        if droneDirection == 3:
            droneDirection = 0
        else:
            droneDirection = droneDirection + 1
    return directions[droneDirection]

#Displays options menu
def displayMenu():
    print("Which direction would you like to move the drone?")
    print("1 - Move Up")
    print("2 - Move Down")
    print("3 - Move Forward")
    print("4 - Move Backward")
    print("5 - Turn Left")
    print("6 - Turn Right")
    print("7 - Display Position")
    print("8 - Exit Navigation")

#Displays the current info about the drone, consisting of the current x, y, and z positions, as well as the drone's current orientation
def displayDroneLocationInfo():
    print("Drone: x_pos={}, y_pos={}, z_pos={}, orientation={}".format(droneXPos, droneYPos, droneZPos, directions[droneDirection]))

#Main control function, takes user keyboard inputs and runs the relevant functions to make the drone do what you say
def controlDrone():
    global droneXPos
    global droneYPos
    global droneZPos
    global directions
    global droneDirection
    global userInput
    displayMenu()
    while userInput != "8":
        userInput = input()
        if userInput == "1":
            setDronePos(droneXPos, droneYPos, droneZPos + 1)
            print("You have moved up")
            displayMenu()
        if userInput == "2":
            setDronePos(droneXPos, droneYPos, droneZPos - 1)
            print("You have moved down")
            displayMenu()
        if userInput == "3":
            if directions[droneDirection] == "North":
                setDronePos(droneXPos, droneYPos + 1, droneZPos)
            if directions[droneDirection] == "East":
                setDronePos(droneXPos + 1, droneYPos, droneZPos)
            if directions[droneDirection] == "South":
                setDronePos(droneXPos, droneYPos - 1, droneZPos)
            if directions[droneDirection] == "West":
                setDronePos(droneXPos - 1, droneYPos, droneZPos)
            print("You have moved forward")
            displayMenu()
        if userInput == "4":
            if directions[droneDirection] == "North":
                setDronePos(droneXPos, droneYPos - 1, droneZPos)
            if directions[droneDirection] == "East":
                setDronePos(droneXPos - 1, droneYPos, droneZPos)
            if directions[droneDirection] == "South":
                setDronePos(droneXPos, droneYPos + 1, droneZPos)
            if directions[droneDirection] == "West":
                setDronePos(droneXPos + 1, droneYPos, droneZPos)
            print("You have moved backward")
            displayMenu()
        if userInput == "5":
            setDroneDirection("Left")
            print("You have turned left")
            displayMenu()
        if userInput == "6":
            setDroneDirection("Right")
            print("You have turned right")
            displayMenu()
        if userInput == "7":
            displayDroneLocationInfo()
            displayMenu()
    print("Exiting navigation")

controlDrone()
