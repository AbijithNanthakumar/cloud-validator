from typing import Dict, List, Tuple
import re

from ai.groq_classifier import GroqClassifier
from ai.gemini_remediator import GeminiRemediator
from models.finding import Finding
from models.ai_result import AIResult


class AIEngine:

    MAX_AI_FINDINGS = 3

    def __init__(self):

        self.groq = GroqClassifier()
        self.gemini = GeminiRemediator()

        self._cache: Dict[Tuple, AIResult] = {}

    def _finding_key(self, finding: Finding) -> Tuple:

        return (
            finding.check_id,
            finding.resource,
            finding.file_name,
            finding.severity,
        )

    def _extract_section(
        self,
        text: str,
        section_name: str,
        next_sections: List[str]
    ) -> str:

        if not text:
            return ""

        next_section_pattern = "|".join(
            re.escape(section)
            for section in next_sections
        )

        if next_section_pattern:

            end_pattern = (
                rf"(?=\n\s*"
                rf"(?:\d+\.\s*)?"
                rf"(?:#+\s*)?"
                rf"(?:{next_section_pattern})"
                rf"\s*:?\s*(?:\n|$)"
                rf"|\Z)"
            )

        else:

            end_pattern = r"(?=\Z)"

        pattern = (
            rf"(?:^|\n)\s*"
            rf"(?:\d+\.\s*)?"
            rf"(?:#+\s*)?"
            rf"{re.escape(section_name)}"
            rf"\s*:?\s*\n?"
            rf"(.*?)"
            rf"{end_pattern}"
        )

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        if not match:
            return ""

        return match.group(1).strip()

    def _extract_terraform(self, text: str) -> str:

        if not text:
            return ""

        fenced_match = re.search(
            r"```(?:terraform|hcl)?\s*(.*?)```",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        if fenced_match:
            return fenced_match.group(1).strip()

        resource_match = re.search(
            r"(resource\s+\".*?\{.*?\})",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        if resource_match:
            return resource_match.group(1).strip()

        return "No Terraform code was generated."

    def _parse_gemini_response(
        self,
        response: str
    ) -> Tuple[str, str, str]:

        sections = [
            "ROOT CAUSE",
            "BUSINESS IMPACT",
            "TERRAFORM REMEDIATION",
            "BEST PRACTICE",
        ]

        root_cause = self._extract_section(
            response,
            "ROOT CAUSE",
            sections[1:]
        )

        business_impact = self._extract_section(
            response,
            "BUSINESS IMPACT",
            sections[2:]
        )

        terraform_section = self._extract_section(
            response,
            "TERRAFORM REMEDIATION",
            sections[3:]
        )

        best_practice = self._extract_section(
            response,
            "BEST PRACTICE",
            []
        )

        remediation_parts = []

        if root_cause:
            remediation_parts.append(
                f"Root Cause:\n{root_cause}"
            )

        if business_impact:
            remediation_parts.append(
                f"Business Impact:\n{business_impact}"
            )

        remediation = "\n\n".join(
            remediation_parts
        )

        if not remediation:
            remediation = response.strip()

        terraform_fix = self._extract_terraform(
            terraform_section
        )

        if (
            not terraform_fix
            or terraform_fix == "No Terraform code was generated."
        ):
            terraform_fix = self._extract_terraform(
                response
            )

        if not best_practice:

            best_practice = (
                "Follow Azure security best practices and "
                "apply the recommended Terraform configuration."
            )

        return (
            remediation,
            terraform_fix,
            best_practice
        )

    def analyze(
        self,
        findings: List[Finding]
    ) -> List[AIResult]:

        results = []

        selected_findings = findings[
            :self.MAX_AI_FINDINGS
        ]

        for finding in selected_findings:

            key = self._finding_key(
                finding
            )

            if key in self._cache:

                results.append(
                    self._cache[key]
                )

                continue

            explanation = self.groq.classify(
                finding
            )

            gemini_response = self.gemini.remediate(
                finding
            )

            (
                remediation,
                terraform_fix,
                best_practice
            ) = self._parse_gemini_response(
                gemini_response
            )

            ai_result = AIResult(
                finding=finding,
                explanation=explanation,
                remediation=remediation,
                terraform_fix=terraform_fix,
                best_practice=best_practice,
                severity=finding.severity,
                source="Groq + Gemini",
            )

            self._cache[key] = ai_result

            results.append(
                ai_result
            )

        return results