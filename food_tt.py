import datetime
import random

def read_meal_options(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    meal_options = {}
    current_category = None
    for line in lines:
        line = line.strip()
        if line:
            if line.startswith("[") and line.endswith("]"):
                current_category = line[1:-1]
                meal_options[current_category] = []
            else:
                meal_options[current_category].append(line)

    return meal_options

def shuffle_meal_options(meal_options):
    for category in meal_options:
        random.shuffle(meal_options[category])

# Read meal options from the "foodTimeTable" file
all_meals = read_meal_options('/workDone/foodT/all_food.txt')

# Get the current week of the year
current_week = datetime.date.today().isocalendar()[1]

# Define days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Define colors for the terminal
GREEN = '\033[92m'
RED = '\033[91m'
END_COLOR = '\033[0m'

# Print the meal plan for each day of each week
for week in range(current_week, current_week + len(days_of_week)):
    print(f"--- Week {week} ---")

    # Shuffle meal options for each week
    shuffle_meal_options(all_meals)

    for day in days_of_week:
        print(f"{day}:")
        selected_meals = all_meals.copy()

        # Select one meal plan for each day, including breakfast, lunch, and dinner
        for category in all_meals:
            selected_meals[category] = random.choice(all_meals[category])

        for category, meals in selected_meals.items():
            if category.startswith("Vegetarian"):
                print(f"\n{GREEN}- {category}:")
            else:
                print(f"\n{RED}- {category}:")
            print(f"  - {meals}")
        print()
