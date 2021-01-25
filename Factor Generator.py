print('Welcome to the Factor Generator App')

running = True

while running:
    number = int(input('\nEnter a number you want to see the factors of: '))
    factors = []
    for num in range(1, number+1):
        if number % num == 0:
            factors.append(num)

    print('\nFactors of ' + str(number) + ' are: ')
    for factor in factors:
        print(factor)

    print('\nIn summary: ')
    for element in range(int(len(factors)/2)):
        print(str(factors[element]) + " * " + str(factors[-element-1]) + " = " + str(number))

    choice = input('\nWould you like to run this again (y/n): ')
    if choice.startswith('n'):
        running = False

print('\nThank you for using the Factor Generator App. Goodbye.')    
