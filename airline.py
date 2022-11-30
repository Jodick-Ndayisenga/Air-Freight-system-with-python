class Airline:
    passengers = {}
    number = 0
    def __init__(self,origin, destination, seats):
        self.origin = origin
        self.destination = destination
        self.seats = seats

    def __str__(self):
        return (f'| From {self.origin} to {self.destination} |')
           
    def addPassenger(self):
        if len(Airline.passengers)<self.seats:
            name = input('Enter your first name: ')
            self.firstName = name
            last = input('Enter your last name: ')
            self.secondName = last
            Airline.number += 1
            Airline.passengers[Airline.number] = f'{self.firstName} {self.secondName}'
            self.seats -=1
            print('-------------------------------------')
            print(f'{self.firstName.upper()} was successfully added!!')
            print(f'Open seats: {self.seats}')
            print('-------------------------------------')
        else:
            print('The flight is full, try opening another flight!!')

    def checkPassengers(self):
        print('--PASSENGERS--')
        print('')
        for keys, values in Airline.passengers.items():
            print(f'{keys}. {values}')
        print('')
        print(f'Open seats: {self.seats}')
        print('--------------------------------------------')       

    def removePassenger(self):
        person = input('Who do you want to remove: ')
        for key in Airline.passengers.keys():
            if Airline.passengers[key] == person:
                Airline.passengers.pop(key)
                self.seats += 1
                break
        num = 0
        print('NOW WE HAVE ON FLIGHT')
        print('-------------------------------------')
        for value in Airline.passengers.values():
            num +=1
            print(f'{num}. {value}')
        print(f'Open seats: {self.seats}')
        print('-------------------------------------')

print('')
origin = input('What is the origin of your journey: ')
destination = input('What is the destination of your journey: ')

while True:
    try:
        seats = int(input('Enter the number of open seats: '))
        while True:
            
            name = Airline(origin, destination, seats=50)
            print('''
            1. Add another passenger.\n
            2. Do you want to see all pasengers on a flight.\n
            3. Remove a passenger from this flight\n
            4. Check the origin\n
            5. Check the destination\n
            6. check itinerary''')
            print('')
        
            try:
                choice = int(input('Enter what you want to do: '))

                if choice == 1:
                    name.addPassenger()

                elif choice == 2:
                    name.checkPassengers()
                elif choice == 3:
                    name.removePassenger()

                elif choice == 4:
                    print('-------------------------------------')
                    print('Departure:', name.origin)
                    print('-------------------------------------')

                elif choice == 5:
                    print('-------------------------------------')
                    print('Destination: ',name.destination)
                    print('-------------------------------------')

                elif choice == 6:
                    print('-------------------------------------------')
                    print(name)
                    print('-------------------------------------------')

                else:
                    print('Please enter a valid number within the range provided')
                    continue
            except:
                print('Please Enter a valid number within the range provided above!')
                continue

    except:
        print('Seats must be in numbers')
        continue