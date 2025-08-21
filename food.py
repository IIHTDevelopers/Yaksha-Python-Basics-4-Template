"""
FoodProcessing Module
---------------------
This module contains functions to process food sales data
from a dataset file.

The dataset file should be a plain text file (.txt) with
each line in the format:

    FoodName,Category,Sales

Example:
    Pizza,Veg,120
    Chicken Wings,Non-Veg,80
    Pasta,Veg,150
"""

def read_food_sales(file_path: str) -> list[tuple[str, str, int]]:
    """
    Reads food items with sales data from a text file.

    Args:
        file_path (str): Path to the food sales dataset file.

    Returns:
        list[tuple[str, str, int]]:
            A list of tuples containing food name, category, and sales.
            Example:
            [
                ("Pizza", "Veg", 120),
                ("Chicken Wings", "Non-Veg", 80),
                ...
            ]

    TODO:
        - Open the file in read mode.
        - Parse each line (split by comma).
        - Convert sales to integer.
        - Return a structured list of tuples.
    """
    pass


def find_lowest_sales_item(items: list[tuple[str, str, int]]) -> tuple[str, int] | None:
    """
    Finds the food item with the lowest sales.

    Args:
        items (list): List of tuples in format (FoodName, Category, Sales).

    Returns:
        tuple[str, int] | None:
            A tuple containing (FoodName, Sales) of the lowest selling item.
            Returns None if items list is empty.

    TODO:
        - Check if items list is empty (return None).
        - Use min() with a key on Sales column to find lowest.
        - Return (FoodName, Sales).
    """
    pass


def get_total_sales_by_category(items: list[tuple[str, str, int]]) -> dict[str, int]:
    """
    Calculates total sales for Veg and Non-Veg categories.

    Args:
        items (list): List of tuples in format (FoodName, Category, Sales).

    Returns:
        dict[str, int]:
            Dictionary containing total sales for each category.
            Example:
            {
                "Veg": 520,
                "Non-Veg": 300
            }

    TODO:
        - Initialize dictionary with {"Veg": 0, "Non-Veg": 0}.
        - Iterate through items and sum sales into the correct category.
        - Return the dictionary.
    """
    pass
