from openai import OpenAI

# Initialize client
client = OpenAI()

# Zero-shot system prompt
system_prompt = """
You are an AI assistant that answers questions about technology in a concise and beginner-friendly way.
"""

# User question (zero-shot: no examples, just the task)
user_prompt = "Explain what Docker is in simple terms."

# Make request to the model
response = client.chat.completions.create(
    model="gpt-4.1-mini",  # you can change to "gpt-4.1" or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.7
)

# Print the response
print("AI Response:", response.choices[0].message["content"])
