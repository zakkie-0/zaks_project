class Car:

    def __init__(self, brand_name, kilometers, liters):
        # insert code
        self.brand_name = brand_name
        self.kilometers = kilometers
        self.liters = liters

    def calculate_mpg(self):
        # insert code
        miles = self.kilometers / 1.609344
        gallons = self.liters / 4.54609
        MPG = miles / gallons
        return round(MPG,2)

    def calculate_rate_of_gas(self, price):
        gas = price / self.calculate_mpg()
        return round(gas,2)
    

    