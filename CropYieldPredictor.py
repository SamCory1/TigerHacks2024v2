crops = ["corn", "wheat", "sweet corn", "cotton", "apples", "rice", "soybeans"]
crop_yield_list = [177.3, 37.1, 5, 813, 400,7649, 50.6 ]
run = True
while run:
    crop = input(f'What crop are you planting? Pick from Corn, Wheat, Sweet Corn, Cotton, Apples, Rice, Soybeans or type "End" to end: ').lower()
    if crop in crops:
        acres = float(input('How many acres did you plant?'))
        crop = crop.capitalize()
        print(f"{crop} selected!")
        if crop == 'Corn':
            crop_yield = round(acres*crop_yield_list[0]) #177.3 bushels per acre on average.
            crop_sale = round(crop_yield*4.1475, 2)
            print(f"This is your expected return: {crop_yield} bushels of corn; worth ${crop_sale}")
        if crop =='Wheat':
            crop_yield = round(acres*crop_yield_list[1])
            crop_sale = round(crop_yield*6.3909, 2)
            print(f"This is your expected return: {crop_yield} bushels of wheat; worth ${crop_sale}")
        if crop == 'Sweet Corn':
            crop_yield = round(acres*crop_yield_list[2])
            crop_sale = round(crop_yield*126, 2)
            print(f"This is your expected return: {crop_yield} tons of sweet corn; worth ${crop_sale}")
        if crop == 'Cotton':
            crop_yield = round(acres*crop_yield_list[3])
            crop_sale = round(crop_yield* 0.7, 2)
            print(f"This is your expected return: {crop_yield} pounds of cotton; worth ${crop_sale}")
        if crop == 'Apples':
            crop_yield = round(acres*crop_yield_list[4])
            crop_sale = round(crop_yield * 55, 2)
            print(f"This is your expected return: {crop_yield} bushels of apples; worth ${crop_sale}")
        if crop == 'Rice':
            crop_yield = round(acres*crop_yield_list[5])
            crop_sale = round(crop_yield *0.97,2)
            print(f"This is your expected return: {crop_yield} pounds of rice; worth ${crop_sale}")
        if crop == 'Soybeans':
            crop_yield = round(acres*crop_yield_list[6])
            crop_sale = round(crop_yield* 11.20, 2)
            print(f"This is your expected return: {crop_yield} bushels of soybeans; worth ${crop_sale}")
    if crop == 'end':
        run = False
