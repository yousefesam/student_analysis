class BatchStrategy:

    def analyze(self, students, batch_size=100):

        subjects = ["math", "physics", "cs"]

        final_results = []

        for subject in subjects:

            total = 0
            highest = 0

            passed = 0
            failed = 0

            passed_total = 0
            failed_total = 0

            count = 0

            for i in range(0, len(students), batch_size):

                batch = students[i:i + batch_size]

                for s in batch:

                    grade = getattr(s, subject)

                    total += grade
                    count += 1

                    if grade > highest:
                        highest = grade

                    if grade >= 50:
                        passed += 1
                        passed_total += grade
                    else:
                        failed += 1
                        failed_total += grade

            avg = total / count

            passed_avg = (
                passed_total / passed
                if passed > 0 else 0
            )

            failed_avg = (
                failed_total / failed
                if failed > 0 else 0
            )

            final_results.append({
                "subject": subject,
                "avg_grades": round(avg, 2),
                "passed": passed,
                "failed": failed,
                "passed_avg": round(passed_avg, 2),
                "failed_avg": round(failed_avg, 2),
                "highest": highest
            })

        return final_results