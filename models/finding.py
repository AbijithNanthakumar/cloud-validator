from dataclasses import dataclass


@dataclass
class Finding:
    """
    Represents a single security finding produced by
    Checkov or OPA.
    """

    check_id: str
    check_name: str
    resource: str
    file_name: str
    guideline: str
    severity: str

    # Source of the finding
    # Example:
    #   Checkov
    #   OPA
    source: str = "Checkov"

    def __post_init__(self):
        """
        Normalize severity values so the dashboard and reporting
        layer always receive a consistent classification.
        """

        if self.severity is None:
            self.severity = "Unknown"

        severity = str(self.severity).strip().lower()

        severity_map = {
            "critical": "Critical",
            "high": "High",
            "medium": "Medium",
            "moderate": "Medium",
            "low": "Low",
            "info": "Low",
            "informational": "Low",
            "unknown": "Unknown",
            "": "Unknown",
        }

        self.severity = severity_map.get(
            severity,
            "Unknown"
        )