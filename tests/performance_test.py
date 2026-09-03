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
    times = []

    print("=" * 60)
    print("PSIDDHI VALIDATION PERFORMANCE TEST")
    print("=" * 60)

    for run in range(3):
        start = time.perf_counter()

        report, findings = engine.validate()

        elapsed = time.perf_counter() - start
        times.append(elapsed)

        print(
            f"Run {run + 1}: "
            f"{elapsed:.3f} seconds | "
            f"Findings: {len(findings)}"
        )

    average = sum(times) / len(times)

    print("-" * 60)
    print(f"Average: {average:.3f} seconds")
    print(f"Passed: {report.passed}")
    print(f"Failed: {report.failed}")
    print(f"Resources: {report.resource_count}")
    print(f"Total Findings: {len(findings)}")
    print("=" * 60)


if __name__ == "__main__":
    main()