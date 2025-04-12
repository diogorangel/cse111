# Author: Diogo Rangel Dos Santos
# Fitness Tracker

import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib

# Support emojis in plots
matplotlib.rcParams['font.family'] = 'Segoe UI Emoji'

WORKOUT_FILE = "workout.csv"

# ------------------------
# Helper: Input Validators
# ------------------------

#First Fuction: get_valid_input
def get_valid_input(prompt, input_type=float, optional=True):
    """Prompt the user until valid input is entered."""
    while True:
        value = input(prompt)
        if optional and value.strip() == "":
            return ""
        try:
            return input_type(value)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
            
#Second Fuction: get_valid_date
def get_valid_date(prompt):
    """Prompt for a valid date in YYYY-MM-DD format."""
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

# ------------------------
# Core Functions
# ------------------------

#Third Fuction: log_workout
def log_workout():
    """Logs a workout entry from user input with validation."""
    print("\nLog New Workout")
    date = get_valid_date("Date (YYYY-MM-DD): ")
    exercise = input("Exercise Type (e.g. Running, Bench Press): ")
    sets = get_valid_input("Sets (leave blank if not applicable): ", int)
    reps = get_valid_input("Reps (leave blank if not applicable): ", int)
    weight = get_valid_input("Weight (kg) (leave blank if not applicable): ", float)
    duration = get_valid_input("Duration (minutes): ", float, optional=False)
    distance = get_valid_input("Distance (km) (leave blank if not applicable): ", float)

    with open(WORKOUT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, exercise, sets, reps, weight, duration, distance])
    print("✅ Workout logged successfully!\n")

#Fourth Fuction: view_progress
def view_progress():
    """Displays the logged workout history."""
    if not os.path.exists(WORKOUT_FILE):
        print("No workouts logged yet.\n")
        return

    print("\n📋 Workout History:")
    with open(WORKOUT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

#Fifth Fuction: calculate_trends
def calculate_trends():
    """Calculates average stats and prints progress info."""
    if not os.path.exists(WORKOUT_FILE):
        print("No data to calculate trends.\n")
        return

    total_weight = 0
    weight_entries = 0
    total_distance = 0
    total_duration = 0

    with open(WORKOUT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                weight = row[4].strip()
                duration = row[5].strip()
                distance = row[6].strip()

                if weight:
                    total_weight += float(weight)
                    weight_entries += 1
                if duration:
                    total_duration += float(duration)
                if distance:
                    total_distance += float(distance)
            except (ValueError, IndexError):
                continue

    print("\n📈 Progress Trends:")
    if weight_entries:
        print(f"- Average Weight Lifted: {total_weight / weight_entries:.2f} kg")
    print(f"- Total Distance Run: {total_distance:.2f} km")
    print(f"- Total Time Exercising: {total_duration:.2f} minutes\n")

#Sixth Fuction: generate_report
def generate_report():
    """Generates a matplotlib line graph of workout duration over time."""
    if not os.path.exists(WORKOUT_FILE):
        print("No data available for report.\n")
        return

    dates = []
    durations = []

    with open(WORKOUT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                if row[0].strip() and row[5].strip():
                    date = datetime.strptime(row[0].strip(), "%Y-%m-%d")
                    duration = float(row[5].strip())
                    dates.append(date)
                    durations.append(duration)
            except (ValueError, IndexError):
                continue

    if len(dates) != len(durations):
        print("Mismatch in data. Skipping report generation.\n")
        return

    if dates and durations:
        plt.figure(figsize=(10, 5))
        plt.plot(dates, durations, marker='o', linestyle='-', color='blue')
        plt.title('🏋️‍♂️ Workout Duration Over Time')
        plt.xlabel('Date')
        plt.ylabel('Duration (minutes)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Insufficient data for visualization.\n")

#seventh Fuction: export_data
def export_data():
    """Exports workout data to a CSV file."""
    if not os.path.exists(WORKOUT_FILE):
        print("No data available to export.\n")
        return

    export_file = "exported_workouts.csv"
    with open(WORKOUT_FILE, mode='r') as src, open(export_file, mode='w', newline='') as dst:
        dst.write(src.read())
    print(f"📤 Data exported to {export_file}\n")

#eighth Fuction: generate_text_report
def generate_text_report():
    """Generates a text-based report and saves it to report_2.txt."""
    if not os.path.exists(WORKOUT_FILE):
        print("No data available for report.\n")
        return

    total_weight = 0
    weight_entries = 0
    total_distance = 0
    total_duration = 0
    exercise_count = {}

    with open(WORKOUT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                exercise = row[1]
                if exercise:
                    exercise_count[exercise] = exercise_count.get(exercise, 0) + 1
                if row[4]:  # weight
                    total_weight += float(row[4])
                    weight_entries += 1
                if row[5]:  # duration
                    total_duration += float(row[5])
                if row[6]:  # distance
                    total_distance += float(row[6])
            except (IndexError, ValueError):
                continue

    with open("report_2.txt", mode="w", encoding="utf-8") as report:
        report.write("🏋️ Fitness Progress Report 🏋️\n")
        report.write("============================\n")
        report.write(f"Total Time Exercising: {total_duration:.2f} minutes\n")
        report.write(f"Total Distance Run: {total_distance:.2f} km\n")
        if weight_entries:
            report.write(f"Average Weight Lifted: {total_weight / weight_entries:.2f} kg\n")
        report.write("\nWorkout Counts by Type:\n")
        for exercise, count in exercise_count.items():
            report.write(f" - {exercise}: {count} sessions\n")

    print("📄 Text report saved to report_2.txt\n")

# ------------------------
# Main Menu
# ------------------------

#ninth Fuction: main (mainly for the menu)
def main():
    while True:
        print("--- 🏋️ Fitness Progress Tracker ---")
        print("1. Log Workout")
        print("2. View Progress")
        print("3. Calculate Trends")
        print("4. Generate Report")
        print("5. Export Data")
        print("6. Generate Text Report")
        print("7. Exit")
        choice = input("Select an option (1-7): ")

        if choice == '1':
            log_workout()
        elif choice == '2':
            view_progress()
        elif choice == '3':
            calculate_trends()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            export_data()
        elif choice == '6':
            generate_text_report()
        elif choice == '7':
            print("👋 Goodbye and keep pushing!")
            break
        else:
            print("❌ Invalid option. Please try again.\n")

if __name__ == '__main__':
    main()
# End of the Fitness Tracker program