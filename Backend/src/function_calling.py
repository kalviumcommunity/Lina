from openai import OpenAI

client = OpenAI()

# Define available functions (tools)
functions = [
    {
        "name": "schedule_linkedin_post",
        "description": "Schedule a LinkedIn post at a given time",
        "parameters": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The content of the LinkedIn post"
                },
                "time": {
                    "type": "string",
                    "description": "The time to schedule the post in ISO 8601 format (YYYY-MM-DDTHH:MM:SS)"
                }
            },
            "required": ["content", "time"]
        },
    },
    {
        "name": "suggest_hashtags",
        "description": "Suggest relevant hashtags for a LinkedIn post",
        "parameters": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The content of the LinkedIn post"
                }
            },
            "required": ["content"]
        },
    }
]

# Dummy implementations of functions
def schedule_linkedin_post(content, time):
    return f"✅ Post scheduled: '{content}' at {time}"

def suggest_hashtags(content):
    return ["#AI", "#LinkedInTips", "#Productivity"]


# Conversation loop with function calling
def chat_with_linkedin_assistant(user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a LinkedIn Assistant AI."},
            {"role": "user", "content": user_message},
        ],
        functions=functions,
        function_call="auto",  # let the model decide when to call a function
    )

    message = response.choices[0].message

    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        arguments = eval(message["function_call"]["arguments"])  # careful in prod, use json.loads
        
        if function_name == "schedule_linkedin_post":
            result = schedule_linkedin_post(arguments["content"], arguments["time"])
        elif function_name == "suggest_hashtags":
            result = suggest_hashtags(arguments["content"])
        else:
            result = "Function not implemented."

        return {"AI": message, "Function Result": result}
    
    return {"AI": message}


# Example usage
print(chat_with_linkedin_assistant("Schedule a LinkedIn post saying 'Excited to launch my new AI project!' tomorrow at 10 AM"))
print(chat_with_linkedin_assistant("Suggest hashtags for a post about AI and career growth"))
