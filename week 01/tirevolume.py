#Author : Diogo Rangel Dos Santos
from datetime import datetime
import math

# Prompts for user input
widht = float(input("Enter the width of the tire in mm(ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire(ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches(ex 15): "))

# Calculate the tire volume using the given formula
volume = (math.pi * widht ** 2 * aspect_ratio * (widht * aspect_ratio + 2540 * diameter)) / 10000000000

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Displays the calculated volume
print(f"The approximate volume of the tire is {volume:.2f} liters")

#Tire price look up based on tire dimensions:
tire_prices = {
    (205,60,15): 80.99,
    (215,65,16): 95.50,
    (225,50,17): 110.75,
    (235,55,18): 125.99,
}

price = tire_prices.get((int(widht), int(aspect_ratio), int(diameter)),"Price not available")

if price != "Price not available":
    print(f"The price of the tire is ${price:.2f}")

else:
    print("The price of the tire is not available.\n")

buy_tires = input("Would you like to buy these dimensions? (yes/no): ").strip().lower()

# Write the data to the volumes.txt file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {widht}, {aspect_ratio}, {diameter}, {volume:.2f} \n")

# Display the data from the volumes.txt file
print("Data has been recorded to volumes.txt.")

if buy_tires == "yes":
    phone_number = input("What is your phone number? ")
    with open("volumes.txt", "a") as file:
        file.write(f"{phone_number}\n")
    print("You have purchased the tires. Thank you. We will contact you.")
else:
    with open("volumes.txt", "a") as file:
        file.write("\n")
    print("No problem. We see you in the future")   

# Display the data from the volumes.txt file
print("Data has been recorded to volumes.txt.")     

#addtional feature : Suggest sizes based on volume range
if volume < 30:
    print("This is a small tire, tipically for compact cars.")
elif 30 <= volume < 50:
    print("This is a medium tire, suitable for sedans and small SUVs.")
else:
    print("This is a large tire, likely for trucks or larger SUVs.")