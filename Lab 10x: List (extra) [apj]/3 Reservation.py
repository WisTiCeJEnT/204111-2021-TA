def print_reservation(guests, tables):
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Start
    print('>>> List of Reservation <<<')
    for i in range(7):
        print(f'{day[i]}: {tables[i]} tables, {guests[i]} guests')
    # End



tables = [0,0,0,0,0,0,0]
guests = [0,0,0,0,0,0,0]

while(True):
    day = input('Day for reservation (1=Mon,2=Tue,...,7=Sun or Exit): ')
    if day == 'Exit':
        break
    day = int(day)
    g = int(input('Enter #guests: '))
    
    if day >= 1 and day <= 4:
        print(f'Payment for {g} guests = {g*300}')
    elif day >= 5 and day <= 7:
        print(f'Payment for {g} guests = {g*500}')
    else:
        print('Invalid number. Day is between 1-7.')
        continue
    tables[day-1] += 1
    guests[day-1] += g
print_reservation(guests, tables)