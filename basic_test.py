import os

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API Key retrieved successfully!")
else:
    print("API Key not found. Please check your environment variables.")
