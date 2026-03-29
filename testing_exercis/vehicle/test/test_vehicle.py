from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    fuel = 36.5
    horsepower = 135.8

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horsepower)

    def test_class_attributes_type(self):
        self.assertTrue(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertTrue(self.vehicle.fuel_consumption, float)
        self.assertTrue(self.vehicle.fuel, float)
        self.assertTrue(self.vehicle.capacity, float)
        self.assertTrue(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horsepower, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(30.25, self.vehicle.fuel)

    def test_drive_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(10.5)
        self.assertEqual(11.5, self.vehicle.fuel)

    def test_refuel_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20.5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = (f"The vehicle has {self.horsepower} "
                    f"horse power with {self.fuel} fuel left"
                    f" and 1.25 fuel consumption")
        self.assertEqual(expected, str(self.vehicle))



if __name__ == "__main__":
    main()