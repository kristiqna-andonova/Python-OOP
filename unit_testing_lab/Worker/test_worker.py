from unittest import TestCase, main
#from unit_testing_lab.Worker.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Tihomir", 10000, 100)

    def test_correct_init(self):
        self.assertEqual("Tihomir", self.worker.name)
        self.assertEqual(10000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_negative_energy(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_with_positive_energy(self):
        exp_energy = self.worker.energy - 1
        exp_money = self.worker.salary

        self.worker.work()

        self.assertEqual(exp_energy, self.worker.energy)
        self.assertEqual(exp_money, self.worker.money)

    def test_rest(self):
        exp_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(exp_energy, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f"{self.worker.name} has saved {self.worker.money} money.", self.worker.get_info())




if __name__ == '__main__':
    main()