from engine.validation_engine import ValidationEngine
from services.ai_analysis_service import AIAnalysisService


def main():

    print("=" * 70)
    print("PSIDDHI AI CLOUD VALIDATOR")
    print("=" * 70)

    # -------------------------------
    # Validation Phase
    # -------------------------------

    validation_engine = ValidationEngine()

    report, findings = validation_engine.validate()

    print(f"\nPassed Checks : {report.passed}")
    print(f"Failed Checks : {report.failed}")
    print(f"Resources     : {report.resource_count}")
    print(f"Findings      : {len(findings)}")

    # -------------------------------
    # AI Phase
    # -------------------------------

    service = AIAnalysisService()

    # Analyze only the first finding during development
    ai_results = service.analyze_findings(findings[:1])

    result = ai_results[0]

    print("\n" + "=" * 70)
    print("FIRST SECURITY FINDING")
    print("=" * 70)

    print(f"Source     : {result.finding.source}")
    print(f"Check ID   : {result.finding.check_id}")
    print(f"Rule       : {result.finding.check_name}")

    print("\n" + "=" * 70)
    print("GROQ ANALYSIS")
    print("=" * 70)

    print(result.explanation)

    print("\n" + "=" * 70)
    print("GEMINI REMEDIATION")
    print("=" * 70)

    print(result.remediation)

    print("\n" + "=" * 70)
    print("PIPELINE STATUS")
    print("=" * 70)

    print("✓ Validation Engine")
    print("✓ AI Analysis Service")
    print("✓ AI Engine")
    print("✓ Groq")
    print("✓ Gemini")
    print("✓ AI Result")


if __name__ == "__main__":
    main()