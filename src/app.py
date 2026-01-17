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
