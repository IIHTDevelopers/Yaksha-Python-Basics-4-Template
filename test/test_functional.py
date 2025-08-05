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
            self.test_obj.yakshaAssert("TestTotalLeavesTaken", result == expected, "functional")
            print("TestTotalLeavesTaken =", "Passed" if result == expected else "Failed")
        except Exception as e:
            print("TestTotalLeavesTaken = Failed due to Exception:", e)

    def test_employees_exceeding_leaves(self):
        try:
            result = employees_exceeding_leaves(self.test_df, limit=5)
            expected_ids = [103]
            actual_ids = result["Employee ID"].tolist()
            self.test_obj.yakshaAssert("TestExceedingLeaves", actual_ids == expected_ids, "functional")
            print("TestExceedingLeaves =", "Passed" if actual_ids == expected_ids else "Failed")
        except Exception as e:
            print("TestExceedingLeaves = Failed due to Exception:", e)

    def test_average_leaves(self):
        try:
            result = average_leaves_taken(self.test_df)
            expected = 4.0
            self.test_obj.yakshaAssert("TestAverageLeaves", result == expected, "functional")
            print("TestAverageLeaves =", "Passed" if result == expected else "Failed")
        except Exception as e:
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
            self.test_obj.yakshaAssert("TestTotalUnits", result == expected, "functional")
            print("TestTotalUnits =", "Passed" if result == expected else "Failed")
        except Exception as e:
            print("TestTotalUnits = Failed due to Exception:", e)

    def test_low_stock(self):
        try:
            result = low_stock_groups(self.blood_df, threshold=5)
            expected_groups = ["O-", "AB-"]
            actual_groups = result["Blood Group"].tolist()
            self.test_obj.yakshaAssert("TestLowStockGroups", actual_groups == expected_groups, "functional")
            print("TestLowStockGroups =", "Passed" if actual_groups == expected_groups else "Failed")
        except Exception as e:
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
            expected = [("Pizza", "Veg"), ("Chicken Wings", "Non-Veg"), ("Pasta", "Veg"), ("Fish Fry", "Non-Veg")]
            self.test_obj.yakshaAssert("TestReadFoodItems", result == expected, "functional")
            print("TestReadFoodItems =", "Passed" if result == expected else "Failed")
        except Exception as e:
            print("TestReadFoodItems = Failed due to Exception:", e)

    def test_classify_food_items(self):
        try:
            food_list = [("Pizza", "Veg"), ("Chicken Wings", "Non-Veg"), ("Pasta", "Veg"), ("Fish Fry", "Non-Veg")]
            result = classify_food_items(food_list)
            expected = {
                "Veg": ["Pizza", "Pasta"],
                "Non-Veg": ["Chicken Wings", "Fish Fry"]
            }
            self.test_obj.yakshaAssert("TestClassifyFoodItems", result == expected, "functional")
            print("TestClassifyFoodItems =", "Passed" if result == expected else "Failed")
        except Exception as e:
            print("TestClassifyFoodItems = Failed due to Exception:", e)
