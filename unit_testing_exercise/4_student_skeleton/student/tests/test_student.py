from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self):
        self.student = Student("Student 1", {"Python": ["n1", "n2"], "JS": ["n1", "n2"]})
        self.student_2 = Student("Student 2")

    def test_init(self):
        self.assertEqual("Student 1", self.student.name)
        self.assertEqual({"Python": ["n1", "n2"], "JS": ["n1", "n2"]}, self.student.courses)

    def test_init_without_course(self):
        self.assertEqual("Student 2", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_enroll_course(self):
        result = self.student.enroll("Python", ["n4", "n5"], add_course_notes="N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n4", "n5"], "JS": ["n1", "n2"]}, self.student.courses)

        result = self.student.enroll("Python", ["n8", "n9"], add_course_notes="Y")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n4", "n5", "n8", "n9"], "JS": ["n1", "n2"]},
                         self.student.courses)

    def test_with_no_existing_course_with_yes(self):
        result = self.student.enroll("C#", ["n1", "n2"], add_course_notes="Y")

        self.assertTrue("C#" in self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student.courses["C#"])

    def test_with_none_existing_course_with_empty_str(self):
        result = self.student.enroll("C#", ["n1", "n2"], add_course_notes="")

        self.assertTrue("C#" in self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student.courses["C#"])

    def test_with_none_existing_course_and_no_notes(self):
        result = self.student.enroll("C#", ["n1", "n2"], add_course_notes="M")

        self.assertTrue("C#" in self.student.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["C#"])

    def test_add_notes_to_existing_course(self):
        self.student_2.enroll("C#", ["n1"])
        result = self.student_2.add_notes("C#", "n2")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2"], self.student_2.courses["C#"])

    def test_with_none_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("C#", ["n1"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        result = self.student.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student.courses)

    def test_leave_course_none_with_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("C#")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()
