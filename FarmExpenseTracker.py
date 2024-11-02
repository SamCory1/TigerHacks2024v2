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
                print(f"{amount} acres of {crop_name} added. Total cost is now ${total_cost:.2f}. Remaining budget: ${remaining_budget:.2f}.")
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

if __name__ == "__main__":
    main()
