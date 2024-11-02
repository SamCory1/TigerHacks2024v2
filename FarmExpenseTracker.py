run = True
crops = ["corn", "wheat", "sweet corn", "cotton", "apple", "rice", "soybean", "potato", "melon", "hay", "sweet potato"]
budget = 10000
corn_price_per_acre = 120
wheat_price_per_acre = 40
sweetcorn_price_per_acre = 250
cotton_price_per_acre = 70
apple_price_per_acre = 300
rice_price_per_acre = 50
soybean_price_per_acre = 70
potato_price_per_acre = 335
melon_price_per_acre = 335
hay_price_per_acre = 50
sweetpotato_price_per_acre = 335

print(f"The current budget is: ${budget}")
while run:
    answer = input("What crop would you like to buy? ").lower()
    if answer in ["End", "end", "END"]:
        run = False
        continue

    if answer in crops:
        try:
           acre = float(input("How many acres would you like to plant on? "))
           if answer == "corn":
               cost = acre * corn_price_per_acre
           elif answer == "wheat":
               cost = acre * wheat_price_per_acre
           elif answer == "sweet corn":
               cost = acre * sweetcorn_price_per_acre
           elif answer == "cotton":
               cost = acre * cotton_price_per_acre
           elif answer == "apple":
               cost = acre * apple_price_per_acre
           elif answer == "rice":
               cost = acre * rice_price_per_acre
           elif answer == "soybean":
               cost = acre * soybean_price_per_acre
           elif answer == "potato":
               cost = acre * potato_price_per_acre
           elif answer == "melon":
               cost = acre * melon_price_per_acre
           elif answer == "hay":
               cost = hay_price_per_acre
           elif answer == "sweet potato":
               cost = acre * sweetpotato_price_per_acre

           if cost > budget:
               print("Price exceeds budget.")
           else:
               budget = budget - cost
               print(f"You have bought {acre} acres of {answer}. Your remaining budget is ${budget}")
        except ValueError:
            print("Must enter a number.")
    else:
        print("Not in crop selection.")


