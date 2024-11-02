crops = ["corn", "wheat", "sweet corn", "cotton", "apples", "rice", "soybeans"]
run = True
while run:
    answer = input(f'What crop are you attempting to plant? Pick from {crops}: ')
    if answer == 'Corn':
        print('Corn')
    if answer == 'End':
        run = False
    if answer not in crops and not 'End':
     print("Try again")
