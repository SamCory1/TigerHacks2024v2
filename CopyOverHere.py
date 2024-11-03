import datetime
import json
import os

# Crop Recommendations Data and Functions
states = [
    "alabama", "alaska", "arizona", "arkansas", "california",
    "colorado", "connecticut", "delaware", "florida", "georgia",
    "hawaii", "idaho", "illinois", "indiana", "iowa",
    "kansas", "kentucky", "louisiana", "maine", "maryland",
    "massachusetts", "michigan", "minnesota", "mississippi", "missouri",
    "montana", "nebraska", "nevada", "new hampshire", "new jersey",
    "new mexico", "new york", "north carolina", "north dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina",
    "south dakota", "tennessee", "texas", "utah", "vermont",
    "virginia", "washington", "west virginia", "wisconsin", "wyoming"
]

seasons = ["spring", "summer", "fall"]

recommendations = {
    "alabama": {"spring": ["tomatoes", "peppers"], "summer": ["corn", "okra"], "fall": ["collards", "turnips"]},
    "alaska": {"spring": ["lettuce", "radishes"], "summer": ["potatoes", "carrots"], "fall": ["cabbage", "kale"]},
    "arizona": {"spring": ["peppers", "squash"], "summer": ["tomatoes", "melons"], "fall": ["garlic", "pumpkins"]},
    "arkansas": {"spring": ["peas", "lettuce"], "summer": ["corn", "rice"], "fall": ["pumpkins", "greens"]},
    "california": {"spring": ["tomatoes", "peppers"], "summer": ["grapes", "melons"], "fall": ["garlic", "winter squash"]},
    "colorado": {"spring": ["lettuce", "spinach"], "summer": ["corn", "beans"], "fall": ["pumpkins", "kale"]},
    "connecticut": {"spring": ["peas", "spinach"], "summer": ["zucchini", "beans"], "fall": ["turnips", "winter squash"]},
    "delaware": {"spring": ["peas", "lettuce"], "summer": ["tomatoes", "sweet corn"], "fall": ["collards", "turnips"]},
    "florida": {"spring": ["tomatoes", "peppers"], "summer": ["melons", "corn"], "fall": ["cabbage", "sweet potatoes"]},
    "georgia": {"spring": ["tomatoes", "peppers"], "summer": ["peanuts", "cotton"], "fall": ["sweet potatoes", "kale"]},
    "hawaii": {"spring": ["tomatoes", "peppers"], "summer": ["pineapples", "taro"], "fall": ["coffee", "sweet potatoes"]},
    "idaho": {"spring": ["potatoes", "peas"], "summer": ["corn", "beans"], "fall": ["winter squash", "garlic"]},
    "illinois": {"spring": ["lettuce", "beans"], "summer": ["corn", "tomatoes"], "fall": ["winter squash", "garlic"]},
    "indiana": {"spring": ["spinach", "carrots"], "summer": ["corn", "soybeans"], "fall": ["squash", "turnips"]},
    "iowa": {"spring": ["corn", "soybeans"], "summer": ["tomatoes", "peppers"], "fall": ["winter squash", "popcorn"]},
    "kansas": {"spring": ["wheat", "corn"], "summer": ["sorghum", "sunflowers"], "fall": ["winter wheat", "pumpkins"]},
    "kentucky": {"spring": ["lettuce", "peas"], "summer": ["corn", "tomatoes"], "fall": ["winter squash", "pumpkins"]},
    "louisiana": {"spring": ["tomatoes", "peppers"], "summer": ["okra", "sweet potatoes"], "fall": ["greens", "mustard"]},
    "maine": {"spring": ["lettuce", "peas"], "summer": ["tomatoes", "blueberries"], "fall": ["kale", "squash"]},
    "maryland": {"spring": ["radishes", "carrots"], "summer": ["cucumbers", "peppers"], "fall": ["kale", "squash"]},
    "massachusetts": {"spring": ["broccoli", "beets"], "summer": ["peppers", "eggplant"], "fall": ["collards", "pumpkins"]},
    "michigan": {"spring": ["peas", "spinach"], "summer": ["tomatoes", "cucumbers"], "fall": ["Brussels sprouts", "apples"]},
    "minnesota": {"spring": ["lettuce", "peas"], "summer": ["corn", "tomatoes"], "fall": ["squash", "pumpkins"]},
    "mississippi": {"spring": ["sweet potatoes", "corn"], "summer": ["tomatoes", "melons"], "fall": ["greens", "pumpkins"]},
    "missouri": {"spring": ["lettuce", "peas"], "summer": ["corn", "soybeans"], "fall": ["pumpkins", "garlic"]},
    "montana": {"spring": ["peas", "lettuce"], "summer": ["barley", "wheat"], "fall": ["winter wheat", "squash"]},
    "nebraska": {"spring": ["corn", "soybeans"], "summer": ["peppers", "melons"], "fall": ["pumpkins", "winter squash"]},
    "nevada": {"spring": ["lettuce", "spinach"], "summer": ["tomatoes", "peppers"], "fall": ["garlic", "winter squash"]},
    "new hampshire": {"spring": ["radishes", "carrots"], "summer": ["cucumbers", "corn"], "fall": ["Brussels sprouts", "garlic"]},
    "new jersey": {"spring": ["peas", "spinach"], "summer": ["tomatoes", "peppers"], "fall": ["pumpkins", "kale"]},
    "new mexico": {"spring": ["peppers", "squash"], "summer": ["beans", "tomatoes"], "fall": ["garlic", "melons"]},
    "new york": {"spring": ["radishes", "lettuce"], "summer": ["sweet corn", "tomatoes"], "fall": ["pumpkins", "garlic"]},
    "north carolina": {"spring": ["peppers", "tomatoes"], "summer": ["sweet potatoes", "okra"], "fall": ["collards", "turnips"]},
    "north dakota": {"spring": ["peas", "radishes"], "summer": ["barley", "sunflowers"], "fall": ["winter wheat", "pumpkins"]},
    "ohio": {"spring": ["lettuce", "peas"], "summer": ["sweet corn", "tomatoes"], "fall": ["pumpkins", "garlic"]},
    "oklahoma": {"spring": ["corn", "beans"], "summer": ["watermelons", "tomatoes"], "fall": ["winter wheat", "garlic"]},
    "oregon": {"spring": ["lettuce", "spinach"], "summer": ["tomatoes", "berries"], "fall": ["kale", "pumpkins"]},
    "pennsylvania": {"spring": ["spinach", "peas"], "summer": ["tomatoes", "peppers"], "fall": ["kale", "carrots"]},
    "rhode island": {"spring": ["carrots", "lettuce"], "summer": ["corn", "tomatoes"], "fall": ["kale", "onions"]},
    "south carolina": {"spring": ["tomatoes", "peppers"], "summer": ["okra", "sweet corn"], "fall": ["greens", "squash"]},
    "south dakota": {"spring": ["peas", "carrots"], "summer": ["corn", "soybeans"], "fall": ["pumpkins", "wheat"]},
    "tennessee": {"spring": ["lettuce", "radishes"], "summer": ["corn", "tomatoes"], "fall": ["sweet potatoes", "squash"]},
    "texas": {"spring": ["tomatoes", "peppers"], "summer": ["okra", "sweet potatoes"], "fall": ["collards", "squash"]},
    "utah": {"spring": ["lettuce", "peas"], "summer": ["tomatoes", "peppers"], "fall": ["pumpkins", "squash"]},
    "vermont": {"spring": ["spinach", "peas"], "summer": ["beans", "tomatoes"], "fall": ["winter squash", "potatoes"]},
    "virginia": {"spring": ["spinach", "asparagus"], "summer": ["tomatoes", "cucumbers"], "fall": ["Brussels sprouts", "garlic"]},
    "washington": {"spring": ["broccoli", "peas"], "summer": ["sweet corn", "tomatoes"], "fall": ["apples", "squash"]},
    "west virginia": {"spring": ["lettuce", "peas"], "summer": ["tomatoes", "beans"], "fall": ["kale", "squash"]},
    "wisconsin": {"spring": ["radishes", "peas"], "summer": ["sweet corn", "beans"], "fall": ["potatoes", "kale"]},
    "wyoming": {"spring": ["lettuce", "radishes"], "summer": ["beans", "corn"], "fall": ["winter squash", "garlic"]}
}

crop_prices = {
    "tomatoes": 3000,
    "peppers": 2500,
    "corn": 1500,
    "okra": 2000,
    "collards": 1000,
    "turnips": 900,
    "lettuce": 2500,
    "radishes": 1000,
    "potatoes": 2000,
    "carrots": 1800,
    "cabbage": 1500,
    "kale": 1200,
    "squash": 2000,
    "melons": 2500,
    "garlic": 3000,
    "pumpkins": 1800,
    "peas": 1200,
    "blueberries": 4000,
    "cucumbers": 2500,
    "eggplant": 2200,
    "soybeans": 1000,
    "wheat": 800,
    "sorghum": 1200,
    "sunflowers": 1500,
    "sweet potatoes": 2200,
    "berries": 3500,
    "apples": 3000,
    "greens": 1500,
}


def get_recommendations(state, season):
    state = state.lower()
    if state in recommendations and season in recommendations[state]:
        return recommendations[state][season]
    return []


def get_price(crop):
    return crop_prices.get(crop, 0)


# Crop and Livestock Classes for Watering and Feeding Reminders
class Crop:
    def __init__(self, name, base_frequency, last_watered=None):
        self.name = name
        self.base_frequency = base_frequency
        self.last_watered = last_watered

    def set_last_watered(self, date):
        self.last_watered = date

    def adjust_frequency(self, season, recent_rain):
        frequency = self.base_frequency
        if season == "summer":
            frequency = max(1, frequency - 1)
        elif season == "winter":
            frequency += 1
        if recent_rain:
            frequency += 1
        return frequency

    def needs_watering(self, season, recent_rain):
        if not self.last_watered:
            return True
        adjusted_frequency = self.adjust_frequency(season, recent_rain)
        days_since_watered = (datetime.date.today() - self.last_watered).days
        return days_since_watered >= adjusted_frequency


class Livestock:
    def __init__(self, name, feed_frequency, last_fed=None):
        self.name = name
        self.feed_frequency = feed_frequency
        self.last_fed = last_fed

    def set_last_fed(self, date):
        self.last_fed = date

    def needs_feeding(self):
        if not self.last_fed:
            return True
        days_since_fed = (datetime.date.today() - self.last_fed).days
        return days_since_fed >= self.feed_frequency


# Data Loading and Saving Functions
DATA_FILE = "farm_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            crop_data = {name: datetime.date.fromisoformat(date) for name, date in data.get("crops", {}).items()}
            livestock_data = {name: datetime.date.fromisoformat(date) for name, date in
                              data.get("livestock", {}).items()}
            return crop_data, livestock_data
    return {}, {}


def save_data(crops, livestock):
    data = {
        "crops": {crop.name: crop.last_watered.isoformat() for crop in crops if crop.last_watered is not None},
        "livestock": {animal.name: animal.last_fed.isoformat() for animal in livestock if animal.last_fed is not None}
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)


# Farm Expense Tracker
def expense_tracker():
    budget = float(input("Enter your budget for purchasing crops: "))
    print("Available states: ", ", ".join(states))
    state = input("Enter your state: ").strip().lower()
    season = input("Enter the current season (spring, summer, fall): ").strip().lower()

    if state not in states:
        print("Invalid state. Please run the program again.")
        return

    if season not in seasons:
        print("Invalid season. Please run the program again.")
        return

    crop_list = get_recommendations(state, season)

    if not crop_list:
        print("No recommendations available for your state and season.")
        return

    print("Recommended crops for {} in {}:".format(state.title(), season.title()))
    for index, crop in enumerate(crop_list, 1):
        print(f"{index}. {crop} (Cost per acre: ${get_price(crop)})")

    total_cost = 0
    crops_to_buy = []

    while total_cost < budget:
        crop_name = input("Enter the name of the crop you want to buy (or type 'exit' to finish): ").strip().lower()
        if crop_name == 'exit':
            break
        if crop_name in crop_list:
            amount = int(input(f"How many acres of {crop_name} do you want to buy? "))
            crop_cost = get_price(crop_name) * amount
            if total_cost + crop_cost <= budget:
                total_cost += crop_cost
                crops_to_buy.append((crop_name, amount))
                remaining_budget = budget - total_cost
                print(
                    f"{amount} acres of {crop_name} added. Total cost is now ${total_cost:.2f}. Remaining budget: ${remaining_budget:.2f}.")
            else:
                print("You don't have enough budget for this purchase.")
        else:
            print("Invalid crop name. Please try again.")

    if crops_to_buy:
        print("You have purchased:")
        for crop, acres in crops_to_buy:
            print(f"{acres} acres of {crop}")
    print(f"Total spent: ${total_cost:.2f}")
    print(f"Remaining budget: ${budget - total_cost:.2f}")


# Crop Yield Calculator
def crop_yield_calculator():
    crops = ["corn", "wheat", "sweet corn", "cotton", "apples", "rice", "soybeans"]
    crop_yield_list = [177.3, 37.1, 5, 813, 400, 7649, 50.6]
    crop_prices = [4.1475, 6.3909, 126, 0.7, 55, 0.97, 11.20]
    run = True

    while run:
        crop = input('Enter the crop you are planting (or "end" to stop): ').lower()
        if crop == 'end':
            run = False
            continue

        if crop in crops:
            acres = float(input("How many acres did you plant? "))
            index = crops.index(crop)
            crop_yield = round(acres * crop_yield_list[index])
            crop_sale = round(crop_yield * crop_prices[index], 2)
            print(f"Expected yield: {crop_yield} units of {crop}; Estimated value: ${crop_sale}")
        else:
            print("Invalid crop name. Please try again.")


# Main Function
def main():
    # Load data for watering and feeding schedules
    crop_data, livestock_data = load_data()

    # Initialize crops
    crops = [
        Crop("Corn", 4, crop_data.get("Corn")),
        Crop("Wheat", 7, crop_data.get("Wheat")),
        # Add other crops as needed
    ]

    # Initialize livestock
    livestock = [
        Livestock("Cows", 1, livestock_data.get("Cows")),
        # Add other animals as needed
    ]

    # Farm management options
    while True:
        choice = input(
            "Choose an option: (1) Expense Tracker, (2) Yield Calculator, (3) Watering and Feeding, (4) Exit: ")

        if choice == "1":
            expense_tracker()
        elif choice == "2":
            crop_yield_calculator()
        elif choice == "3":
            print("Managing watering and feeding schedules...")
            # Call any additional functions for updating watering/feeding here
        elif choice == "4":
            print("Exiting farm manager.")
            break
        else:
            print("Invalid choice, please try again.")

    # Save data at the end
    save_data(crops, livestock)


if __name__ == "__main__":
    main()