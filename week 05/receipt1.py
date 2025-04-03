#Author : Diogo Rangel Dos Santos

import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row  # Store the entire row as the value
    
    return dictionary

def main():
    # Read the products file into a dictionary
    products_dict = read_dictionary('products.csv', 0)
    print("Product Dictionary Loaded:")
    print(products_dict)  # Debug print to check dictionary contents

    # Open the request file and process orders
    with open('request.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        print("\nCustomer Receipt:")
        for row in reader:
            product_number, quantity = row[0], int(row[1])
            if product_number in products_dict:
                product_name = products_dict[product_number][1]
                product_price = float(products_dict[product_number][2])
                print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
            else:
                print(f"Product {product_number} not found.")

if __name__ == "__main__":
    main()
