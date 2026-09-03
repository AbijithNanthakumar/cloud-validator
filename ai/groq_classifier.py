from groq import Groq

from config.settings import GROQ_API_KEY


class GroqClassifier:
    """
    Uses Groq LLM to classify
    cloud security findings.
    """

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def classify(self, finding):

        prompt = f"""
You are a Cloud Security Expert.

Analyze this security finding.

Check ID:
{finding.check_id}

Rule:
{finding.check_name}

Severity:
{finding.severity}

Explain:

1. Why this issue is dangerous.
2. What could happen if ignored.
3. Give a concise security recommendation.

Keep the answer under 200 words.
"""

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.choices[0].message.content