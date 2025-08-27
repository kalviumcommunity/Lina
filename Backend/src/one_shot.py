from openai import OpenAI

# Initialize client
client = OpenAI(api_key="your_api_key_here")

# One-shot example prompt
one_shot_prompt = """
You are an AI PDF Expert Assistant.
You must always answer strictly in JSON format:
{
  "answer": "",
  "summary": "",
  "key_points": []
}

Example:
User Question: "What is the title of this PDF?"
PDF Content: "The title of the document is 'AI in Education: Future Prospects'."
AI Response:
{
  "answer": "The title of the PDF is 'AI in Education: Future Prospects'.",
  "summary": "The PDF focuses on AI's role in the future of education.",
  "key_points": ["AI in education", "Future prospects", "Technology in learning"]
}

Now, answer the following question strictly using the PDF content.

User Question: "Summarize the introduction section."
PDF Content: "The introduction explains how artificial intelligence is reshaping multiple industries, with a special focus on education, healthcare, and finance."
"""

# Send request to GPT
response = client.chat.completions.create(
    model="gpt-4o-mini",  # you can use gpt-4o or gpt-3.5-turbo too
    messages=[
        {"role": "system", "content": "You are an AI PDF Expert Assistant."},
        {"role": "user", "content": one_shot_prompt}
    ]
)

# Print the response
print(response.choices[0].message.content)
