import datetime

class Crop:
    def __init__(self, name, base_frequency):
        self.name = name
        self.base_frequency = base_frequency  # default days between watering
        self.last_watered = None  # To be set by user

    def set_last_watered(self):
        date_input = input(f"Enter the last watered date for {self.name} (YYYY-MM-DD): ")
        self.last_watered = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

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

def main():
    # Create a list of crops with their base watering frequencies
    crops = [
        Crop("Tomato", 2),
        Crop("Lettuce", 1),
        Crop("Carrot", 3),
    ]

    # Prompt user for season and rain conditions
    season = input("Enter the current season (spring, summer, fall, winter): ").lower()
    recent_rain_input = input("Has it rained recently? (yes/no): ").lower()
    recent_rain = recent_rain_input == "yes"

    # Prompt user to input last watered dates
    for crop in crops:
        crop.set_last_watered()

    # Check each crop to see if it needs watering
    print("\nWatering Schedule:")
    for crop in crops:
        if crop.needs_watering(season, recent_rain):
            print(f"Reminder: Water your {crop.name} today!")
            crop.water()
        else:
            adjusted_frequency = crop.adjust_frequency(season, recent_rain)
            days_left = adjusted_frequency - (datetime.date.today() - crop.last_watered).days
            print(f"{crop.name} will need watering in {days_left} day(s).")

# Run the program
if __name__ == "__main__":
    main()