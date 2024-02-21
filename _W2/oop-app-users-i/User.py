# your User class goes here
class User_Info:
    def __init__(self, name, email, address, driver_license_number):
        self.name = name
        self.email = email
        self.address = address
        self.driver_license_number = driver_license_number


Doug = User_Info("Doug", "doug@gmail.com", "1234 Main St", "123456")
print(Doug.name)
print(Doug.email)
print(Doug.address)
print(f'{Doug.driver_license_number}\n')

Gerald = User_Info("Gerald", "Gerald@gmail.com", "1234 different St", "123456")
print(Doug.name)
print(Doug.email)
print(Doug.address)
print(Doug.driver_license_number)
