def taxi (distance=0):
    BASE_FARE = 4.00
    if distance > 140:
        
        return f'{(BASE_FARE + (1*(distance/140)))- 1 :.2f}'
    
    return f'{BASE_FARE:.2f}'


print(taxi(721))