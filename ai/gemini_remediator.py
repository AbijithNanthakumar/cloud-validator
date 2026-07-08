from google import genai

from config.settings import GEMINI_API_KEY


class GeminiRemediator:
    """
    Generates Terraform remediation
    using Google's Gemini.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def remediate(self, finding):

        prompt = f"""
You are a Senior Cloud Security Engineer.

Security Finding:

Check ID:
{finding.check_id}

Rule:
{finding.check_name}

Generate:

1. Root Cause
2. Business Impact
3. Terraform Remediation
4. Best Practice

Keep the answer under 250 words.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text