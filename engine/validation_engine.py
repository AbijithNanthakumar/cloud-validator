from parsers.checkov_parser import CheckovParser
from scanners.opa_scanner import OPAScanner


class ValidationEngine:
    """
    Central engine responsible for
    validating Terraform infrastructure
    using multiple security engines.
    """

    def __init__(self):

        self.checkov_parser = CheckovParser("reports/results_json.json")

        self.opa_scanner = OPAScanner()

    def validate(self):

        report = self.checkov_parser.parse()

        checkov_findings = report.findings

        opa_findings = self.opa_scanner.scan()

        all_findings = checkov_findings + opa_findings

        return report, all_findings