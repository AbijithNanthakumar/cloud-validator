import json
from pathlib import Path

from models.finding import Finding
from models.report import ScanReport


class CheckovParser:
    """
    Parses a Checkov JSON report and converts it into
    ScanReport and Finding objects.

    Checkov may return severity as null. In that case,
    Psiddhi applies its centralized security-risk
    classification.
    """

    SEVERITY_MAP = {
        "Critical": {
            # Direct exposure of remote administration
            "CKV_AZURE_9",

            # Password-based VM authentication
            "CKV_AZURE_1",
            "CKV_AZURE_149",
        },

        "High": {
            # Storage security and data exposure
            "CKV_AZURE_59",
            "CKV_AZURE_33",
            "CKV_AZURE_190",

            # Strong authentication
            "CKV_AZURE_178",

            # Storage authorization controls
            "CKV2_AZURE_40",
            "CKV2_AZURE_47",

            # Customer-managed encryption
            "CKV2_AZURE_1",
        },

        "Medium": {
            # Storage logging
            "CKV_AZURE_33",

            # TLS configuration
            "CKV_AZURE_44",

            # VM extensions
            "CKV_AZURE_50",

            # Storage private endpoint
            "CKV2_AZURE_33",

            # Storage soft-delete
            "CKV2_AZURE_38",

            # SAS expiration policy
            "CKV2_AZURE_41",
        },

        "Low": {
            # Storage replication
            "CKV_AZURE_206",
        },
    }

    def __init__(self, report_path: str):
        self.report_path = Path(report_path)

    def _normalize_severity(self, severity) -> str:
        """
        Normalize severity values into the standard
        Psiddhi classification.
        """

        if severity is None:
            return "Unknown"

        value = str(severity).strip().lower()

        severity_map = {
            "critical": "Critical",
            "high": "High",
            "medium": "Medium",
            "moderate": "Medium",
            "low": "Low",
            "info": "Low",
            "informational": "Low",
            "unknown": "Unknown",
            "": "Unknown",
        }

        return severity_map.get(value, "Unknown")

    def _get_severity(self, check: dict) -> str:
        """
        Determine finding severity.

        Priority:
        1. Severity explicitly returned by Checkov.
        2. Alternative severity field.
        3. Checkov metadata severity.
        4. Psiddhi centralized classification.
        5. Unknown when no reliable classification exists.
        """

        # -----------------------------------------------------
        # 1. Direct Checkov severity
        # -----------------------------------------------------

        direct_severity = check.get("severity")

        if direct_severity:
            normalized = self._normalize_severity(
                direct_severity
            )

            if normalized != "Unknown":
                return normalized

        # -----------------------------------------------------
        # 2. Alternative severity field
        # -----------------------------------------------------

        alternative_severity = check.get("check_severity")

        if alternative_severity:
            normalized = self._normalize_severity(
                alternative_severity
            )

            if normalized != "Unknown":
                return normalized

        # -----------------------------------------------------
        # 3. Checkov metadata
        # -----------------------------------------------------

        metadata = check.get("metadata", {})

        if isinstance(metadata, dict):
            metadata_severity = metadata.get("severity")

            if metadata_severity:
                normalized = self._normalize_severity(
                    metadata_severity
                )

                if normalized != "Unknown":
                    return normalized

        # -----------------------------------------------------
        # 4. Psiddhi centralized classification
        # -----------------------------------------------------

        check_id = check.get("check_id", "")

        for severity, check_ids in self.SEVERITY_MAP.items():
            if check_id in check_ids:
                return severity

        # -----------------------------------------------------
        # 5. No classification available
        # -----------------------------------------------------

        return "Unknown"

    def parse(self) -> ScanReport:
        """
        Read the Checkov JSON report and convert failed
        checks into Finding objects.
        """

        with open(
            self.report_path,
            "r",
            encoding="utf-8"
        ) as file:
            report = json.load(file)

        summary = report["summary"]

        findings = []

        failed_checks = report["results"]["failed_checks"]

        for check in failed_checks:

            finding = Finding(
                check_id=check["check_id"],
                check_name=check["check_name"],
                resource=check["resource"],
                file_name=Path(
                    check["file_path"]
                ).name,
                guideline=check.get(
                    "guideline",
                    ""
                ),
                severity=self._get_severity(check),
                source="Checkov",
            )

            findings.append(finding)

        return ScanReport(
            passed=summary["passed"],
            failed=summary["failed"],
            skipped=summary["skipped"],
            resource_count=summary["resource_count"],
            findings=findings,
        )
    