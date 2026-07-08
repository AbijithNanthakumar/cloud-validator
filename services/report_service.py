from models.report import ScanReport
from services.compliance_service import ComplianceService


class ReportService:
    """
    Generates a structured security summary
    from a ScanReport.
    """

    @staticmethod
    def generate_summary(report: ScanReport) -> dict:

        score, compliance = ComplianceService.get_compliance_status(report)

        return {
            "passed_checks": report.passed,
            "failed_checks": report.failed,
            "skipped_checks": report.skipped,
            "resource_count": report.resource_count,
            "security_score": score,
            "compliance_status": compliance,
            "total_findings": len(report.findings)
        }