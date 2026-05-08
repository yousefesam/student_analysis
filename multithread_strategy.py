from concurrent.futures import ThreadPoolExecutor

class MultiThreadStrategy:

    def analyze(self, students):

        subjects = ["math", "physics", "cs"]

        def analyze_subject(subject):

            total = 0
            highest = 0

            passed = 0
            failed = 0

            passed_total = 0
            failed_total = 0

            for s in students:

                grade = getattr(s, subject)

                total += grade

                if grade > highest:
                    highest = grade

                if grade >= 50:
                    passed += 1
                    passed_total += grade
                else:
                    failed += 1
                    failed_total += grade

            avg = total / len(students)

            passed_avg = (
                passed_total / passed
                if passed > 0 else 0
            )

            failed_avg = (
                failed_total / failed
                if failed > 0 else 0
            )

            return {
                "subject": subject,
                "avg_grades": round(avg, 2),
                "passed": passed,
                "failed": failed,
                "passed_avg": round(passed_avg, 2),
                "failed_avg": round(failed_avg, 2),
                "highest": highest
            }

        with ThreadPoolExecutor(max_workers=3) as executor:
            results = list(
                executor.map(analyze_subject, subjects)
            )

        return results