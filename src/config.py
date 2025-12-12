import os

# Load the Groq API key from the environment; raise a clear error if missing
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY not set in environment variables")
