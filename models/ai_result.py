from dataclasses import dataclass

from models.finding import Finding


@dataclass
class AIResult:
    """
    Represents the final AI analysis
    for a security finding.
    """

    finding: Finding

    explanation: str

    remediation: str

    terraform_fix: str

    best_practice: str

    severity: str

    source: str