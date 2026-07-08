from services.scoring_service import ScoringService
from services.compliance_service import ComplianceService
from services.report_service import ReportService
from parsers.checkov_parser import CheckovParser


def main():

    parser = CheckovParser("reports/results_json.json")

    report = parser.parse()
    summary = ReportService.generate_summary(report)

    print("\n" + "=" * 70)
    print("CHECKOV SECURITY REPORT")
    print("=" * 70)

    print(f"Passed Checks : {summary['passed_checks']}")
    print(f"Failed Checks : {summary['failed_checks']}")
    print(f"Skipped Checks: {summary['skipped_checks']}")
    print(f"Resources     : {summary['resource_count']}")
    print(f"Security Score: {summary['security_score']}%")
    print(f"Compliance    : {summary['compliance_status']}")

    print("=" * 70)
    print(f"Total Findings : {summary["total_findings"]}")
    print("=" * 70)

    for finding in report.findings:
        print(f"\nCheck ID   : {finding.check_id}")
        print(f"Check Name : {finding.check_name}")
        print(f"Resource   : {finding.resource}")
        print(f"File       : {finding.file_name}")
        print("-" * 70)


if __name__ == "__main__":
    main()