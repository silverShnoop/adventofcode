#
# Get the Puzzle Input from the User
#
def puzzle_choice(title, puzzle_no, puzzle_options):
    
    avail_options = []

    # Print the available puzzle options

    print(title + puzzle_no)
    print("Select one of: ")

    for option in puzzle_options:
        print(str(option[0]) + " " + option[1])
        avail_options.append(option[0])

        # Raise an exception if the options are not integers
        try:
           number = int(option[0])
        except:
            raise

        # Raise an exception if no options are supplied
    if len(avail_options) <=0:
        raise ValueError("No options supplied")


    # Get user input

    number = 0

    while True:
        try:
            number = int(input("No: "))

            if number not in avail_options:
                raise ValueError

            break
        except ValueError:
            print("This was not a valid option, please try again.")
     
    return number