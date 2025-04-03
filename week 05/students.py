#Author : Diogo Rangel Dos Santos

import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}
    
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) >= 2:
                key = row[key_column_index].replace("-", "")  # Remove dashes
                student_dict[key] = row[1]  # Store name as value
    
    return student_dict

def get_valid_inumber():
    """Prompt the user for an I-Number, validate it, and return it."""
    inumber = input("Enter an I-Number (e.g., 123456789 or 123-45-6789): ").replace("-", "")
    
    if not inumber.isdigit():
        print("Invalid I-Number")
        return None
    
    if len(inumber) < 9:
        print("Invalid I-Number: too few digits")
        return None
    
    if len(inumber) > 9:
        print("Invalid I-Number: too many digits")
        return None
    
    return inumber

def main():
    filename = "students.csv"
    key_column_index = 0  # Using I-Number as the key
    
    # Read students data into dictionary
    students = read_dictionary(filename, key_column_index)
    
    # Get a valid I-Number from the user
    inumber = get_valid_inumber()
    if inumber is None:
        return
    
    # Find and display the student name
    if inumber in students:
        print(f"Student Name: {students[inumber]}")
    else:
        print("No such student")

if __name__ == "__main__":
    main()