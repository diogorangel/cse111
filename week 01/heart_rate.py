"""When you physically exercise to strengthen your heart, you should 
maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate."""

# Get user input for age
age = int(input("Enter your age: "))
max_heart_rate = 220 - age

# Calculate target heart rate range (65% - 85% of max heart rate)
slowest_rate = max_heart_rate * 0.65
fastest_rate = max_heart_rate * 0.85

#display Results
print("\nYour maximum heart rate is", max_heart_rate, "beats per minute.")
print(f"Slowest: {slowest_rate:.1f} beats per minute")
print(f"Fastest: {fastest_rate:.1f} beats per minute")