import openai
import os
import subprocess  # Importing subprocess for running the generated file

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
            temperature=0.1  # Reduce creativity for more structured code
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main function
if __name__ == "__main__":
    # Prompt to generate Python code
    prompt = "Write a Python program that checks if a number is prime. The program must be clean, without Markdown formatting, comments, or examples. The code should be ready to run as is. Also please include running unit tests with asserts that check the logic of the program. Make sure to also check interesting edge cases. There should be 3-4 different unit tests and print feedback good/not"
    
    # Generate code using OpenAI API
    generated_code = generate_code(prompt)
    # print(generated_code)

    # Save the generated code to a file named 'generatedcode.py'
    with open("generatedcode.py", "w") as file:
        file.write(generated_code)

    # Run the generated file using subprocess
    try:
        result = subprocess.run(["python", "generatedcode.py"], text=True, capture_output=True, check=True)
        print("\nOutput of generated code:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("\nAn error occurred while running the generated code:")
        print(e.stderr)
    except subprocess.TimeoutExpired:
        print("\nThe generated code took too long to run and was terminated.")
