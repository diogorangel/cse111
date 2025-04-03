#Author: Diogo Rangel
#Date: 2025-04-02

def main():
    # Open the file for reading
    with open("provinces.txt", "r") as file:
        # Read lines into a list, stripping newline characters
        provinces = [line.strip() for line in file.readlines()]
    
    # Print the original list
    print("Original list:")
    print(provinces)
    
    # Remove the first and last elements
    if provinces:
        provinces.pop(0)  # Remove first element
    if provinces:
        provinces.pop(-1)  # Remove last element
    
    # Replace occurrences of "AB" with "Alberta"
    provinces = ["Alberta" if province == "AB" else province for province in provinces]
    
    # Count occurrences of "Alberta"
    alberta_count = provinces.count("Alberta")
    
    # Print modified list and Alberta count
    print("\nModified list:")
    print(provinces)
    print(f"\nNumber of times 'Alberta' appears: {alberta_count}")

# Run the main function
if __name__ == "__main__":
    main()
