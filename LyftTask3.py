import unittest
from datetime import datetime

from LyftTask2 import Car
from LyftTask2 import Calliope
from LyftTask2 import Glissade
from LyftTask2 import Palindrome
from LyftTask2 import Rorschach
from LyftTask2 import Thovex
from LyftTask2 import Capulet
from LyftTask2 import Willoughby
from LyftTask2 import Sternman
from LyftTask2 import Spindler
from LyftTask2 import Nubbin

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 30001
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 29999
        engine_warning_on = False

        car = Calliope(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 60001
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 59999
        engine_warning_on = False

        car = Glissade(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = True

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 99999999999
        engine_warning_on = False

        car = Palindrome(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 60001
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 59999
        engine_warning_on = False

        car = Rorschach(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        last_service_mileage = 0
        current_mileage = 0
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 30001
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        last_service_mileage = 0
        current_mileage = 29999
        engine_warning_on = False

        car = Thovex(last_service_date, last_service_mileage, current_mileage, engine_warning_on)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
