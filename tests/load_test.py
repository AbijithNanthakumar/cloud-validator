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

    total_runs = 20
    expected_findings = 17
    times = []
    successful_runs = 0

    print("=" * 60)
    print("PSIDDHI VALIDATION LOAD TEST")
    print("=" * 60)

    overall_start = time.perf_counter()

    for run in range(1, total_runs + 1):

        start = time.perf_counter()

        try:
            report, findings = engine.validate()

            elapsed = time.perf_counter() - start
            times.append(elapsed)

            if (
                report.passed == 9
                and report.failed == 16
                and report.resource_count == 3
                and len(findings) == expected_findings
            ):
                successful_runs += 1
                status = "PASS"
            else:
                status = "FAIL"

            print(
                f"Run {run:02d}: {status} | "
                f"{elapsed:.3f}s | "
                f"Findings: {len(findings)}"
            )

        except Exception as exc:
            print(
                f"Run {run:02d}: FAIL | "
                f"Error: {exc}"
            )

    total_time = time.perf_counter() - overall_start

    print("-" * 60)

    if times:
        print(f"Total Time   : {total_time:.3f} seconds")
        print(f"Average Time : {sum(times) / len(times):.3f} seconds")
        print(f"Fastest Run  : {min(times):.3f} seconds")
        print(f"Slowest Run  : {max(times):.3f} seconds")

    print(f"Total Runs   : {total_runs}")
    print(f"Successful   : {successful_runs}")
    print(f"Failed       : {total_runs - successful_runs}")

    reliability = (
        successful_runs / total_runs
    ) * 100

    print(f"Reliability  : {reliability:.1f}%")

    print("-" * 60)

    if successful_runs == total_runs:
        print("RESULT: PASS")
        print("Validation remained stable under repeated load.")
    else:
        print("RESULT: REVIEW")

    print("=" * 60)


if __name__ == "__main__":
    main()