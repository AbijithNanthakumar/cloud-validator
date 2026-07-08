from typing import List

from ai.groq_classifier import GroqClassifier
from models.finding import Finding


class AIEngine:
    """
    Coordinates all AI operations.

    Currently:
        - Groq Classification

    Future:
        - Gemini Remediation
        - LangChain Workflow
    """

    def __init__(self):

        self.groq_classifier = GroqClassifier()

    def analyze(self, findings: List[Finding]) -> List[dict]:
        """
        Analyze all findings using AI.

        Returns:
            List of AI analysis results.
        """

        results = []

        for finding in findings:

            analysis = self.groq_classifier.classify(finding)

            results.append({
                "finding": finding,
                "analysis": analysis
            })

        return results