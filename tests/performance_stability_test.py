import os
import sys
import time
import statistics

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from engine.validation_engine import ValidationEngine


def main():
    engine = ValidationEngine()

    total_runs = 10
    expected_findings = 17

    times = []
    finding_counts = []

    print("=" * 60)
    print("PSIDDHI PERFORMANCE STABILITY TEST")
    print("=" * 60)

    for run in range(1, total_runs + 1):

        start = time.perf_counter()

        try:
            report, findings = engine.validate()

            elapsed = time.perf_counter() - start

            times.append(elapsed)
            finding_counts.append(len(findings))

            print(
                f"Run {run:02d}: "
                f"{elapsed:.3f}s | "
                f"Findings: {len(findings)}"
            )

        except Exception as exc:

            times.append(None)
            finding_counts.append(None)

            print(
                f"Run {run:02d}: FAIL | "
                f"Error: {exc}"
            )

    successful_times = [
        value for value in times
        if value is not None
    ]

    valid_finding_counts = [
        value for value in finding_counts
        if value is not None
    ]

    if not successful_times:
        print("-" * 60)
        print("RESULT: FAIL")
        print("No successful validation runs.")
        print("=" * 60)
        return

    average = statistics.mean(successful_times)
    median = statistics.median(successful_times)
    fastest = min(successful_times)
    slowest = max(successful_times)

    standard_deviation = (
        statistics.stdev(successful_times)
        if len(successful_times) > 1
        else 0
    )

    results_consistent = (
        len(valid_finding_counts) == total_runs
        and all(
            count == expected_findings
            for count in valid_finding_counts
        )
    )

    print("-" * 60)
    print(f"Average Time       : {average:.3f} seconds")
    print(f"Median Time        : {median:.3f} seconds")
    print(f"Fastest Run        : {fastest:.3f} seconds")
    print(f"Slowest Run        : {slowest:.3f} seconds")
    print(f"Standard Deviation : {standard_deviation:.3f} seconds")
    print(f"Total Runs         : {total_runs}")
    print(f"Successful Runs    : {len(successful_times)}")
    print(f"Expected Findings  : {expected_findings}")
    print(f"Result Consistent  : {results_consistent}")
    print("-" * 60)

    if (
        len(successful_times) == total_runs
        and results_consistent
    ):
        print("RESULT: PASS")
        print(
            "Validation performance remained stable "
            "across all runs."
        )
    else:
        print("RESULT: REVIEW")

    print("=" * 60)


if __name__ == "__main__":
    main()