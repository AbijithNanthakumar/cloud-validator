from typing import Dict, List, Tuple

from ai.groq_classifier import GroqClassifier
from ai.gemini_remediator import GeminiRemediator

from models.finding import Finding
from models.ai_result import AIResult


class AIEngine:
    """
    Central AI orchestration engine.

    Responsible for coordinating Groq and Gemini
    and returning unified AIResult objects.

    AI analysis is intentionally limited to a small number
    of findings to avoid excessive API usage during
    development and dashboard refreshes.
    """

    MAX_AI_FINDINGS = 3

    def __init__(self):

        self.groq = GroqClassifier()
        self.gemini = GeminiRemediator()

        # Cache AI results for findings already processed
        # during the current application session.
        self._cache: Dict[Tuple, AIResult] = {}

    def _finding_key(self, finding: Finding) -> Tuple:
        """
        Creates a stable key for identifying the same finding.
        """

        return (
            finding.check_id,
            finding.resource,
            finding.file_name,
            finding.severity,
        )

    def analyze(
        self,
        findings: List[Finding]
    ) -> List[AIResult]:
        """
        Analyze a limited number of findings using
        Groq and Gemini.

        Cached findings are returned without making
        additional API calls.
        """

        results = []

        # Limit AI processing to avoid unnecessary API usage.
        selected_findings = findings[:self.MAX_AI_FINDINGS]

        for finding in selected_findings:

            key = self._finding_key(finding)

            # Reuse previously generated AI result.
            if key in self._cache:
                results.append(self._cache[key])
                continue

            # Groq classification
            explanation = self.groq.classify(finding)

            # Gemini remediation
            remediation = self.gemini.remediate(finding)

            # Build unified AI result
            ai_result = AIResult(
                finding=finding,
                explanation=explanation,
                remediation=remediation,
                terraform_fix="To be generated",
                best_practice="To be generated",
                severity=finding.severity,
                source="Groq + Gemini"
            )

            # Store result for reuse
            self._cache[key] = ai_result

            results.append(ai_result)

        return results