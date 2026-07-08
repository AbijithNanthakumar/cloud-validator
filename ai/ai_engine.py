from typing import List

from ai.groq_classifier import GroqClassifier
from ai.gemini_remediator import GeminiRemediator

from models.finding import Finding
from models.ai_result import AIResult


class AIEngine:
    """
    Central AI orchestration engine.

    Responsible for coordinating
    all AI providers and returning
    a unified AIResult object.
    """

    def __init__(self):

        self.groq = GroqClassifier()
        self.gemini = GeminiRemediator()

    def analyze(self, findings: List[Finding]) -> List[AIResult]:

        results = []

        for finding in findings:

            explanation = self.groq.classify(finding)

            remediation = self.gemini.remediate(finding)

            ai_result = AIResult(
                finding=finding,
                explanation=explanation,
                remediation=remediation,
                terraform_fix="To be generated",
                best_practice="To be generated",
                severity=finding.severity,
                source="Groq + Gemini"
            )

            results.append(ai_result)

        return results