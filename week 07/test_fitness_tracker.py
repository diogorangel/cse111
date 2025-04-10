# Author: Diogo Rangel Dos Santos
#Test Fitness Tracker

import unittest
import os
import csv
from datetime import datetime
from unittest.mock import patch, mock_open
import builtins

# Import functions from your FitnessTracker.py file
import FitnessTracker as ft

TEST_WORKOUT_FILE = "test_workout.csv"


class TestFitnessTracker(unittest.TestCase):

    def setUp(self):
        """Setup a test workout CSV file."""
        ft.WORKOUT_FILE = TEST_WORKOUT_FILE
        with open(TEST_WORKOUT_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["2024-04-01", "Running", "", "", "", "30", "5"])
            writer.writerow(["2024-04-02", "Bench Press", "3", "10", "60", "45", ""])
            writer.writerow(["2024-04-03", "Cycling", "", "", "", "60", "15"])

    def tearDown(self):
        """Remove the test CSV file."""
        if os.path.exists(TEST_WORKOUT_FILE):
            os.remove(TEST_WORKOUT_FILE)
        if os.path.exists("report_2.txt"):
            os.remove("report_2.txt")
        if os.path.exists("exported_workouts.csv"):
            os.remove("exported_workouts.csv")

    def test_valid_date(self):
        with patch('builtins.input', return_value="2024-04-09"):
            self.assertEqual(ft.get_valid_date("Date: "), "2024-04-09")

    def test_invalid_date_then_valid(self):
        with patch('builtins.input', side_effect=["invalid", "2024-04-10"]):
            self.assertEqual(ft.get_valid_date("Date: "), "2024-04-10")

    def test_valid_input_optional(self):
        with patch('builtins.input', return_value=""):
            self.assertEqual(ft.get_valid_input("Sets: ", int), "")

    def test_valid_input_non_optional(self):
        with patch('builtins.input', return_value="25"):
            self.assertEqual(ft.get_valid_input("Duration: ", float, optional=False), 25.0)

    def test_generate_text_report_creates_file(self):
        ft.generate_text_report()
        self.assertTrue(os.path.exists("report_2.txt"))
        with open("report_2.txt", encoding="utf-8") as file:
            contents = file.read()
            self.assertIn("Fitness Progress Report", contents)
            self.assertIn("Running", contents)

    def test_export_data(self):
        ft.export_data()
        self.assertTrue(os.path.exists("exported_workouts.csv"))
        with open("exported_workouts.csv", 'r') as file:
            content = file.read()
            self.assertIn("Running", content)

    def test_calculate_trends_output(self):
        # This will just check that the function runs without crashing
        try:
            ft.calculate_trends()
        except Exception as e:
            self.fail(f"calculate_trends() raised an exception {e}")


if __name__ == "__main__":
    unittest.main()
