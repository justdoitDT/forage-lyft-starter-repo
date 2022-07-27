import unittest
from datetime import datetime

from LyftTask4 import Car
from LyftTask4 import Calliope
from LyftTask4 import Glissade
from LyftTask4 import Palindrome
from LyftTask4 import Rorschach
from LyftTask4 import Thovex
from LyftTask4 import Capulet
from LyftTask4 import Willoughby
from LyftTask4 import Sternman
from LyftTask4 import Spindler
from LyftTask4 import Nubbin

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 30001
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 29999
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0.9, 0]
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0.89, 0]
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 60001
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 59999
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [1, 1, 1, 0]
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [1, 1, 0.9, 0]
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = True

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 99999999999
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [1, 1, 1, 0]
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [1, 1, 0.9, 0]
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 60001
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 59999
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [1, 1, 1, 0]
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [1, 1, 0.9, 0]
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 30001
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 29999
        tire_wear_array = [0, 0, 0, 0]
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0.9, 0]
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        tire_wear_array = [0, 0, 0.89, 0]
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, tire_wear_array, engine_warning_on)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
