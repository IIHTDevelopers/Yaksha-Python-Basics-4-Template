import unittest
import pandas as pd
from EmployeeLeaveManagementSystem import total_leaves_taken, employees_exceeding_leaves, average_leaves_taken
from test.TestUtils import TestUtils

class TestEmployeeLeave(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.test_df = pd.DataFrame({
            "Employee ID": [101, 102, 103, 104],
            "Name": ["Alice", "Bob", "Charlie", "Diana"],
            "Leaves Taken": [5, 2, 8, 1]
        })

    def test_total_leaves_taken(self):
        try:
            result = total_leaves_taken(self.test_df)
            expected = 16
            status = result == expected
            self.test_obj.yakshaAssert("TestTotalLeavesTaken", status, "functional")
            print("TestTotalLeavesTaken =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalLeavesTaken", False, "functional")
            print("TestTotalLeavesTaken = Failed due to Exception:", e)

    def test_employees_exceeding_leaves(self):
        try:
            result = employees_exceeding_leaves(self.test_df, limit=5)
            expected_ids = [103]
            actual_ids = result["Employee ID"].tolist()
            status = actual_ids == expected_ids
            self.test_obj.yakshaAssert("TestExceedingLeaves", status, "functional")
            print("TestExceedingLeaves =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestExceedingLeaves", False, "functional")
            print("TestExceedingLeaves = Failed due to Exception:", e)

    def test_average_leaves(self):
        try:
            result = average_leaves_taken(self.test_df)
            expected = 4.0
            status = result == expected
            self.test_obj.yakshaAssert("TestAverageLeaves", status, "functional")
            print("TestAverageLeaves =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestAverageLeaves", False, "functional")
            print("TestAverageLeaves = Failed due to Exception:", e)

import unittest
import pandas as pd
from BloodBankManagementSystem import total_units, low_stock_groups
from test.TestUtils import TestUtils

class TestBloodBank(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.blood_df = pd.DataFrame({
            "Blood Group": ["A+", "B+", "O-", "AB-"],
            "Units Available": [10, 8, 4, 3]
        })

    def test_total_units(self):
        try:
            result = total_units(self.blood_df)
            expected = 25
            status = result == expected
            self.test_obj.yakshaAssert("TestTotalUnits", status, "functional")
            print("TestTotalUnits =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalUnits", False, "functional")
            print("TestTotalUnits = Failed due to Exception:", e)

    def test_low_stock(self):
        try:
            result = low_stock_groups(self.blood_df, threshold=5)
            expected_groups = ["O-", "AB-"]
            actual_groups = result["Blood Group"].tolist()
            status = actual_groups == expected_groups
            self.test_obj.yakshaAssert("TestLowStockGroups", status, "functional")
            print("TestLowStockGroups =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestLowStockGroups", False, "functional")
            print("TestLowStockGroups = Failed due to Exception:", e)
import unittest
import os
from test.TestUtils import TestUtils
from food import read_food_sales, find_lowest_sales_item

class TestFoodProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.filename = "food_sales.txt"
        with open(cls.filename, "w") as f:
            f.write("Pizza,Veg,120\n")
            f.write("Chicken Wings,Non-Veg,80\n")
            f.write("Pasta,Veg,150\n")
            f.write("Fish Fry,Non-Veg,60\n")
            f.write("Noodles,Veg,200\n")
            f.write("Lamb Curry,Non-Veg,90\n")
            f.write("Salad,Veg,50\n")
            f.write("Prawn Fry,Non-Veg,70\n")

        cls.expected_items = [
            ("Pizza", "Veg", 120),
            ("Chicken Wings", "Non-Veg", 80),
            ("Pasta", "Veg", 150),
            ("Fish Fry", "Non-Veg", 60),
            ("Noodles", "Veg", 200),
            ("Lamb Curry", "Non-Veg", 90),
            ("Salad", "Veg", 50),
            ("Prawn Fry", "Non-Veg", 70),
        ]

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.filename):
            os.remove(cls.filename)

    def test_read_food_sales(self):
        try:
            items = read_food_sales(self.filename)
            self.assertEqual(items, self.expected_items)
            self.test_obj.yakshaAssert("test_read_food_sales", True, "functional")
            print("test_read_food_sales = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_read_food_sales", False, "exception")
            print("test_read_food_sales = Failed")

    def test_find_lowest_sales_item(self):
        try:
            items = read_food_sales(self.filename)
            lowest = find_lowest_sales_item(items)
            self.assertEqual(lowest, ("Salad", 50))  # Salad has lowest sales
            self.test_obj.yakshaAssert("test_find_lowest_sales_item", True, "functional")
            print("test_find_lowest_sales_item = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_find_lowest_sales_item", False, "exception")
            print("test_find_lowest_sales_item = Failed")



if __name__ == "__main__":
    unittest.main()
