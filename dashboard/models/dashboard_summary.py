from dataclasses import dataclass


@dataclass
class DashboardSummary:

    security_score: int

    compliance: str

    passed: int

    failed: int

    skipped: int

    resources: int