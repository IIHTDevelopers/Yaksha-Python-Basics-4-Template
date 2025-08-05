import pandas as pd

# ✅ Initial blood bank data
blood_groups = ["A+", "B+", "O-", "AB-"]
units_available = [10, 8, 4, 3]

# Creating DataFrame
blood_df = pd.DataFrame({
    "Blood Group": blood_groups,
    "Units Available": units_available
})

# TODO: Function 1 - Add a new blood group and its units to the DataFrame
def add_blood_group(df, group, units):
    # Add a new row to the DataFrame with given blood group and units
    pass


# TODO: Function 2 - Calculate the total units available across all groups
def total_units(df):
    # Return the sum of 'Units Available'
    pass


# TODO: Function 3 - Get all blood groups with units less than a given threshold
def low_stock_groups(df, threshold=5):
    # Return DataFrame rows where 'Units Available' < threshold
    pass


# Optional: Sample usage block for testing manually
if __name__ == "__main__":
    # TODO: Test total_units()
    total = total_units(blood_df)
    print("Total Units:", total)

    # TODO: Test low_stock_groups()
    low_stock = low_stock_groups(blood_df, threshold=5)
    print("\nBlood Groups with Low Stock:")
    print(low_stock)
