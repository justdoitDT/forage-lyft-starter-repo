from datetime import datetime


# car super-class
class Car:
    def __init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on=False):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.engine_warning_on = engine_warning_on
        self.days_since_serviced = (datetime.today().date() - last_service_date).days
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()




# car model sub-classes (edit these if a model switches parts, and with actual tire types when they become available)

class Calliope(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.engine = Capulet(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.battery = Spindler(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        # edit the following line when actual tire data becomes available
        self.tires = Tire_Type_A(last_service_date, last_service_mileage, current_mileage, engine_warning_on)

class Glissade(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.engine = Willoughby(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.battery = Spindler(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        # edit the following line when actual tire data becomes available
        self.tires = Tire_Type_B(last_service_date, last_service_mileage, current_mileage, engine_warning_on)

class Palindrome(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.engine = Sternman(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.battery = Spindler(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        # edit the following line when actual tire data becomes available
        self.tires = Tire_Type_C(last_service_date, last_service_mileage, current_mileage, engine_warning_on)

class Rorschach(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.engine = Willoughby(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.battery = Nubbin(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        # edit the following line when actual tire data becomes available
        self.tires = Tire_Type_A(last_service_date, last_service_mileage, current_mileage, engine_warning_on)

class Thovex(Car):
    def __init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on=False):
        Car.__init__(self, last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.engine = Capulet(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.battery = Nubbin(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        # edit the following line when actual tire data becomes available
        self.tires = Tire_Type_B(last_service_date, last_service_mileage, current_mileage, engine_warning_on)




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
        return self.days_since_serviced / 365.25 > 2

class Nubbin(Car):
    def needs_service(self):
        return self.days_since_serviced / 365.25 > 4




# tire sub-classes (edit these when actual tire data and service criteria become available)

class Tire_Type_A(Car):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= float('inf')

class Tire_Type_B(Car):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= float('inf')

class Tire_Type_C(Car):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= float('inf')