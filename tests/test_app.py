import unittest
from src.app import MarksSystem


class TestSprint1(unittest.TestCase):

    def test_add_student_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        self.assertIn("101", ms.students)
        self.assertEqual(ms.students["101"].name, "Asha")

    def test_add_student_duplicate(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_student("101", "Asha Again")

    def test_add_student_missing_fields(self):
        ms = MarksSystem()
        with self.assertRaises(ValueError):
            ms.add_student("", "Asha")
        with self.assertRaises(ValueError):
            ms.add_student("101", "")

    def test_add_marks_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        ms.add_marks("101", 88)
        self.assertEqual(ms.students["101"].marks, 88)

    def test_add_marks_out_of_range(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_marks("101", 120)
        with self.assertRaises(ValueError):
            ms.add_marks("101", -5)

    def test_add_marks_unknown_student(self):
        ms = MarksSystem()
        with self.assertRaises(KeyError):
            ms.add_marks("999", 50)


if __name__ == "__main__":
    unittest.main()
