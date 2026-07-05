import json
from pathlib import Path

from models.finding import Finding


class CheckovParser:

    def __init__(self, report_path: str):
        self.report_path = Path(report_path)

    def parse(self):
        with open(self.report_path, "r", encoding="utf-8") as file:
            report = json.load(file)

        findings = []

        failed_checks = report["results"]["failed_checks"]

        for check in failed_checks:

            finding = Finding(
                check_id=check["check_id"],
                check_name=check["check_name"],
                resource=check["resource"],
                file_name=Path(check["file_path"]).name,
                guideline=check["guideline"],
                severity="Unknown"
            )

            findings.append(finding)

        return findings