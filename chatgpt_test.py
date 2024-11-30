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
            messages=[{"role": "user", "content": prompt}],  # Message format
            max_tokens=200,  # Increase token limit for complete code
            temperature=0.5  # Reduce creativity for more structured code
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main function
if __name__ == "__main__":
    prompt = prompt = "Write a Python program that checks if a number is prime. The program must be clean, without Markdown formatting, comments, or examples. The code should be ready to run as is."
    generated_code = generate_code(prompt)
    print(generated_code)

    with open("generatedcode.py", "w") as file:
        file.write(generated_code)
