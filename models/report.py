from dataclasses import dataclass
from typing import List

from models.finding import Finding

@dataclass
class ScanReport:
    passed: int
    failed: int
    skipped: int
    resource_count: int
    findings: List[Finding]