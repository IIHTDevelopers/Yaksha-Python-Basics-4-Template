import pandas as pd

# ✅ Initial employee leave data
employee_ids = [101, 102, 103, 104]
employee_names = ["Alice", "Bob", "Charlie", "Diana"]
leaves_taken = [5, 2, 8, 1]

# Creating the DataFrame
leave_df = pd.DataFrame({
    "Employee ID": employee_ids,
    "Name": employee_names,
    "Leaves Taken": leaves_taken
})


# TODO: Function 1 - Calculate the total number of leaves taken
def total_leaves_taken(df):
    # Return total sum of "Leaves Taken"
    pass


# TODO: Function 2 - Get employees with leaves greater than a given limit
def employees_exceeding_leaves(df, limit=5):
    # Return DataFrame rows where "Leaves Taken" > limit
    pass


# TODO: Function 3 - Calculate the average number of leaves taken
def average_leaves_taken(df):
    # Return average of "Leaves Taken"
    pass


# Optional: Sample testing block
if __name__ == "__main__":
    # TODO: Print total leaves taken
    print("Total Leaves Taken:", total_leaves_taken(leave_df))

    # TODO: Print employees with excessive leave
    print("\nEmployees with Leaves > 5:")
    print(employees_exceeding_leaves(leave_df, limit=5))

    # TODO: Print average leaves taken
    print("\nAverage Leaves Taken:", average_leaves_taken(leave_df))
