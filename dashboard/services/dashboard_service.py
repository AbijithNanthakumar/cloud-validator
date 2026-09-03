import streamlit as st

from engine.validation_engine import ValidationEngine
from services.ai_analysis_service import AIAnalysisService

from dashboard.models.dashboard_summary import DashboardSummary
from dashboard.models.dashboard_data import DashboardData


@st.cache_resource
def get_dashboard_service():
    """
    Creates and reuses a single DashboardService instance
    during the Streamlit application session.
    """
    return DashboardService()


class DashboardService:
    """
    Service responsible for preparing dashboard data.

    AI analysis is NOT executed by default.
    This prevents normal dashboard navigation from
    consuming Groq/Gemini API requests.
    """

    def __init__(self):
        self.validation_engine = ValidationEngine()
        self.ai_service = AIAnalysisService()

    def load_dashboard(
        self,
        include_ai: bool = False
    ) -> DashboardData:
        """
        Loads dashboard data.

        By default, only infrastructure validation is performed.
        AI analysis is executed only when explicitly requested.
        """

        # Execute infrastructure validation
        report, findings = self.validation_engine.validate()

        # AI analysis is optional.
        # Overview, Findings and Reports will use the default False.
        if include_ai:
            ai_results = self.ai_service.analyze_findings(findings)
        else:
            ai_results = []

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