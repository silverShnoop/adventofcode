import common

TITLE = "ADVENT OF CODE"
PUZZLE_NO = "DAY2"
PUZZLE_OPTIONS = ([1, "MAX-MIN"], [2, "DIVISION"])

INPUT_DATA = "input.txt"

#
# Take the min-value from the max-value in each row and sum them
#
def calc_checksum(spreadsheet):
    
    checksum = 0

    for row in spreadsheet:
        min_value = int(row[0])
        max_value = int(row[0])

        for col in row:
            col_value = int(col)
            if col_value < min_value:
                min_value = col_value
            if col_value > max_value:
                max_value = col_value

        row_checksum = max_value - min_value

        checksum += row_checksum

    return checksum
   

#
# Find the only 2 numbers that evenly divide in each row and sum them 
#
def calc_checksum_2(spreadsheet):
    
    checksum = 0

    for row in spreadsheet:
        
        row_checksum = 0

        for div_pos, dividend in enumerate(row):
            dividend_value = int(dividend)

            for divisor in row[div_pos+1:]:
                divisor_value = int(divisor)

                if dividend_value > divisor_value:
                    if dividend_value % divisor_value == 0:
                        row_checksum = int(dividend_value / divisor_value)
                        break
                elif divisor_value > dividend_value:
                    if divisor_value % dividend_value == 0:
                        row_checksum = int(divisor_value / dividend_value)
                        break
                else:
                    print("ERROR: values are same")
                    print(row)
            
            if row_checksum > 0:
                break

        if row_checksum > 0:
            checksum += row_checksum
        else:
            print("ERROR: no evenly divided value found for row")
            print(row)

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

    if puzzle_no == 1:
        checksum = calc_checksum(spreadsheet)
    elif puzzle_no == 2:
        checksum = calc_checksum_2(spreadsheet)
    
    print("RESULT: ", checksum)


main()
