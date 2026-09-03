import os
import sys

import pytest

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from engine.validation_engine import ValidationEngine
from dashboard.services.dashboard_service import DashboardService
from services.ai_analysis_service import AIAnalysisService


EXPECTED_PASSED = 9
EXPECTED_FAILED = 16
EXPECTED_RESOURCES = 3
EXPECTED_FINDINGS = 17

VALID_SEVERITIES = {
    "Critical",
    "High",
    "Medium",
    "Low",
}


@pytest.fixture
def validation_result():
    engine = ValidationEngine()
    return engine.validate()


def test_validation_engine_returns_expected_summary(
    validation_result
):
    report, findings = validation_result

    assert report.passed == EXPECTED_PASSED
    assert report.failed == EXPECTED_FAILED
    assert report.resource_count == EXPECTED_RESOURCES
    assert len(findings) == EXPECTED_FINDINGS


def test_all_findings_have_required_metadata(
    validation_result
):
    _, findings = validation_result

    assert findings

    for finding in findings:
        assert finding.check_id
        assert finding.check_name
        assert finding.resource
        assert finding.file_name
        assert finding.severity
        assert finding.source


def test_all_findings_have_valid_severity(
    validation_result
):
    _, findings = validation_result

    for finding in findings:
        assert finding.severity in VALID_SEVERITIES


def test_expected_critical_finding_exists(
    validation_result
):
    _, findings = validation_result

    matching_findings = [
        finding
        for finding in findings
        if finding.check_id == "CKV_AZURE_9"
    ]

    assert len(matching_findings) >= 1

    finding = matching_findings[0]

    assert finding.severity == "Critical"
    assert finding.source == "Checkov"


def test_dashboard_summary_matches_backend():
    dashboard_service = DashboardService()

    dashboard_data = dashboard_service.load_dashboard(
        include_ai=False
    )

    summary = dashboard_data.summary

    assert summary.passed == EXPECTED_PASSED
    assert summary.failed == EXPECTED_FAILED
    assert summary.resources == EXPECTED_RESOURCES
    assert len(dashboard_data.findings) == EXPECTED_FINDINGS


def test_dashboard_security_score():
    dashboard_service = DashboardService()

    dashboard_data = dashboard_service.load_dashboard(
        include_ai=False
    )

    assert dashboard_data.summary.security_score == 36


def test_ai_service_handles_provider_failure():
    ai_service = AIAnalysisService()

    def simulated_failure(_):
        raise Exception(
            "SIMULATED AI PROVIDER FAILURE"
        )

    ai_service.ai_engine.analyze = simulated_failure

    result = ai_service.analyze_findings([])

    assert result == []


def test_dashboard_data_contains_expected_findings():
    dashboard_service = DashboardService()

    dashboard_data = dashboard_service.load_dashboard(
        include_ai=False
    )

    assert dashboard_data.report is not None
    assert dashboard_data.findings is not None
    assert len(dashboard_data.findings) == EXPECTED_FINDINGS


if __name__ == "__main__":
    pytest.main()