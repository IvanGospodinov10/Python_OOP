class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


# ============ "Test case - unit test" =======


from unittest import TestCase, main


class WorkerTest(TestCase):
    def test_init(self):
        w = Worker("test", 1000, 100)
        self.assertEqual("test", w.name)
        self.assertEqual(1000, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

    def test_worker_works_no_energy_raises(self):
        w = Worker("test", 1000, 0)
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

        w.energy = -1
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work(self):
        w = Worker("test", 1000, 100)
        self.assertEqual(0, w.money)
        self.assertEqual(100, w.energy)

        w.work()

        self.assertEqual(99, w.energy)
        self.assertEqual(1000, w.money)

        w.work()

        self.assertEqual(98, w.energy)
        self.assertEqual(2000, w.money)

    def test_rest(self):
        w = Worker("test", 1000, 80)

        w.rest()

        self.assertEqual(81, w.energy)

        w.rest()

        self.assertEqual(82, w.energy)

    def test_get_info(self):
        w = Worker("test", 1000, 100)

        expected_text = "test has saved 0 money."
        result = w.get_info()
        self.assertEqual(expected_text, result)

        w.work()
        expected_text = "test has saved 1000 money."
        result = w.get_info()
        self.assertEqual(expected_text, result)


if __name__ == '__main__':
    main()
