#
# Get the Puzzle Input from the User
#
def puzzle_choice(title, puzzle_no, puzzle_options):
    
    avail_options = []

    # Print the available puzzle options

    print(title) 
    print(puzzle_no)

    for option in puzzle_options:
        print(str(option[0]) + " " + option[1])
        avail_options.append(option[0])

        # Raise an exception if the options are not integers
        try:
           number = int(option[0])
        except:
            raise

        # Raise an exception if no options are supplied
    if len(avail_options) <= 0:
        return


    # Get user input

    print("Select puzzle stage: ")
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