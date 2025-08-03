from typing import Set, List, Optional
from tabulate import tabulate

class Teacher:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        can_teach_subjects: Set[str]
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects: Set[str] = set()

    def __repr__(self):
        return f"<Teacher {self.first_name} {self.last_name}>"

def create_schedule(
    subjects: Set[str],
    teachers: List[Teacher]
) -> Optional[List[Teacher]]:
    uncovered = set(subjects)
    schedule: List[Teacher] = []
    candidates = teachers[:]

    while uncovered and candidates:
        best = None
        best_count = 0
        for t in candidates:
            cover = t.can_teach_subjects & uncovered
            if len(cover) > best_count or (
               len(cover) == best_count and best and t.age < best.age
            ):
                best = t
                best_count = len(cover)

        if not best or best_count == 0:
            break

        best.assigned_subjects = best.can_teach_subjects & uncovered
        schedule.append(best)
        uncovered -= best.assigned_subjects
        candidates.remove(best)

    return None if uncovered else schedule

if __name__ == "__main__":
    subjects = {"Mathematics", "Physics", "Chemistry", "Informatics", "Biology"}
    teachers = [
        Teacher("Oleksandr","Ivanenko",45,"o.ivanenko@example.com",{"Mathematics","Physics"}),
        Teacher("Maria",     "Petrenko",  38,"m.petrenko@example.com",  {"Chemistry"}),
        Teacher("Serhii",    "Kovalenko", 50,"s.kovalenko@example.com", {"Informatics","Mathematics"}),
        Teacher("Nataliia",  "Shevchenko",29,"n.shevchenko@example.com",{"Biology","Chemistry"}),
        Teacher("Dmytro",    "Bondarenko",35,"d.bondarenko@example.com", {"Physics","Informatics"}),
        Teacher("Olena",     "Hrytsenko", 42,"o.grytsenko@example.com", {"Biology"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule is None:
        print("Unable to cover all subjects with the available teachers.")
    else:
        rows = []
        for t in schedule:
            rows.append([
                t.first_name + " " + t.last_name,
                t.age,
                t.email,
                ", ".join(sorted(t.assigned_subjects))
            ])

        print("\nClass Schedule:\n")
        print(tabulate(
            rows,
            headers=["Teacher", "Age", "Email", "Assigned Subjects"],
            tablefmt="pretty",
            stralign="center",
            numalign="center"
        ))
