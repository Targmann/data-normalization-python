import csv
import os;

input_file = "input.csv"
output_file = "output.csv"

def main():
    # Ordering
    ordering = input(
'''
How would you like to order the data?
n - Alphabetically by first name
a - Chronologically by age (NA at end)
c - Chronologically by date (n.d. at end)
l - Alphabetically by location

> '''
)
    # Catch a missing file error
    if not os.path.exists(input_file):
        print("FileNotFoundError: The input file does not exist in the specified path");
    # Open files to read and write
    with open(input_file, mode="r", newline="", encoding="utf-8") as infile, \
        open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        # Read header
        header = next(reader)
        # Write header
        writer.writerow(header)
        # Sorted rows
        rows = []
        # Formatting rows
        for row in reader:
            # Store row values and format
            name = row[0].strip().title()
            age = row[1].strip()
            email = row[2].strip().lower()
            city = row[3].strip().title()
            signup_date = row[4].strip()
            name = ' '.join(name.split()) # Remove extra spaces between names
            # Substitute missing ages or dates
            if (age == ''):
                age = "NA"
            if (signup_date == ''):
                signup_date = "n.d."
            # Store formatted rows
            rows.append([name, age, email, city, signup_date])
        # Sort rows according to user choice
        match(ordering):
            case 'n':
                rows.sort(key=lambda row: row[0])
            case 'a':
                rows.sort(key=lambda row: row[1])
            case 'c':
                rows.sort(key=lambda row: row[4])
            case 'l':
                rows.sort(key=lambda row: row[3])
        # Ouput each row in proper order
        for row in rows:
            writer.writerow(row)

# Main
if __name__ == "__main__":
    main()