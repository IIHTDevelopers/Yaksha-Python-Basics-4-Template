# TODO: Function to read food items from a file
def read_food_items(file_path):
    """
    Reads food items and their type (Veg/Non-Veg) from a file.

    File format:
    Each line must be in the format: ItemName,Type
    Example:
        Pizza,Veg
        Chicken Wings,Non-Veg

    Args:
        file_path (str): Path to the file.

    Returns:
        list of tuples: [(item_name, item_type), ...]
    """
    # Initialize list
    # TODO: Open file and read lines
    # TODO: Split each line into item and type
    # TODO: Append valid entries as tuple
    # TODO: Handle file not found error
    pass


# TODO: Function to classify food items
def classify_food_items(food_items):
    """
    Classifies food items into Veg and Non-Veg lists.

    Args:
        food_items (list): List of tuples (item_name, item_type)

    Returns:
        dict: {'Veg': [...], 'Non-Veg': [...]}
    """
    # TODO: Initialize classification dict
    # TODO: Iterate and sort items into correct list
    pass


# ✅ Main Execution
if __name__ == "__main__":
    file_path = "food_items.txt"  # TODO: Ensure the file exists with proper format
    items = read_food_items(file_path)
    result = classify_food_items(items)

    print("\n--- Food Classification ---")
    print("Veg Items:", result.get('Veg'))
    print("Non-Veg Items:", result.get('Non-Veg'))
