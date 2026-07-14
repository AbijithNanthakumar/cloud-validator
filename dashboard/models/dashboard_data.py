from dataclasses import dataclass
from typing import List

from models.report import ScanReport
from models.finding import Finding
from models.ai_result import AIResult

from dashboard.models.dashboard_summary import DashboardSummary


@dataclass
class DashboardData:

    summary: DashboardSummary

    report: ScanReport

    findings: List[Finding]

    ai_results: List[AIResult]