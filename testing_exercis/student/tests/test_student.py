from unittest import TestCase, main

from django.db.models.expressions import result

from project.student import Student


class StudentTest(TestCase):
    def setUp(self):
        self.student1 = Student("Test1",
                                {"Python": ["n1", "n2", "n3"],
                                 "JS": ["n1", "n2"]})
        self.student2 = Student("Test2")

    def test_init_with_courses(self):
        self.assertEqual("Test1", self.student1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "JS": ["n1", "n2"]}, self.student1.courses)
        self.assertIsInstance(self.student1.name, str)
        self.assertIsInstance(self.student1.courses, dict)

    def test_init_without_courses(self):
        self.assertEqual("Test2", self.student2.name)
        self.assertEqual({}, self.student2.courses)
        self.assertIsInstance(self.student2.name, str)
        self.assertIsInstance(self.student2.courses, dict)

    def test_enroll_existing_courses(self):
        result = self.student1.enroll("Python", ["n4", "n5"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5"],
                          "JS": ["n1", "n2"]}, self.student1.courses)

        result = self.student1.enroll("Python", ["n6", "n7"], "N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5", "n6", "n7"],
                          "JS": ["n1", "n2"]}, self.student1.courses)

    def test_enroll_not_existing_courses_with_Y(self):
        result = self.student1.enroll("C++", ["n1", "n2"], "Y")
        self.assertIn("C++", self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student1.courses["C++"])

    def test_enroll_not_existing_courses_with_empty_str(self):
        result = self.student1.enroll("C++", ["n1", "n2"], "")
        self.assertIn("C++", self.student1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student1.courses["C++"])

    def test_enroll_not_existing_courses_not_adding_note(self):
        result = self.student1.enroll("C++", ["n1", "n2"], "N")
        self.assertIn("C++", self.student1.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student1.courses["C++"])

    def test_add_notes_to_existing_course(self):
        self.student2.enroll('C#', ["n1", "n2"], "Y")
        result = self.student2.add_notes("C#", "n3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2", "n3"], self.student2.courses["C#"])

    def test_add_notes_to_not_existing_course(self):
        with self.assertRaises(Exception) as e:
            self.student2.add_notes("C#", ["n1", "n2"])
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))

    def test_leave_existing_course(self):
        result = self.student1.leave_course("JS")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("JS", self.student1.courses)

    def test_leave_not_existing_course(self):
        with self.assertRaises(Exception) as e:
            self.student1.leave_course("C#")
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))


if __name__ == '__main__':
    main()
