import openai
import os

# Set up OpenAI API key securely from environment variable (replace if using a direct key)
openai.api_key = os.getenv("OPENAI_API_KEY", "import_key")

# List of phrases
phrases = [
    "increase tax",
    "reduce healthcare costs"
]

# Initialize an empty list to store generated questions
questions = []

# Step 1: Generate questions from phrases
for phrase in phrases:
    try:
        # Instruct ChatGPT to turn the phrase into a question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please turn the following phrase into a question: '{phrase}'"}
            ]
        )
        
        # Extract the generated question
        generated_question = response['choices'][0]['message']['content'].strip()
        questions.append(generated_question)
    except Exception as e:
        print(f"Error occurred for phrase '{phrase}': {e}")
        questions.append("Error occurred")
