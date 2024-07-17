full_name = input("What is your first and last name? ")

if len(full_name) <= 2:
    print("Error name has to be more than 2 letters")
else:
    print("The length of your name is " + str(len(full_name)) + ". ")