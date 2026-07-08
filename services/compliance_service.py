from models.report import ScanReport
from services.scoring_service import ScoringService


class ComplianceService:
    """
    Determines compliance based on
    the overall security score.
    """

    @staticmethod
    def get_compliance_status(report: ScanReport) -> tuple[float, str]:

        score = ScoringService.calculate_score(report)

        if score >= 90:
            status = "Compliant"

        elif score >= 70:
            status = "Needs Improvement"

        else:
            status = "Non-Compliant"

        return score, status