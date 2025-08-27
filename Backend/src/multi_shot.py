from openai import OpenAI

# Initialize the client
client = OpenAI(api_key="your_api_key_here")

# Multi-shot examples
multi_shot_prompt = """
You are an AI Assistant that helps users summarize and answer questions from PDFs.
You must only answer using the content inside the PDF and never add external knowledge.
Always respond in JSON format:
{
  "answer": "",
  "summary": "",
  "key_points": []
}

Examples:

Example 1:
User Question: "What is the main topic of the PDF?"
PDF Content: "This PDF is about climate change and its global effects."
AI Response:
{
  "answer": "The PDF discusses climate change and its effects worldwide.",
  "summary": "Focuses on global warming and environmental impact.",
  "key_points": ["Climate change", "Global effects", "Environmental impact"]
}

Example 2:
User Question: "List the challenges mentioned in the PDF."
PDF Content: "The document highlights food shortages, rising sea levels, and health issues."
AI Response:
{
  "answer": "The challenges are food shortages, rising sea levels, and health issues.",
  "summary": "Three main challenges are covered.",
  "key_points": ["Food shortages", "Rising sea levels", "Health issues"]
}

Now, here is the new user question:

User Question: {question}
PDF Content: {pdf_content}

AI Response:
"""

# Function for multi-shot prompting
def ask_pdf_ai(question, pdf_content):
    # Fill the multi-shot template
    prompt = multi_shot_prompt.format(question=question, pdf_content=pdf_content)
    
    # Send to the model
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can also use gpt-4o or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are an AI PDF Expert Assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2  # Lower temp = more structured answers
    )
    
    # Return only the assistant's JSON response
    return response.choices[0].message.content


# Example usage
if __name__ == "__main__":
    user_question = "What solutions does the PDF suggest for climate change?"
    pdf_text = "The document suggests renewable energy adoption and reducing carbon emissions."
    
    result = ask_pdf_ai(user_question, pdf_text)
    print(result)
