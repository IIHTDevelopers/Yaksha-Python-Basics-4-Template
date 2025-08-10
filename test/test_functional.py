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
from food import read_food_items, classify_food_items
from test.TestUtils import TestUtils

class TestFoodDelivery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.test_file = "test_food_items.txt"
        with open(cls.test_file, "w", encoding="utf-8") as f:
            f.write("Pizza,Veg\nChicken Wings,Non-Veg\nPasta,Veg\nFish Fry,Non-Veg")

    def test_read_food_items(self):
        try:
            result = read_food_items(self.test_file)
            expected = [("Pizza", "Veg"), ("Chicken Wings", "Non-Veg"), ("Pasta", "Veg"), ("Fish Fry", "Non-Veg"),("Noddles", "Veg")("lamb", "Non-Veg")]
            status = result == expected
            self.test_obj.yakshaAssert("TestReadFoodItems", status, "functional")
            print("TestReadFoodItems =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestReadFoodItems", False, "functional")
            print("TestReadFoodItems = Failed due to Exception:", e)

    def test_classify_food_items(self):
        try:
            food_list = [("Pizza", "Veg"), ("Chicken Wings", "Non-Veg"), ("Pasta", "Veg"), ("Fish Fry", "Non-Veg"),("Noddles", "Veg")("lamb", "Non-Veg")]
            result = classify_food_items(food_list)
            expected = {
                "Veg": ["Pizza", "Pasta","Noodles"],
                "Non-Veg": ["Chicken Wings", "Fish Fry","lamb"]
            }
            status = result == expected
            self.test_obj.yakshaAssert("TestClassifyFoodItems", status, "functional")
            print("TestClassifyFoodItems =", "Passed" if status else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestClassifyFoodItems", False, "functional")
            print("TestClassifyFoodItems = Failed due to Exception:", e)

