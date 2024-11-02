crops = ["corn", "wheat", "sweet corn", "cotton", "apples", "rice", "soybeans"]
crop_yield_list = [177.3, 37.1, 5, 845, 400,7649, 50.6 ]
run = True
while run:
    crop = input(f'What crop are you planting? Pick from Corn, Wheat, Sweet Corn, Cotton, Apples, Rice, Soybeans or type "End" to end: ')
    acres = float(input('How many acres did you plant?'))
    if crop in crops:
        crop = crop.capitalize()
        print(f"{crop} selected!")
        if crop == 'Corn':
            crop_yield = round(acres*crop_yield_list[0]) #177.3 bushels per acre on average.
            crop_sale = round(crop_yield*4.1475, 2)
            print(f"This is your expected return {crop_yield} bushels of corn worth ${crop_sale}")
        if crop =='Wheat':
            crop_yield = round(acres*crop_yield_list[1])
            crop_salesale = round(crop_yield*)


    if crop == 'End':
        run = False
    if crop not in crops and not 'End':
        print("Try again")
