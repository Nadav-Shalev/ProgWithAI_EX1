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
            temperature=0.2  # Reduce creativity for more structured code
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to clean the generated code
def clean_code(generated_code):
    try:
        # Remove duplicated lines
        lines = generated_code.split("\n")
        unique_lines = []
        for line in lines:
            if line.strip() not in unique_lines:
                unique_lines.append(line.strip())
        return "\n".join(unique_lines)
    except Exception as e:
        return f"Error while cleaning code: {str(e)}"

# Main function
if __name__ == "__main__":
    prompt = "Write a clean Python program that checks if a number is prime. Ensure there are no repetitions or redundant code. Output only the program code without examples or comments."
    print("Generating code...")
    generated_code = generate_code(prompt)
    cleaned_code = clean_code(generated_code)
    print("Generated Code:\n", cleaned_code)
