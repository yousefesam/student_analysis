import csv
from model.student import Student

class Controller:

    def load_data(self, path):
        students = []

        with open(path, newline='') as f:
            reader = csv.DictReader(f)

            for row in reader:
                students.append(
                    Student(
                        row["name"],
                        row["math"],
                        row["physics"],
                        row["cs"]
                    )
                )

        return students