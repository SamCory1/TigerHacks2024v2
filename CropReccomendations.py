run = True

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

seasons = [
    "spring", "summer", "fall"
]

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

print("Welcome to the Crop Recommendation Simulator")
while run:
    state_of_residence = input("What state do you reside in? ").lower()
    if state_of_residence in ["end", "End", "END"]:
        run = False
        continue
    if state_of_residence in states:
        current_season = input("What is the current season? ").lower()
        if current_season in seasons:
            crops = recommendations[state_of_residence][current_season]
            print(f"In {state_of_residence.capitalize()}, during {current_season}, you can plant: {', '.join(crops)}.")
        else:
            print("Invalid season entered. Please enter spring, summer, or fall.")
    else:
        print("Invalid state entered. Please try again.")
