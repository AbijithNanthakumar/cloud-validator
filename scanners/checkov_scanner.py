from parsers.checkov_parser import CheckovParser

parser = CheckovParser("reports/results_json.json")

findings = parser.parse()

print(f"\nTotal Findings: {len(findings)}\n")

for finding in findings:

    print("-" * 70)

    print(f"Check ID   : {finding.check_id}")
    print(f"Check Name : {finding.check_name}")
    print(f"Resource   : {finding.resource}")
    print(f"File       : {finding.file_name}")