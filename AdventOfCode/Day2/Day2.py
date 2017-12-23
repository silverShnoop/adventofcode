import common

TITLE = "ADVENT OF CODE"
PUZZLE_NO = "DAY2"
PUZZLE_OPTIONS = ()

INPUT_DATA = "input.txt"

def calc_checksum(spreadsheet):
    
    checksum = 0

    for row in spreadsheet:
        min_value = row[0]
        max_value = row[0]

        for col in row:
            if col < min_value:
                min_value = col
            if col > max_value:
                max_value = col

        row_checksum = max_value - min_value

        checksum += row_checksum

    return checksum
   

#
# Main
#
def main():

    spreadsheet = []

    # Get the puzzle options

    puzzle_no = common.puzzle_choice(TITLE, PUZZLE_NO, PUZZLE_OPTIONS)
        

    with open(INPUT_DATA, "r") as in_file:
        for row in in_file.readlines():
            spreadsheet.append(row.split())

    
    


main()
