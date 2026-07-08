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