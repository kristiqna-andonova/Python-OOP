from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(12.0, 360.50)

    def test_init_vehicle(self):
        self.assertEqual(12.0, self.vehicle.fuel)
        self.assertEqual(12.0, self.vehicle.capacity)
        self.assertEqual(360.50, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_positive_test(self):
        self.vehicle.drive(2)
        exp_result = 9.5

        self.assertEqual(exp_result, self.vehicle.fuel)

    def test_drive_negative(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(20)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_positive(self):
        self.vehicle.fuel = 1

        self.vehicle.refuel(1)
        self.assertEqual(2, self.vehicle.fuel)

    def test_negative_negative(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        self.vehicle.fuel = 6

        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} "
                         f"horse power with 6 "
                         f"fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    main()
