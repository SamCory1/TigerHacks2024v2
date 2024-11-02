run = True
crops = ["corn", "wheat", "sweet corn", "cotton", "apple", "rice", "soybean", "potato", "melon", "hay", "sweet potato"]
budget = 1000
corn =
print("The current budget is: $", budget)
input("What crop is this?").lower()
while run:
    answer = input("What crop would you like to buy?").lower()
        if answer in crops and not "end":
            acre = input("How many acres would you like to plant on?")