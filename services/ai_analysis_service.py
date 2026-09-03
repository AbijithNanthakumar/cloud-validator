from typing import List

from ai.ai_engine import AIEngine
from models.finding import Finding
from models.ai_result import AIResult


class AIAnalysisService:
    """
    Business service responsible for AI analysis workflow.

    Handles temporary AI provider failures so that the main
    validation pipeline does not crash when an external AI
    service is unavailable.
    """

    def __init__(self):
        self.ai_engine = AIEngine()

    def analyze_findings(
        self,
        findings: List[Finding]
    ) -> List[AIResult]:

        try:
            return self.ai_engine.analyze(findings)

        except Exception as exc:
            print(
                f"[AIAnalysisService] AI analysis unavailable: {exc}"
            )

            return []