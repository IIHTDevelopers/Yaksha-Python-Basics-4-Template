import unittest
from food_sales import read_food_sales, find_lowest_sales_item
from yaksha import YakshaTest

class TestFoodSales(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = YakshaTest()
        cls.filename = "food_sales.txt"
        # Create test file
        with open(cls.filename, "w") as f:
            f.write("Pizza,Veg,120\n")
            f.write("Chicken Wings,Non-Veg,80\n")
            f.write("Pasta,Veg,150\n")
            f.write("Fish Fry,Non-Veg,60\n")
            f.write("Noodles,Veg,200\n")
            f.write("Lamb Curry,Non-Veg,90\n")
            f.write("Salad,Veg,50\n")
            f.write("Prawn Fry,Non-Veg,70\n")
        # Load data once for reuse
        cls.data = read_food_sales(cls.filename)

    # ✅ Test 1: Reading food sales data
    def test_read_food_sales(self):
        try:
            expected = [
                ("Pizza", "Veg", 120),
                ("Chicken Wings", "Non-Veg", 80),
                ("Pasta", "Veg", 150),
                ("Fish Fry", "Non-Veg", 60),
                ("Noodles", "Veg", 200),
                ("Lamb Curry", "Non-Veg", 90),
                ("Salad", "Veg", 50),
                ("Prawn Fry", "Non-Veg", 70),
            ]
            result = self.data
            self.assertEqual(result, expected)
            self.test_obj.yakshaAssert("test_read_food_sales", True, "functional")
            print("test_read_food_sales = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_read_food_sales", False, "exception")
            print("test_read_food_sales = Failed")

    # ✅ Test 2: Finding lowest sales item
    def test_find_lowest_sales_item(self):
        try:
            lowest = find_lowest_sales_item(self.data)
            self.assertEqual(lowest, ("Salad", 50))  # Salad has lowest sales
            self.test_obj.yakshaAssert("test_find_lowest_sales_item", True, "functional")
            print("test_find_lowest_sales_item = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_find_lowest_sales_item", False, "exception")
            print("test_find_lowest_sales_item = Failed")


if __name__ == "__main__":
    unittest.main()
