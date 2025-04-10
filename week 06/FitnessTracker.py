#Author : Diogo Rangel Dos Santos
#Fitness Tracker

import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

WORKOUT_FILE = "workout.csv"

#------------------------
#Core Functions
#------------------------

def log_workout():
    """Logs a workout entry from user input."""
    print("\nLog New Workout")
    date = input("Date (YYYY-MM-DD): ")
    exercise = input("Exercise Type (e.g. Running, Bench Press): ")
    sets = input("Sets (leave blank if not applicable): ")
    reps = input("Reps (leave blank if not applicable): ")
    weight = input("Weight (kg) (leave blank if not applicable): ")
    duration = input("Duration (minutes): ")
    distance = input("Distance (km) (leave blank if not applicable): ")

    with open(WORKOUT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, exercise, sets, reps, weight, duration, distance])
    print("Workout logged successfully!\n")


def view_progress():
    """Displays the logged workout history."""
    if not os.path.exists(WORKOUT_FILE):
        print("No workouts logged yet.\n")
        return

    print("\nWorkout History:")
    with open(WORKOUT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


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
                if row[4]:
                    total_weight += float(row[4])
                    weight_entries += 1
                if row[5]:
                    total_duration += float(row[5])
                if row[6]:
                    total_distance += float(row[6])
            except ValueError:
                continue

    print("\nProgress Trends:")
    if weight_entries:
        print(f"- Average Weight Lifted: {total_weight / weight_entries:.2f} kg")
    print(f"- Total Distance Run: {total_distance:.2f} km")
    print(f"- Total Time Exercising: {total_duration:.2f} minutes\n")


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
                if row[0] and row[5]:
                    dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
                    durations.append(float(row[5]))
            except ValueError:
                continue

    if dates and durations:
        plt.figure(figsize=(10, 5))
        plt.plot(dates, durations, marker='o', linestyle='-', color='blue')
        plt.title('Workout Duration Over Time')
        plt.xlabel('Date')
        plt.ylabel('Duration (minutes)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Insufficient data for visualization.\n")


def export_data():
    """Exports workout data to a CSV file."""
    if not os.path.exists(WORKOUT_FILE):
        print("No data available to export.\n")
        return

    export_file = "exported_workouts.csv"
    with open(WORKOUT_FILE, mode='r') as src, open(export_file, mode='w', newline='') as dst:
        dst.write(src.read())
    print(f"Data exported to {export_file}\n")

# ----------------------------
# Main Menu
# ----------------------------
def main():
    while True:
        print("--- Fitness Progress Tracker ---")
        print("1. Log Workout")
        print("2. View Progress")
        print("3. Calculate Trends")
        print("4. Generate Report")
        print("5. Export Data")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == '__main__':
    main()
