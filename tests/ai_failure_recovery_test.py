import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from engine.validation_engine import ValidationEngine
from services.ai_analysis_service import AIAnalysisService


def main():
    print("=" * 60)
    print("PSIDDHI AI FAILURE RECOVERY TEST")
    print("=" * 60)

    # ---------------------------------------------------------
    # Run normal validation first.
    # ---------------------------------------------------------

    validation_engine = ValidationEngine()

    report, findings = validation_engine.validate()

    print(f"Validation Passed : {report.passed}")
    print(f"Validation Failed : {report.failed}")
    print(f"Resources         : {report.resource_count}")
    print(f"Findings          : {len(findings)}")

    # ---------------------------------------------------------
    # Simulate an unavailable AI service.
    # ---------------------------------------------------------

    ai_service = AIAnalysisService()

    def simulated_ai_failure(_):
        raise Exception("SIMULATED AI PROVIDER UNAVAILABLE")

    ai_service.ai_engine.analyze = simulated_ai_failure

    ai_results = ai_service.analyze_findings(findings[:1])

    # ---------------------------------------------------------
    # Verify recovery behavior.
    # ---------------------------------------------------------

    validation_ok = (
        report.passed == 9
        and report.failed == 16
        and report.resource_count == 3
        and len(findings) == 17
    )

    ai_failure_handled = ai_results == []

    print("-" * 60)
    print(f"Validation Still Works : {validation_ok}")
    print(f"AI Failure Handled     : {ai_failure_handled}")
    print(f"AI Results Returned    : {len(ai_results)}")
    print("-" * 60)

    if validation_ok and ai_failure_handled:
        print("RESULT: PASS")
        print(
            "Core validation remains operational "
            "when the AI provider is unavailable."
        )
    else:
        print("RESULT: REVIEW")

    print("=" * 60)


if __name__ == "__main__":
    main()