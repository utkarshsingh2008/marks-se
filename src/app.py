from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Student:
    roll_no: str
    name: str
    marks: Optional[float] = None


@dataclass
class MarksSystem:
    students: Dict[str, Student] = field(default_factory=dict)

    def add_student(self, roll_no: str, name: str) -> None:
        if not roll_no or not name:
            raise ValueError("roll_no and name required")

        if roll_no in self.students:
            raise ValueError("student exists")

        self.students[roll_no] = Student(roll_no=roll_no, name=name)

    def add_marks(self, roll_no: str, marks: float) -> None:
        if roll_no not in self.students:
            raise KeyError("student not found")

        if marks < 0 or marks > 100:
            raise ValueError("marks must be 0..100")

        self.students[roll_no].marks = marks
    def calculate_grade(self, roll_no: str) -> str:
        if roll_no not in self.students:
            raise KeyError("student not found")

        marks = self.students[roll_no].marks

        if marks is None:
            raise ValueError("marks not set")

        if marks >= 90:
            return "A+"
        if marks >= 80:
            return "A"
        if marks >= 70:
            return "B"
        if marks >= 60:
            return "C"
        if marks >= 50:
            return "D"
        return "F"
    def generate_report(self) -> str:
        lines = ["ROLL\tNAME\tMARKS\tGRADE"]

        for roll_no, student in self.students.items():
            if student.marks is None:
                marks_str = "-"
                grade = "-"
            else:
                # Convert 91.0 → 91
                marks_str = (
                    str(int(student.marks))
                    if float(student.marks).is_integer()
                    else str(student.marks)
                )
                grade = self.calculate_grade(roll_no)

            lines.append(f"{roll_no}\t{student.name}\t{marks_str}\t{grade}")

        return "\n".join(lines)
