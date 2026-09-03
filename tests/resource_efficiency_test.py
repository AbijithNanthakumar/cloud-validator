import os
import sys
import time
import tracemalloc

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
    memory_usage = []
    successful_runs = 0

    print("=" * 60)
    print("PSIDDHI RESOURCE EFFICIENCY TEST")
    print("=" * 60)

    tracemalloc.start()

    for run in range(1, total_runs + 1):

        tracemalloc.reset_peak()

        start = time.perf_counter()

        try:
            report, findings = engine.validate()

            elapsed = time.perf_counter() - start

            current_memory, peak_memory = tracemalloc.get_traced_memory()

            times.append(elapsed)
            memory_usage.append(peak_memory)

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
                f"Findings: {len(findings)} | "
                f"Peak Memory: {peak_memory / 1024:.1f} KB"
            )

        except Exception as exc:
            print(
                f"Run {run:02d}: FAIL | "
                f"Error: {exc}"
            )

    tracemalloc.stop()

    print("-" * 60)

    if times:
        average_time = sum(times) / len(times)
        average_memory = sum(memory_usage) / len(memory_usage)
        maximum_memory = max(memory_usage)

        print(
            f"Average Time       : "
            f"{average_time:.3f} seconds"
        )

        print(
            f"Average Peak Memory: "
            f"{average_memory / 1024:.1f} KB"
        )

        print(
            f"Maximum Peak Memory: "
            f"{maximum_memory / 1024:.1f} KB"
        )

    print(f"Total Runs         : {total_runs}")
    print(f"Successful Runs    : {successful_runs}")
    print(f"Expected Findings  : {expected_findings}")

    print("-" * 60)

    if successful_runs == total_runs:
        print("RESULT: PASS")
        print(
            "Validation completed consistently "
            "without resource-related failures."
        )
    else:
        print("RESULT: REVIEW")

    print("=" * 60)


if __name__ == "__main__":
    main() 