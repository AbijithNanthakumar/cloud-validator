from dataclasses import dataclass

from models.finding import Finding


@dataclass
class AIResult:
    """
    Represents the final AI analysis
    for a security finding.
    """

    finding: Finding

    # Groq security analysis
    explanation: str

    # Gemini remediation guidance
    remediation: str

    # Extracted Terraform remediation
    terraform_fix: str

    # Security best-practice recommendation
    best_practice: str

    # Final severity assigned to the finding
    severity: str

    # AI providers used for the result
    source: str