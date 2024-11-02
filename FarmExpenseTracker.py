# FarmExpenseTracker.py

from CropReccomendations import get_recommendations, get_price, states, seasons

def main():
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
        crop_choice = int(input("Enter the number of the crop you want to buy (0 to finish): "))
        if crop_choice == 0:
            break
        if 1 <= crop_choice <= len(crop_list):
            crop_name = crop_list[crop_choice - 1]
            crop_cost = get_price(crop_name)
            total_cost += crop_cost
            if total_cost <= budget:
                crops_to_buy.append(crop_name)
                print(f"{crop_name} added. Total cost is now ${total_cost:.2f}.")
            else:
                total_cost -= crop_cost
                print("You don't have enough budget for this crop.")
        else:
            print("Invalid choice. Please try again.")

    print("You have purchased: ", ", ".join(crops_to_buy))
    print(f"Total spent: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
