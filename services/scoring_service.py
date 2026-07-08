from models.report import ScanReport


class ScoringService:
    """
    Calculates the overall security score
    from a ScanReport.
    """

    @staticmethod
    def calculate_score(report: ScanReport) -> float:
        """
        Returns the security score as a percentage.
        """

        total_checks = report.passed + report.failed

        if total_checks == 0:
            return 100.0

        score = (report.passed / total_checks) * 100

        return round(score, 2)