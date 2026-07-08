import json
import subprocess

from config.settings import OPA_EXECUTABLE
from models.finding import Finding


class OPAScanner:
    """
    Executes OPA policies and converts
    the result into Finding objects.
    """

    def __init__(self):

        self.policy = "policies/azure/storage.rego"

        self.input = "policies/input/storage.json"

    def scan(self):

        command = [
            OPA_EXECUTABLE,
            "eval",
            "--format=json",
            "--data",
            self.policy,
            "--input",
            self.input,
            "data.cloudvalidator.azure.deny"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        opa_output = json.loads(result.stdout)

        findings = []

        try:

            messages = opa_output["result"][0]["expressions"][0]["value"]

            for index, message in enumerate(messages, start=1):

                findings.append(
                    Finding(
                        check_id=f"OPA_{index:03}",
                        check_name=message,
                        resource="Storage Account",
                        file_name="storage.rego",
                        guideline="Custom Organization Policy",
                        severity="Medium",
                        source="OPA"
                    )
                )

        except (KeyError, IndexError):

            pass

        return findings