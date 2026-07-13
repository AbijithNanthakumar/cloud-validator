from engine.validation_engine import ValidationEngine
from services.ai_analysis_service import AIAnalysisService

from models.dashboard_summary import DashboardSummary
from models.dashboard_data import DashboardData


class DashboardService:
    """
    Service responsible for preparing dashboard
    data for the UI.
    """

    def __init__(self):
        self.validation_engine = ValidationEngine()
        self.ai_service = AIAnalysisService()

    def load_dashboard(self):

        # Execute validation
        report, findings = self.validation_engine.validate()

        # Generate AI analysis
        ai_results = self.ai_service.analyze_findings(findings)

        # Calculate security score
        total_checks = report.passed + report.failed

        security_score = (
            round((report.passed / total_checks) * 100)
            if total_checks > 0
            else 0
        )

        # Build dashboard summary
        summary = DashboardSummary(
            security_score=security_score,
            compliance=(
                "Compliant"
                if report.failed == 0
                else "Non-Compliant"
            ),
            passed=report.passed,
            failed=report.failed,
            skipped=report.skipped,
            resources=report.resource_count,
        )

        # Return dashboard data
        return DashboardData(
            summary=summary,
            report=report,
            findings=findings,
            ai_results=ai_results,
        )