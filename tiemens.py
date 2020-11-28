goAgain = "Y"
name = input("What is your name? ")
while goAgain == "Y":
    print("Hello", name, end="")
    print("! What type of video game genre do you enjoy? ", end="")
    game = input()
    print("That's awesome! I don't know if I've played the", game, "genre before.")
    print("Would you like to tell me another video game genre you like?")
    goAgain = input("Enter Y or N :")
    if goAgain == "N":
        print("Have a great day", name)
        end=""
