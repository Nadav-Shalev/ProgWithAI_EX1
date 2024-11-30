from openai import OpenAI
import os

# Retrieve the API Key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise Exception("OPENAI_API_KEY is not set in the environment variables!")

# Create an OpenAI client object
client = OpenAI(api_key=api_key)

# Function to send a request to ChatGPT
def generate_code(prompt):
    try:
        response = client.ChatCompletion.create(
            model="gpt-4o-mini",  # Model to use
            messages=[{"role": "user", "content": prompt}],  # The prompt to send
            max_tokens=200,  # Maximum length of the response
            temperature=0.5  # Creativity level
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Main function
if __name__ == "__main__":
    prompt = "Create a Python program that checks if a number is prime. Do not write any explanations, just show me the code itself."
    print("Generating code...")
    generated_code = generate_code(prompt)
    print("Generated Code:\n", generated_code)
