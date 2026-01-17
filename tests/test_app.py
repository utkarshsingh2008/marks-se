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
class TestSprint2(unittest.TestCase):

    def test_calculate_grade_A_plus(self):
        ms = MarksSystem()
        ms.add_student("201", "Ravi")
        ms.add_marks("201", 95)
        self.assertEqual(ms.calculate_grade("201"), "A+")

    def test_calculate_grade_boundaries(self):
        ms = MarksSystem()
        ms.add_student("202", "Mina")

        ms.add_marks("202", 89)
        self.assertEqual(ms.calculate_grade("202"), "A")

        ms.add_marks("202", 79)
        self.assertEqual(ms.calculate_grade("202"), "B")

        ms.add_marks("202", 60)
        self.assertEqual(ms.calculate_grade("202"), "C")

        ms.add_marks("202", 50)
        self.assertEqual(ms.calculate_grade("202"), "D")

        ms.add_marks("202", 49)
        self.assertEqual(ms.calculate_grade("202"), "F")

    def test_calculate_grade_marks_not_set(self):
        ms = MarksSystem()
        ms.add_student("203", "NoMarks")
        with self.assertRaises(ValueError):
            ms.calculate_grade("203")
class TestSprint3(unittest.TestCase):

    def test_generate_report_header(self):
        ms = MarksSystem()
        ms.add_student("301", "Kiran")
        report = ms.generate_report()
        self.assertIn("ROLL\tNAME\tMARKS\tGRADE", report)

    def test_generate_report_contains_student(self):
        ms = MarksSystem()
        ms.add_student("302", "Amit")
        ms.add_marks("302", 91)
        report = ms.generate_report()
        self.assertIn("302\tAmit\t91\tA+", report)
