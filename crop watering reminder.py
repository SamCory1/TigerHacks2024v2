import datetime
import json
import os

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

# File to save watering data
DATA_FILE = "watering_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return {name: datetime.date.fromisoformat(date) for name, date in data.items()}
    return {}

def save_data(crops):
    data = {crop.name: crop.last_watered.isoformat() for crop in crops if crop.last_watered is not None}
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def parse_date(date_str):
    """Attempts to parse the date string in multiple formats."""
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%B %d, %Y"):
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please try again.")

def main():
    # Create a list of crops with their base watering frequencies
    crop_data = load_data()
    crops = [
        Crop("Corn", 4, crop_data.get("Corn")),
        Crop("Wheat", 7, crop_data.get("Wheat")),
        Crop("Sweet Corn", 3, crop_data.get("Sweet Corn")),
        Crop("Cotton", 5, crop_data.get("Cotton")),
        Crop("Apples", 10, crop_data.get("Apples")),
        Crop("Rice", 1, crop_data.get("Rice")),
        Crop("Soybeans", 5, crop_data.get("Soybeans")),
    ]

    # Check if we need to prompt for a last watered date
    if all(crop.last_watered is None for crop in crops):
        while True:
            date_input = input("Enter the last watered date for all crops (e.g., YYYY-MM-DD, DD-MM-YYYY, MM/DD/YYYY, Month DD, YYYY): ")
            try:
                last_watered_date = parse_date(date_input)
                break
            except ValueError as e:
                print(e)
        for crop in crops:
            crop.set_last_watered(last_watered_date)
    else:
        # Ask if the user wants to update the last watered date
        update_date = input("Do you want to update the last watered date for all crops? (yes/no): ").lower()
        if update_date == "yes":
            while True:
                date_input = input("Enter the new last watered date for all crops (e.g., YYYY-MM-DD, DD-MM-YYYY, MM/DD/YYYY, Month DD, YYYY): ")
                try:
                    last_watered_date = parse_date(date_input)
                    break
                except ValueError as e:
                    print(e)
            for crop in crops:
                crop.set_last_watered(last_watered_date)

    # Prompt user for season and rain conditions
    season = input("Enter the current season (spring, summer, fall, winter): ").lower()
    recent_rain_input = input("Has it rained recently? (yes/no): ").lower()
    recent_rain = recent_rain_input == "yes"

    # Check each crop to see if it needs watering
    print("\nWatering Schedule:")
    for crop in crops:
        if crop.needs_watering(season, recent_rain):
            print(f"Reminder: Water your {crop.name} today!")
        else:
            adjusted_frequency = crop.adjust_frequency(season, recent_rain)
            days_left = adjusted_frequency - (datetime.date.today() - crop.last_watered).days
            print(f"{crop.name} will need watering in {days_left} day(s).")

    # Save updated last watered dates to the file
    save_data(crops)

# Run the program
if __name__ == "__main__":
    main()