import os
import sys
import time

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from engine.validation_engine import ValidationEngine


def main():
    engine = ValidationEngine()

    total_runs = 10
    successful_runs = 0
    failed_runs = 0
    expected_findings = 17

    print("=" * 60)
    print("PSIDDHI VALIDATION RELIABILITY TEST")
    print("=" * 60)

    for run in range(1, total_runs + 1):
        start = time.perf_counter()

        try:
            report, findings = engine.validate()

            elapsed = time.perf_counter() - start

            if (
                report.passed == 9
                and report.failed == 16
                and report.resource_count == 3
                and len(findings) == expected_findings
            ):
                successful_runs += 1
                status = "PASS"
            else:
                failed_runs += 1
                status = "FAIL"

            print(
                f"Run {run:02d}: {status} | "
                f"{elapsed:.3f}s | "
                f"Findings: {len(findings)}"
            )

        except Exception as exc:
            failed_runs += 1

            print(
                f"Run {run:02d}: FAIL | "
                f"Error: {exc}"
            )

    print("-" * 60)
    print(f"Total Runs      : {total_runs}")
    print(f"Successful Runs : {successful_runs}")
    print(f"Failed Runs     : {failed_runs}")

    reliability = (
        successful_runs / total_runs
    ) * 100

    print(f"Reliability     : {reliability:.1f}%")

    print("-" * 60)

    if failed_runs == 0:
        print("RESULT: PASS")
        print("All validation runs completed consistently.")
    else:
        print("RESULT: REVIEW")
        print("One or more validation runs failed.")

    print("=" * 60)


if __name__ == "__main__":
    main()