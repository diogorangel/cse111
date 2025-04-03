#Author : Diogo Rangel Dos Santos
import csv
import datetime

def read_csv_file(filename):
    """Reads a CSV file and returns a dictionary where the first column is the key."""
    data = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                data[row[0]] = row[1:]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
        return None
    return data

def process_order(products_file, request_file):
    """Processes the order and prints a receipt."""
    products = read_csv_file(products_file)
    requests = read_csv_file(request_file)
    
    if products is None or requests is None:
        return
    
    subtotal = 0.0
    total_items = 0
    sales_tax_rate = 0.06
    print("\n==============================")
    print("   Welcome to Fresh Mart!   ")
    print("==============================\n")
    print("Items Purchased:")
    
    try:
        for item_id, quantity in requests.items():
            if item_id not in products:
                raise KeyError(f"Product ID {item_id} not found in product catalog.")
            name, price = products[item_id]
            price = float(price)
            quantity = int(quantity[0])
            total_price = price * quantity
            subtotal += total_price
            total_items += quantity
            print(f"{name}: {quantity} @ ${price:.2f} each = ${total_price:.2f}")
    except KeyError as e:
        print(f"Error: {e}")
        return
    except ValueError:
        print("Error: Invalid data format in CSV file.")
        return
    
    sales_tax = subtotal * sales_tax_rate
    total_due = subtotal + sales_tax
    
    print("\n------------------------------")
    print(f"Total items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (6%): ${sales_tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")
    print("------------------------------\n")
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Date & Time: {current_time}")
    print("\nThank you for shopping at Fresh Mart!")
    print("==============================")

if __name__ == "__main__":
    process_order("products.csv", "request.csv")