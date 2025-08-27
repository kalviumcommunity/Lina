from openai import OpenAI

client = OpenAI()

# Chain of Thought Prompting for LinkedIn Assistant
def generate_linkedin_post(topic):
    system_prompt = """
    Role: You are a LinkedIn Content Creator Assistant.
    Task: Help users write engaging LinkedIn posts.
    Style: Professional yet approachable, encouraging audience engagement.
    Format: Always return in JSON with:
    {
      "reasoning": "",
      "final_post": ""
    }
    """

    user_prompt = f"""
    Topic: {topic}

    Think step by step:
    1. Identify the key audience for this post.
    2. Decide the right tone (professional, inspiring, informative, casual).
    3. Break the topic into 2–3 key points for clarity.
    4. Add an engaging hook at the beginning.
    5. Conclude with a call-to-action (e.g., comment, share, connect).

    Finally, generate the LinkedIn post.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use GPT-4o-mini or GPT-4o
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    topic = "The importance of learning Data Structures & Algorithms for career growth"
    post = generate_linkedin_post(topic)
    print(post)
