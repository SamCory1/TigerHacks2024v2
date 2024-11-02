crops = ["corn", "wheat", "sweet corn", "cotton", "apples", "rice", "soybeans"]
run = True
while run:
    crop = input(f'What crop are you attempting to plant? Pick from Corn, Wheat, Sweet Corn, Cotton, Apples, Rice, Soybeans or type "End" to end: ')
    seeds = input('How many acres did you plant?')
    if crop in crops:
        crop = crop.capitalize()
        print(f"{crop} selected!")
        if crop == 'corn':


    if crop == 'End':
        run = False
    if crop not in crops and not 'End':
     print("Try again")
