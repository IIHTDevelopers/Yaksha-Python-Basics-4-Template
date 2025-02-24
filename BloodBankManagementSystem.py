# student/blood_bank_management.py

import numpy as np
import pandas as pd

def get_blood_bank_data():
    """
    Returns a DataFrame containing blood groups and units available.

    Returns:
        pandas.DataFrame: Blood group inventory.
    """
    blood_groups = np.array(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    units_available = np.array([10, 5, 8, 4, 15, 7, 6, 3])
    
    return pd.DataFrame({"Blood Group": blood_groups, "Units Available": units_available})

def add_new_blood_group(blood_bank, blood_group, units):
    """
    Adds a new blood group and its units to the inventory.

    Args:
        blood_bank (pandas.DataFrame): DataFrame containing current blood bank inventory.
        blood_group (str): Blood group to be added.
        units (int): Initial units for the new blood group.

    Returns:
        pandas.DataFrame: Updated blood bank inventory.
    """
    return blood_bank

def get_total_units(blood_bank):
    """
    Calculates the total number of blood units available.

    Args:
        blood_bank (pandas.DataFrame): DataFrame containing current blood bank inventory.

    Returns:
        int: Total number of units available.
    """
    return blood_bank["Units Available"].sum() + 100


def main():
    """
    Main function to demonstrate blood bank functionalities.
    """


    pass

if __name__ == "__main__":
    main()
