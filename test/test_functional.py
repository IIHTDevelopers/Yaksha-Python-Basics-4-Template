# test/test_all_management_systems.py

import unittest
import sys
import os
import pandas as pd

# Adjusting the path to import TestUtils and the required modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from OnlineFoodDeliverySystem import get_menu, calculate_bill, save_order
from BloodBankManagementSystem import (
    get_blood_bank_data,
    add_new_blood_group,

    get_total_units,
    find_scarcity
)



class TestManagementSystems(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # ===== Online Food Delivery System =====
        self.menu = get_menu()
        self.orders = [
            ("Pizza", 2),
            ("Burger", 1),
            ("Pasta", 3),
            ("Fries", 2),
            ("Cola", 2)
        ]
        self.expected_total_bill = 54.75
        self.expected_order_summary = [
            "Pizza x2 = $17.00",
            "Burger x1 = $5.00",
            "Pasta x3 = $21.75",
            "Fries x2 = $7.00",
            "Cola x2 = $4.00"
        ]
        self.food_filename = "test_food_orders.txt"

        # ===== Blood Bank Management System =====
        self.blood_bank = get_blood_bank_data()



    # ========== Online Food Delivery System Tests ==========
    def test_get_menu(self):
        """
        Test case for get_menu() function.
        """
        try:
            result = get_menu()
            expected_result = {
                "Pizza": 8.50,
                "Burger": 5.00,
                "Pasta": 7.25,
                "Fries": 3.50,
                "Cola": 2.00
            }
            if result == expected_result:
                self.test_obj.yakshaAssert("TestGetMenu", True, "functional")
                print("TestGetMenu = Passed")
            else:
                self.test_obj.yakshaAssert("TestGetMenu", False, "functional")
                print("TestGetMenu = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestGetMenu", False, "functional")
            print(f"TestGetMenu = Failed ")

    def test_calculate_bill(self):
        """
        Test case for calculate_bill() function.
        """
        try:
            total_bill, order_summary = calculate_bill(self.orders, self.menu)
            result = (
                round(total_bill, 2) == self.expected_total_bill and
                order_summary == self.expected_order_summary
            )
            if result:
                self.test_obj.yakshaAssert("TestCalculateBill", True, "functional")
                print("TestCalculateBill = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateBill", False, "functional")
                print("TestCalculateBill = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateBill", False, "functional")
            print(f"TestCalculateBill = Failed ")

    def test_save_order(self):
        """
        Test case for save_order() function.
        """
        try:
            filename = save_order(self.expected_order_summary, self.expected_total_bill, self.food_filename)
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    content = file.read()
                result = "Total Bill: $54.75" in content
                if result:
                    self.test_obj.yakshaAssert("TestSaveOrder", True, "functional")
                    print("TestSaveOrder = Passed")
                else:
                    self.test_obj.yakshaAssert("TestSaveOrder", False, "functional")
                    print("TestSaveOrder = Failed")
            else:
                self.test_obj.yakshaAssert("TestSaveOrder", False, "functional")
                print("TestSaveOrder = Failed ")
            os.remove(filename)
        except Exception as e:
            self.test_obj.yakshaAssert("TestSaveOrder", False, "functional")
            print(f"TestSaveOrder = Failed")

    # ========== Blood Bank Management System Tests ==========
    def test_add_new_blood_group(self):
        """
        Test case for add_new_blood_group() function.
        """
        result = add_new_blood_group(self.blood_bank, "P+", 10)
        added = not result[result["Blood Group"] == "P+"].empty
        if added:
            self.test_obj.yakshaAssert("TestAddNewBloodGroup", True, "functional")
            print("TestAddNewBloodGroup = Passed")
        else:
            self.test_obj.yakshaAssert("TestAddNewBloodGroup", False, "functional")
            print("TestAddNewBloodGroup = Failed")


    def test_get_total_units(self):
        """
        Test case for get_total_units() function.
        """
        total_units = get_total_units(self.blood_bank)
        expected_total = self.blood_bank["Units Available"].sum()
        result = total_units == expected_total
        if result:
            self.test_obj.yakshaAssert("TestGetTotalUnits", True, "functional")
            print("TestGetTotalUnits = Passed")
        else:
            self.test_obj.yakshaAssert("TestGetTotalUnits", False, "functional")
            print("TestGetTotalUnits = Failed")


# test/test_employee_leave_management.py

import unittest
import sys
import os

# Adjusting the path to import TestUtils and the employee leave management module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from EmployeeLeaveManagementSystem import (
    get_employee_data,
    process_leave_requests,

)


class TestEmployeeLeaveManagement(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

        # Sample Data for Testing
        self.employees = get_employee_data()
        self.leave_requests = [
            ("E001", 3),  # Approved
            ("E003", 2),  # Approved
            ("E005", 6),  # Denied (Insufficient Balance)
            ("E002", 1),  # Approved
            ("E004", 5),  # Approved
            ("E999", 3),  # Non-existent Employee ID
            ("E003", -2)  # Invalid Negative Leave Request
        ]

        # Expected Data for Verification
        self.expected_leave_summary = [
            "John Doe granted 3 days leave. Remaining: 9 days",
            "Bob Johnson granted 2 days leave. Remaining: 6 days",
            "Michael Brown leave request denied. Insufficient balance.",
            "Alice Smith granted 1 days leave. Remaining: 9 days",
            "Emma Davis granted 5 days leave. Remaining: 10 days",
            "Employee ID E999 not found.",
            "Invalid leave request for Bob Johnson. Negative days not allowed."
        ]
        self.filename = "test_leave_status.txt"

    def test_get_employee_data(self):
        """
        Test case for get_employee_data() function.
        """
        try:
            result = get_employee_data()
            expected_result = {
                "E001": {"name": "John Doe", "leave_balance": 12},
                "E002": {"name": "Alice Smith", "leave_balance": 10},
                "E003": {"name": "Bob Johnson", "leave_balance": 8},
                "E004": {"name": "Emma Davis", "leave_balance": 15},
                "E005": {"name": "Michael Brown", "leave_balance": 5}
            }
            if result == expected_result:
                self.test_obj.yakshaAssert("TestGetEmployeeData", True, "functional")
                print("TestGetEmployeeData = Passed")
            else:
                self.test_obj.yakshaAssert("TestGetEmployeeData", False, "functional")
                print("TestGetEmployeeData = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestGetEmployeeData", False, "functional")
            print(f"TestGetEmployeeData = Failed ")

    def test_process_leave_requests(self):
        """
        Test case for process_leave_requests() function.
        """
        try:
            result = process_leave_requests(self.employees, self.leave_requests)
            if result == self.expected_leave_summary:
                self.test_obj.yakshaAssert("TestProcessLeaveRequests", True, "functional")
                print("TestProcessLeaveRequests = Passed")
            else:
                self.test_obj.yakshaAssert("TestProcessLeaveRequests", False, "functional")
                print("TestProcessLeaveRequests = Failed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestProcessLeaveRequests", False, "functional")
            print(f"TestProcessLeaveRequests = Failed ")



if __name__ == '__main__':
    unittest.main()
