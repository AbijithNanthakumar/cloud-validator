from dataclasses import dataclass

@dataclass
class Finding:
    check_id: str
    check_name: str
    resource: str
    file_name: str
    guideline: str
    severity: str = "Unknown"
