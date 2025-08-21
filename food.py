def read_food_sales(file_path):
    """
    Reads food items with sales data from a text file.
    Each line format: FoodName,Category,Sales

    Args:
        file_path (str): Path to the sales data file.

    Returns:
        list[tuple]: A list of tuples in the form (FoodName, Category, Sales)
    """
    # TODO: Open the file in read mode
    # TODO: Read line by line
    # TODO: Split by comma and parse values
    # TODO: Append as (FoodName, Category, Sales) tuple to items list
    # TODO: Return the list of tuples
    pass


def find_lowest_sales_item(items):
    """
    Finds the food item with the lowest sales.

    Args:
        items (list[tuple]): List of tuples [(FoodName, Category, Sales), ...]

    Returns:
        tuple | None: (FoodName, Sales) of the lowest selling item,
                      or None if list is empty.
    """
    # TODO: Check if items is empty, return None
    # TODO: Find item with minimum sales
    # TODO: Return (FoodName, Sales) tuple
    pass


if __name__ == "__main__":
    # TODO: Define the file name (e.g., "food_sales.txt")
    # TODO: Call read_food_sales(file_name)
    # TODO: Print the sales data
    # TODO: Call find_lowest_sales_item(sales_data)
    # TODO: Print the lowest sales item
    pass
