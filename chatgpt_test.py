import openai
import os

# Retrieve the API Key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise Exception("OPENAI_API_KEY is not set in the environment variables!")

# Set the API Key for the OpenAI module
openai.api_key = api_key

# Function to send a request to the chat completion endpoint
def generate_code(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use the chat model
            messages=[{"role": "user", "content": prompt}],  # Format required for chat models
            max_tokens=200,  # Limit the length of the response
            temperature=0.5  # Adjust creativity level
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main function
if __name__ == "__main__":
    prompt = "Write a clean Python program that checks if a number is prime. Ensure there are no repetitions or redundant code. Only output the program code."
    print("Generating code...")
    generated_code = generate_code(prompt)
    print("Generated Code:\n", generated_code)
