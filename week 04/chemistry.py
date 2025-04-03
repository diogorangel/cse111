#Author : Diogo Rangel Dos Santos
#Week 04 : Chemistry

import re
from formula import parse_formula

def periodic_table_dict():
    """Returns a dictionary representing the periodic table of elements."""
    return {
        "H": ["Hydrogen", 1.00794], "He": ["Helium", 4.002602], "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182], "B": ["Boron", 10.811], "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067], "O": ["Oxygen", 15.9994], "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797], "Na": ["Sodium", 22.98976928], "Mg": ["Magnesium", 24.305],
        "Al": ["Aluminum", 26.9815386], "Si": ["Silicon", 28.0855], "P": ["Phosphorus", 30.973762],
        "S": ["Sulfur", 32.065], "Cl": ["Chlorine", 35.453], "K": ["Potassium", 39.0983],
        "Ca": ["Calcium", 40.078], "Fe": ["Iron", 55.845], "Cu": ["Copper", 63.546],
        "Zn": ["Zinc", 65.38], "Ag": ["Silver", 107.8682], "Au": ["Gold", 196.966569]
    }
# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    # Return the total molar mass.
    return

def compute_molar_mass(formula, periodic_table):
    """Computes and returns the molar mass of a molecule given its formula."""
    element_pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(element_pattern, formula)
    
    molar_mass = 0.0
    for element, count in matches:
        count = int(count) if count else 1
        if element in periodic_table:
            atomic_mass = periodic_table[element][1]
            molar_mass += atomic_mass * count
        else:
            raise ValueError(f"Unknown element: {element}")
    
    return molar_mass

def main():
     # Get a chemical formula for a molecule from the user.
  # Get the mass of a chemical sample in grams from the user.
  # Call the make_periodic_table function and
  # store the periodic table in a variable.
  # Call the parse_formula function to convert the
  # chemical formula given by the user to a compound
  # list that stores element symbols and the quantity
  # of atoms of each element in the molecule.
  # Call the compute_molar_mass function to compute the
  # molar mass of the molecule from the compound list.
  # Compute the number of moles in the sample.
  # Print the molar mass.
  # Print the number of moles.
    periodic_table = periodic_table_dict()
    formula = input("Enter the chemical formula of the substance: ")
    mass = float(input("Enter the mass in grams of the sample: "))
    
    molar_mass = compute_molar_mass(formula, periodic_table)
    moles = mass / molar_mass
    
    print(f"Molar Mass of {formula}: {molar_mass:.5f} g/mol")
    print(f"Number of moles in the sample: {moles:.5f} moles")

if __name__ == "__main__":
    main()