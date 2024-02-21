class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, mileage, services=[]):
        CarManager.total_cars += 1
        # update all_carslist
        CarManager.all_cars.append(self)

        self._id = CarManager.total_cars  # never repeat
        self._make = make  # string
        self._model = model  # string
        self._year = int(year)  # int
        self._mileage = int(mileage)  # int
        self._services = services  # list of services

    def __str__(self):
        return f'''ID: {self._id} Make: {self._make} | Model: {self._model} | Year: {self._year} | Mileage: {self._mileage} | Service(s): {self._services}'''

    # def add_services(self):
    #     # self._services.append(service)

    def __repr__(self):
        return str(self)

    # @classmethod
    # def get_all_cars(cls):
    #     return cls.all_cars


def menu():

    print(f'''----  WELCOME  ----
    1. Add a car
    2. View all cars
    3. View total number of cars
    4. See a car's details
    5. Service a car
    6. Update mileage
    7. Quit''')
    user_choice = input('Please enter a number to select an option: ')

    if user_choice == "1" or user_choice == "1.":
        print('You have selected to add a car.')
        make = input('Enter the make of the car: ')
        model = input('Enter the model of the car: ')
        year = input('Enter the year of the car: ')
        mileage = input('Enter the mileage of the car: ')
        car1 = CarManager(make, model, year, mileage)
        print(f'car was added successfully!')
        print(car1)
        menu()

    if user_choice == "2":
        print('You have selected to view all cars.')
        print(CarManager.all_cars)
        menu()

    if user_choice == "3":
        print('You have selected to view the total number of cars.')
        print(CarManager.total_cars)
        menu()

    if user_choice == "4":
        print('You have selected to see a car\'s details.')
        car_id = input(
            'Enter the ID of the car you would like to see the details of: ')
        print(CarManager.all_cars[int(car_id)-1])
        menu()

    if user_choice == "5":
        print('You have selected to service a car.')
        # CarManager.add_services()
        car_id = input(
            'Enter the ID of the car you would like to service: ')
        service = input('Enter the service you would like to add: ')
        CarManager.all_cars[int(car_id)-1]._services.append(service)
        print(CarManager.all_cars[int(car_id)-1])
        print('Service was added successfully!')
        menu()

    if user_choice == "6":
        print('You have selected to update the mileage of a car.')
        car_id = input(
            'Enter the ID of the car you would like to update: ')
        new_mileage = input('Enter the updated mileage: ')
        CarManager.all_cars[int(car_id)-1]._mileage = int(new_mileage)
        print(CarManager.all_cars[int(car_id)-1])
        print('Service was added successfully!')
        menu()

    if user_choice == "7":
        print('''You have selected to quit.
              Goodbye!''')
        exit()


menu()
# print("total cars", str(CarManager.total_cars))
# print("car2")
# car2 = CarManager("Jeep", "Wrangler", 1998, 100000)
# print(car2)
# print(CarManager.all_cars)

# print("total cars: " + str(CarManager.total_cars))
# print("car2")
# car2 = CarManager("Honda", "Civic")
# print(car2._id)
# print(CarManager.all_cars)

# print("total cars: " + str(CarManager.total_cars))
# print("car3")
# car3 = CarManager("Volkswagen", "Jetta")
# print(car3._id)
# print(CarManager.all_cars)

# print("total cars: " + str(CarManager.total_cars))
# print("car4")
# car4 = CarManager("Chevrolet", "Silverado")
# print(car4._id)
# print(CarManager.all_cars)
