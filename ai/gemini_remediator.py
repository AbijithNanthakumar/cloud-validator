from google import genai

from config.settings import GEMINI_API_KEY


class GeminiRemediator:
    """
    Generates concise, actionable Terraform remediation guidance
    using Google's Gemini.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def remediate(self, finding):
        """
        Generate remediation guidance for a security finding.

        The prompt is intentionally focused and concise to reduce
        token usage while producing useful remediation output.
        """

        prompt = f"""
You are a Senior Cloud Security Engineer specializing in
Terraform and Azure security.

Analyze ONLY the following security finding:

Check ID:
{finding.check_id}

Rule:
{finding.check_name}

Resource:
{finding.resource}

File:
{finding.file_name}

Provide practical remediation guidance that a developer can
review and apply to the existing Terraform configuration.

Return exactly these four sections:

1. ROOT CAUSE
Explain what security configuration is wrong and why it
causes this finding.

2. BUSINESS IMPACT
Explain the realistic security or business risk if the
issue remains unresolved.

3. TERRAFORM REMEDIATION
Provide ONLY the Terraform configuration relevant to fixing
this specific finding.

IMPORTANT TERRAFORM RULES:
- Do NOT recreate the entire resource unless it is necessary.
- Prefer showing only the relevant Terraform block or
  security rule that needs to be changed.
- Do NOT invent resource names, resource groups, locations,
  IDs, IP addresses, CIDR ranges, passwords, keys, or other
  environment-specific values.
- If a required value is unknown, use an explicit placeholder
  such as "YOUR_TRUSTED_IP_OR_CIDR".
- Never use realistic-looking example values such as
  "203.0.113.0/24" as if they were the user's actual value.
- Do not invent unrelated Terraform resources.
- Do not include configuration unrelated to this finding.
- Keep the Terraform example concise and directly connected
  to the security issue.
- The Terraform must represent a security improvement, not
  simply suppress or bypass the Checkov finding.

4. BEST PRACTICE
Give one concise Azure/Terraform security best practice
directly related to this finding.

Additional rules:
- Be technically accurate.
- Base the remediation only on information available in the
  finding.
- Clearly use placeholders when the actual environment value
  is unavailable.
- Do not recommend disabling security controls.
- Do not claim that a placeholder is an actual configured value.
- Keep the complete response under 300 words.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if not response or not response.text:
            return "Gemini did not return remediation guidance."

        return response.text.strip()