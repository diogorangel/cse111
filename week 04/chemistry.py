#Author : Diogo Rangel Dos Santos
#Week 04 : Chemistry

import re

def make_periodic_table():
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
    periodic_table = make_periodic_table()
    formula = input("Enter the chemical formula of the substance: ")
    mass = float(input("Enter the mass in grams of the sample: "))
    
    molar_mass = compute_molar_mass(formula, periodic_table)
    moles = mass / molar_mass
    
    print(f"Molar Mass of {formula}: {molar_mass:.5f} g/mol")
    print(f"Number of moles in the sample: {moles:.5f} moles")

if __name__ == "__main__":
    main()