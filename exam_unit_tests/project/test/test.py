from unittest import TestCase, main

from project.star_system import StarSystem


class TestStarSystem(TestCase):
    def test_init_validation(self):
        system = StarSystem(
            name="Alpha",
            star_type="Red giant",
            system_type="Single",
            num_planets=3,
            habitable_zone_range=(1, 3)
        )
        self.assertEqual(system.name, "Alpha")
        self.assertEqual(system.star_type, "Red giant")
        self.assertEqual(system.system_type, "Single")
        self.assertEqual(system.num_planets, 3)
        self.assertEqual(system.habitable_zone_range, (1, 3))
        self.assertTrue(system.is_habitable)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("", "Red giant", "Single", 2)
        self.assertEqual("Name must be a non-empty string.", str(ex.exception))

    def test_invalid_star_type(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Invalid", "Single", 2)
        self.assertIn("Star type must be one of", str(ex.exception))

    def test_invalid_system_type(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", "Invalid", 2)
        self.assertIn("System type must be one of", str(ex.exception))

    def test_invalid_num_planets(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", "Single", -1)
        self.assertEqual("Number of planets must be a non-negative integer.", str(ex.exception))

    def test_invalid_habitable_zone_range(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", "Single", 2, (7, 2))
        self.assertEqual("Habitable zone range must be a tuple of two numbers"
                         " (start, end) where start < end.", str(ex.exception))

    def test_is_habitable_zone_no_range(self):
        system = StarSystem("Alpha", "Red giant", "Single", 3, None)
        self.assertFalse(system.is_habitable)

    def test_is_habitable_has_no_planets(self):
        system = StarSystem("Alpha", "Red giant", "Single", 0, (1, 3))
        self.assertFalse(system.is_habitable)

    def test_gt_valid(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, (1, 5))  # range = 4
        s2 = StarSystem("B", "Red giant", "Single", 3, (2, 4))  # range = 2
        self.assertTrue(s1 > s2)

    def test_gt_raises_if_not_habitable(self):
        s1 = StarSystem("A", "Red giant", "Single", 0, (1, 5))
        s2 = StarSystem("B", "Red giant", "Single", 3, (1, 5))

        with self.assertRaises(ValueError) as ex:
            result = s1 > s2
        self.assertEqual("Comparison not possible: One or both systems lack a defined"
                         " habitable zone or planets.", str(ex.exception))

    def test_compare_star_systems_first_wider(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, (1, 5))  # range 4
        s2 = StarSystem("B", "Red giant", "Single", 3, (1, 3))  # range 2

        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("A has a wider habitable zone than B.", result)

    def test_compare_star_systems_second_wider_or_equal(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, (1, 3))  # range 2
        s2 = StarSystem("B", "Red giant", "Single", 3, (1, 5))  # range 4

        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("B has a wider or equal habitable zone compared to A.", result)

    def test_compare_star_systems_error(self):
        s1 = StarSystem("A", "Red giant", "Single", 0, (1, 3))
        s2 = StarSystem("B", "Red giant", "Single", 3, (1, 3))

        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual(
            "Comparison not possible: One or both systems lack a defined habitable zone or planets.",
            result
        )


if __name__ == '__main__':
    main()
