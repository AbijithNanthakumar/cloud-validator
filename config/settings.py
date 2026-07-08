"""
Application Configuration
"""

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# --------------------------------------------------
# API KEYS
# --------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --------------------------------------------------
# OPA
# --------------------------------------------------

OPA_EXECUTABLE = r"C:\Users\abijith.nanthakumar\opa.exe"

# --------------------------------------------------
# Reports
# --------------------------------------------------

CHECKOV_REPORT_PATH = "reports/results_json.json"

# --------------------------------------------------
# Policies
# --------------------------------------------------

OPA_POLICY_FOLDER = "policies/azure"

OPA_INPUT_FOLDER = "policies/input"