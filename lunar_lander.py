"""
Name: Sabrina Smai
PennID: 64371075
Statement of Work: 
    Resources include (Stack Overflow, CIT591 Office Hours, Lecture Videos)
win = []
inputs = []
"""
game_running = True

# A comma-separated list of inputs that leads to a “win” 
win = []
# A comma-separated list of inputs that leads to a “loss” 
inputs = []

# a while loop: while condition is met, run code block inside loop
# while game_running is True , run code block inside loop
while (game_running):

# Initial are the initial values for the three variables
    altitude = 100.0  #meters
    fuel = 100 # liters
    velocity = 0.0 # meters/second
    constant = 0.15 # given constant
    seconds = 0 # Numbers of iterations through the while loop = seconds of the game


    #while loop: while condition is met, run code block inside loop
    while (altitude > 0):
        # ​velocity​ increases by 1.6 meters per second
        velocity += 1.6
        # get user input
        z = input("Enter the amount of fuel to use \n")
        # number of iterations through the while loop = seconds of the game so adding 1 everytime the playing runs through this loop
        seconds += 1
        # for loop: checking each character in string to determine it is a digit (stack overflow). If not digit, ask user to input a number.
        for character in z: 
            if character.isdigit() == False:
                print("Please enter a number.\n") 
                z = input("Enter the amount of fuel to use \n")
                break  
        # casting fuel amount to float to avoid type errors
        y = float(z)
        # adding inputs into list   
        inputs.append(z)
        # any fuel less than zero, set it to 0 as there's no such thing as negative fuel
        if y < 0:
            y = 0
        # however, if fuel left is less than user input for fuel, just set fuel to equal user input
        if y > fuel:
            y = fuel
        # calculating velocity decrease proportional to fuel burned by multiplying the specified constant 0.15
        x = constant * y
        #  ​velocity​ decreases by an amount proportional to the ​fuel​ you burn
        velocity -= x
        print("Velocity = " + str(velocity) + "\n")
        # altitude​ decreases by your ​velocity
        altitude -= velocity
        # this condition ensures that player does not go in the opposite direction. Forcing altitude greater than 100 to be 100.
        if altitude > 100: 
            altitude = 100
        print("Altitude = " + str(altitude) + "\n")
        # fuel​ decreases by the amount specified by the player
        fuel -= y
        # print how much fuel is left
        print("Fuel = " + str(fuel) + "\n") 
        # if fuel is less than 0 means you ran out, the loop breaks and game is over.
        if fuel <= 0:
            game_running=False
            break
    #end while loop

    # out of the while loop
    # a safe landing is one where the final ​velocity​ is <  10m/s
    if velocity < 10:
        print("Your landing was safe\n")
        win.append("win")
    else:
        print("Your landing was unsafe\n")
        win.append("lose")
    # Display final results
    print("Final velocity = " + str(velocity) + "\n")
    print("Number of seconds for landing = " + str(seconds) + "\n")
    print("Final fuel = " + str(fuel) + "\n")

    # asking user input of whether they want to play again. This is looking at the first character to see if it's a 'y' or 'Y', then replay again
    replay = input("Would you like to play again? \n")
    if replay[0] == 'y' or replay[0] == 'Y':
        game_running = True
    # if the first character of the input is 'n' or 'N', then end game. Show user their wins in a list by which inputs they gave
    elif replay[0] == 'n' or replay[0] == 'N':
        game_running = False
        print(win)
        print(inputs)
    else:
    # however, if input isn't 'y', 'Y', 'n', nor 'N' get another input by specifically ask for an answer of 'yes' or 'no'
        replay = input("Enter either yes or no \n")
    # if yes, continue playing  
        if replay[0] == 'y' or replay[0] == 'Y':
            game_running = True
    # if no, end game and show wins with the fuel inputs
        if replay[0] == 'n' or replay[0] == 'N':
            game_running = False
            print(win)
            print(inputs)
# end of game
