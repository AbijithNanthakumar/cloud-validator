from engine.validation_engine import ValidationEngine
from ai.ai_engine import AIEngine


def main():

    # -----------------------------------------
    # Validation Phase
    # -----------------------------------------

    validation_engine = ValidationEngine()

    report, findings = validation_engine.validate()

    # -----------------------------------------
    # AI Phase
    # -----------------------------------------

    ai_engine = AIEngine()

    ai_results = ai_engine.analyze(findings)

    # -----------------------------------------
    # Display First Result
    # -----------------------------------------

    print("\n" + "=" * 70)
    print("AI CLOUD VALIDATOR")
    print("=" * 70)

    print(f"Total Findings : {len(findings)}")

    print("=" * 70)

    first_result = ai_results[0]

    finding = first_result["finding"]

    print(f"\nFinding : {finding.check_name}")

    print("\nAI Analysis:\n")

    print(first_result["analysis"])


if __name__ == "__main__":
    main()