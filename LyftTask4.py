# Note to Lyft team members assigned to Forage:
# The instructions are unclear about which model cars are outfitted with which model tires.
# I have assigned Carrigan tires to all Calliope and Thovex models and
# Octoprime tires to all Glissade, Palindrome, and Rorschach models.


from datetime import datetime


# car super-class
class Car:
    def __init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on=False):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.engine_warning_on = engine_warning_on
        self.tire_wear_array = tire_wear_array
        self.days_since_serviced = (datetime.today().date() - last_service_date).days
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()




# car model sub-classes (edit these if a model switches parts, and with actual tire types when they become available)

class Calliope(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.engine = Capulet(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.battery = Spindler(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.tires = Carrigan(tire_wear_array)

class Glissade(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.engine = Willoughby(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.battery = Spindler(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.tires = Octoprime(tire_wear_array)

class Palindrome(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.engine = Sternman(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.battery = Spindler(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.tires = Octoprime(tire_wear_array)

class Rorschach(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.engine = Willoughby(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.battery = Nubbin(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.tires = Octoprime(tire_wear_array)

class Thovex(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.engine = Capulet(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.battery = Nubbin(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.tires = Carrigan(tire_wear_array)




# engine sub-classes (edit these if engine service criteria change)

class Capulet(Car):
    def needs_service(self):
        # should the warning indicator also trigger service? if so, uncomment the following line
        # return self.current_mileage - self.last_service_mileage >= 30000 or engine_warning_on
        return self.current_mileage - self.last_service_mileage >= 30000

class Willoughby(Car):
    def needs_service(self):
        # should the warning indicator also trigger service? if so, uncomment the following line
        # return self.current_mileage - self.last_service_mileage >= 60000 or engine_warning_on
        return self.current_mileage - self.last_service_mileage >= 60000

class Sternman(Car):
    def needs_service(self):
        return self.engine_warning_on




# battery sub-classes (edit these if battery service criteria change)

class Spindler(Car):
    def needs_service(self):
        return self.days_since_serviced / 365.25 > 3

class Nubbin(Car):
    def needs_service(self):
        return self.days_since_serviced / 365.25 > 4




# tire sub-classes (edit these if tire service criteria change)

class Carrigan:
    def __init__(self, wear_array):
        self.wear_array = wear_array
    def needs_service(self):
        return max(self.wear_array) >= 0.9

class Octoprime:
    def __init__(self, wear_array):
        self.wear_array = wear_array
    def needs_service(self):
        return sum(self.wear_array) >= 3
