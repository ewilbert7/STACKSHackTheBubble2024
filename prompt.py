import openai
import os

# Set up OpenAI API key securely from environment variable (replace if using a direct key)
openai.api_key = os.getenv("OPENAI_API_KEY", "add_key")

# List of phrases

# Initialize an empty list to store generated questions
questions = []

# Step 1: Generate questions from phrases
def generate(input):
    try:
        # Instruct ChatGPT to turn the phrase into a question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please turn the following phrase into a prompt which asks the user how they feel about phrase: '{input[1]}'"} 
            ]
        )
        
        # Extract the generated question
        generated_question = response['choices'][0]['message']['content'].strip()
        questions.append(generated_question)
    except Exception as e:
        print(f"Error occurred for phrase '{input[1]}': {e}")
        questions.append("Error occurred")

print(questions)