import datetime
import json
import os

# crop class for watering reminder
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
            frequency = max(1, frequency - 1)  # Water more frequently in summer
        elif season == "winter":
            frequency += 1  # Water less frequently in winter
        if recent_rain:
            frequency += 1  # Delay watering if it recently rained
        return frequency

    def needs_watering(self, season, recent_rain):
        adjusted_frequency = self.adjust_frequency(season, recent_rain)
        days_since_watered = (datetime.date.today() - self.last_watered).days
        return days_since_watered >= adjusted_frequency

# livestock class for feeding scheduler
class Livestock:
    def __init__(self, name, feed_frequency, last_fed=None):
        self.name = name
        self.feed_frequency = feed_frequency
        self.last_fed = last_fed

    def set_last_fed(self, date):
        self.last_fed = date

    def needs_feeding(self):
        days_since_fed = (datetime.date.today() - self.last_fed).days
        return days_since_fed >= self.feed_frequency # only return true if feeding is due

# File to save watering and feeding data
DATA_FILE = "farm_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            crop_data = {name: datetime.date.fromisoformat(date) for name, date in data.get("crops", {}).items()}
            livestock_data = {name: datetime.date.fromisoformat(date) for name, date in data.get("livestock", {}).items()}
            return crop_data, livestock_data
    return {}, {}

def save_data(crops, livestock):
    data = {
        "crops": {crop.name: crop.last_watered.isoformat() for crop in crops if crop.last_watered is not None},
        "livestock": {animal.name: animal.last_fed.isoformat() for animal in livestock if animal.last_fed is not None}
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def parse_date(date_str):
    """Attempts to parse the date string in multiple formats."""
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%B %d, %Y"):
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError("Invalid date format: Please try again.")


def main():
    # Load data
    crop_data, livestock_data = load_data()

    # Initialize crops
    crops = [
        Crop("Corn", 4, crop_data.get("Corn")),
        Crop("Wheat", 7, crop_data.get("Wheat")),
        Crop("Sweet Corn", 3, crop_data.get("Sweet Corn")),
        Crop("Cotton", 5, crop_data.get("Cotton")),
        Crop("Apples", 10, crop_data.get("Apples")),
        Crop("Rice", 1, crop_data.get("Rice")),
        Crop("Soybeans", 5, crop_data.get("Soybeans")),
    ]

    # Initialize livestock
    livestock = [
        Livestock("Cows", 1, livestock_data.get("Cows")),
        Livestock("Chickens", 1, livestock_data.get("Chickens")),
        Livestock("Sheep", 2, livestock_data.get("Sheep")),
        Livestock("Goats", 2, livestock_data.get("Goats"))
    ]

    # Ask if the user wants to update dates
    update_dates = input("Do you want to update the last watered and fed dates? (yes/no): ").lower() == "yes"

    # If updating dates, ask for the preferred method
    if update_dates:
        # Update dates for crops
        update_method = input(
            "Do you want to update watering dates for all crops at once or individually? (all/individual): ").lower()
        if update_method == "all":
            while True:
                try:
                    date_input = input("Enter the last watered date for all crops (e.g., YYYY-MM-DD): ")
                    last_watered_date = parse_date(date_input)
                    break
                except ValueError as e:
                    print(e)
            for crop in crops:
                crop.set_last_watered(last_watered_date)
        else:
            print("\nUpdating watering dates for each crop:")
            for crop in crops:
                while True:
                    try:
                        date_input = input(f"Enter the last watered date for {crop.name} (e.g., YYYY-MM-DD): ")
                        crop.set_last_watered(parse_date(date_input))
                        break
                    except ValueError as e:
                        print(e)

        # Update dates for livestock
        update_method = input(
            "Do you want to update feeding dates for all animals at once or individually? (all/individual): ").lower()
        if update_method == "all":
            while True:
                try:
                    date_input = input("Enter the last fed date for all animals (e.g., YYYY-MM-DD): ")
                    last_fed_date = parse_date(date_input)
                    break
                except ValueError as e:
                    print(e)
            for animal in livestock:
                animal.set_last_fed(last_fed_date)
        else:
            print("\nUpdating feeding dates for each animal:")
            for animal in livestock:
                while True:
                    try:
                        date_input = input(f"Enter the last fed date for {animal.name} (e.g., YYYY-MM-DD): ")
                        animal.set_last_fed(parse_date(date_input))
                        break
                    except ValueError as e:
                        print(e)
    else:
        print("Using previously saved dates, if available.")

    # Season and rain input for crops
    season = input("Enter the current season (spring, summer, fall, winter): ").lower()
    recent_rain = input("Has it rained recently? (yes/no): ").lower() == "yes"

    # Watering schedule
    print("\nWatering Schedule:")
    for crop in crops:
        if crop.needs_watering(season, recent_rain):
            print(f"Reminder: Water your {crop.name} today!")
            crop.set_last_watered(datetime.date.today())
        else:
            adjusted_frequency = crop.adjust_frequency(season, recent_rain)
            days_left = adjusted_frequency - (datetime.date.today() - crop.last_watered).days
            print(f"{crop.name} will need watering in {days_left} day(s).")

    # Feeding schedule
    print("\nFeeding Schedule:")
    for animal in livestock:
        if animal.needs_feeding():
            print(f"Reminder: Feed your {animal.name} today!")
            animal.set_last_fed(datetime.date.today())
        else:
            days_left = animal.feed_frequency - (datetime.date.today() - animal.last_fed).days
            print(f"{animal.name} will need feeding in {days_left} day(s).")

    # Save updated data
    save_data(crops, livestock)


if __name__ == "__main__":
    main()