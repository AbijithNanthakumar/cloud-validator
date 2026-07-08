from typing import List

from ai.ai_engine import AIEngine
from models.finding import Finding
from models.ai_result import AIResult


class AIAnalysisService:
    """
    Business service responsible for AI analysis workflow.
    """

    def __init__(self):
        self.ai_engine = AIEngine()

    def analyze_findings(
        self,
        findings: List[Finding]
    ) -> List[AIResult]:

        return self.ai_engine.analyze(findings)