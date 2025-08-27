# 🎥 Video Script: Explaining System & User Prompt with RTFC Framework

---

### 🟢 Intro (30s)

"Hi everyone, in this video I’ll explain how I designed the **System Prompt** and **User Prompt** for my backend project.
I’ll also show you how I applied the **RTFC framework – Role, Task, Format, and Context –** to structure these prompts in a clear and consistent way."

---

### 🔵 Part 1: System Prompt Explanation (2 min)

#### Narration:

"Let’s start with the **System Prompt**.
The System Prompt defines how the AI should behave throughout the project.
Here’s the exact code snippet I used:"

#### On screen: (show code)

```js
export const systemPrompt = `
Role: You are an AI PDF Expert Assistant.
Task: Help users understand and interact with their uploaded PDFs by answering questions strictly based on PDF content.
Format: Always respond in strict JSON format:
{
  "answer": "",
  "summary": "",
  "key_points": []
}
Context: The user uploads a PDF document. Your job is to extract meaning, summarize sections, and answer questions without using external knowledge.
`;
```

#### Narration:

"Now let me break this down using the **RTFC framework**:

* **Role** → I clearly define the AI as an *AI PDF Expert Assistant*. This sets its identity.
* **Task** → The AI’s main job is to help users understand their PDFs and answer questions based only on the document.
* **Format** → I specify that the response must always be in strict JSON. This keeps answers machine-readable for my backend.
* **Context** → I explain the environment: a user uploads a PDF, and the AI should never use outside knowledge – only the PDF’s content.

This structure ensures the AI is consistent, reliable, and aligned with my project needs."

---

### 🟠 Part 2: User Prompt Explanation (1 min)

#### Narration:

"Next, let’s look at the **User Prompt**.
The User Prompt takes the user’s question and sends it to the AI in a clean and structured way."

#### On screen: (show code)

```js
export const createUserPrompt = (question) => `
User Question: ${question}
`;
```

#### Narration:

"Here, whenever a user asks a question, like *‘Summarize page 2’*, it gets wrapped into the **User Prompt** format:

👉 `User Question: Summarize page 2`

This ensures that the AI always knows exactly what the user is asking, and it can respond following the JSON structure defined in the System Prompt."

---

### 🟣 Part 3: Why RTFC Matters (45s)

#### Narration:

"Using the **RTFC framework** makes my prompts predictable and professional:

* **Role** avoids confusion about AI identity.
* **Task** makes the AI goal-oriented.
* **Format** ensures structured outputs that the backend can process easily.
* **Context** keeps the AI focused on the uploaded PDF, avoiding hallucinations.

This way, my backend can reliably use the AI’s responses for summaries, answers, or key points."

---

### 🟢 Outro (20s)

"So that’s how I designed my **System Prompt** and **User Prompt**, and how the **RTFC framework** guided me.

Thanks for watching – and if you’re building an AI project, try structuring your prompts with RTFC for more control and consistency."




## 🎤 **Video Script: Zero-Shot Prompting**

Hello everyone,

In this video, I’m going to explain what **Zero-Shot Prompting** is, how it works, and how I’ve implemented it in my backend project.

---

### **Introduction to Zero-Shot Prompting**

Let’s begin with the basics.

Zero-shot prompting is a technique in AI prompting where you give an instruction or a query to the AI **without providing any prior examples or demonstrations**.

Think of it like this: you are giving the AI only the task description, and the model has to figure out the answer on its own, based on its training knowledge.

For example, if I say:
*"Translate this English sentence into French: I love programming."*

The AI immediately gives me the correct French translation: *"J’aime programmer."*

Notice here, I didn’t give the AI any examples of English-to-French translations. That’s why it’s called **Zero-Shot**.

---

### **Why Zero-Shot is Useful in My Project**

Now, let’s connect this to my backend project.

In my project, the backend uses **system prompts and user prompts** to guide the AI when interacting with uploaded PDFs.

The system prompt defines the **role of the AI**, the **task it has to perform**, and the **format in which it should respond**.

The user prompt, on the other hand, contains the **actual question or query** that the user asks about their PDF.

Here’s where **zero-shot prompting** comes into play.

Since I want the AI to **answer questions about the PDF content** without showing it any training examples each time, I rely on zero-shot prompting.

So, if the user uploads a PDF and asks:
*"What is the summary of page 5?"*

The AI uses the instructions from the system prompt and the user’s question to generate the answer—without me giving it sample questions or answers beforehand.

---

### **How I Implemented Zero-Shot Prompting in Code**

Let me walk you through the code part.

Inside my backend project, I created a file called **`zero_shot_prompt.py`**.

Here’s the code:

```python
system_prompt = """
Role: You are an AI PDF Expert Assistant.
Task: Help users understand and interact with their uploaded PDFs by answering questions strictly based on PDF content.
Format: Always respond in strict JSON format:
{
  "answer": "",
  "summary": "",
  "key_points": []
}
Context: The user uploads a PDF document. Your job is to extract meaning, summarize sections, and answer questions without using external knowledge.
"""

def create_user_prompt(question: str) -> str:
    return f"User Question: {question}"
```

Now, when a user asks a question, for example:
*"What is the conclusion of this research paper?"*

The backend combines the **system prompt** and the **user’s question**, and then sends it directly to the AI model.

Since I don’t provide any training examples or few-shot examples here, this is a **pure zero-shot prompt**.

---

### **Benefits of Zero-Shot Prompting in This Case**

There are a few clear benefits of using zero-shot prompting here:

1. **Simplicity** – I don’t need to prepare or hard-code training examples.
2. **Flexibility** – The user can ask any type of question about the PDF, and the AI can handle it.
3. **Lightweight** – It reduces overhead because I’m not constantly passing examples with every query.

---

### **Conclusion**

So, to summarize:

* **Zero-shot prompting** means giving the AI only instructions, without examples.
* In my backend project, I’ve used it by combining a **system prompt** and a **user prompt** to guide the AI in answering PDF-related queries.
* This makes my system flexible, simple, and efficient.

That’s how I’ve implemented **Zero-Shot Prompting** in my project.

Thank you for watching!



# 🎥 Video Script: One-Shot Prompting

---

### **Intro (Hook + Context)**

“Hey everyone! In this video, I’ll be walking you through **One-Shot Prompting** — an important prompting technique we use in our AI-powered PDF Assistant project.

You’ve already seen **Zero-Shot Prompting**, where we give the model just the instructions and expect it to perform the task without any prior examples.

But sometimes, that’s not enough. The model might misunderstand what we want.

That’s where **One-Shot Prompting** comes in. We provide the model with **one clear example** of the input and the output we expect, so it learns the format and context before answering the actual user query.”

---

### **Explanation of One-Shot Prompting**

“Let’s break it down:

* In **Zero-Shot Prompting**, we said:
  ‘Here’s the role, here’s the task, now answer this question.’

* In **One-Shot Prompting**, we add an **example interaction** — something like:
  ‘Here’s a sample question a user might ask, and here’s the type of answer you should return.’

This example acts as a **guide** for the model. It’s like showing it a solved problem before asking it to solve a new one.”

---

### **Code Walkthrough**

“Now let me show you the code for One-Shot Prompting inside our backend.”

```python
# backend/prompts/one_shot_prompt.py

system_prompt = """
Role: You are an AI PDF Expert Assistant.
Task: Help users understand and interact with their uploaded PDFs by answering questions strictly based on PDF content.
Format: Always respond in strict JSON format:
{
  "answer": "",
  "summary": "",
  "key_points": []
}
Context: The user uploads a PDF document. Your job is to extract meaning, summarize sections, and answer questions without using external knowledge.
Example:
User Question: What is the abstract about?
Response:
{
  "answer": "The abstract discusses the impact of climate change on polar bear habitats.",
  "summary": "The abstract explains how rising temperatures reduce sea ice, making it harder for polar bears to hunt.",
  "key_points": [
    "Focus on polar bear survival",
    "Rising temperatures",
    "Loss of sea ice"
  ]
}
"""

def create_user_prompt(question: str) -> str:
    return f"User Question: {question}"
```

---

### **Narration while showing code**

“In this code, we do three things:

1. **System Prompt**: Defines the AI’s role, task, and response format — exactly like we did in zero-shot.

2. **Example**: But this time, we added a worked-out example of a user question and the correct JSON response. This is the ‘one-shot’ part — one demonstration for the AI to follow.

3. **User Prompt Function**: Finally, when the user asks their real question, the function appends it to the system prompt, and the AI already knows what kind of response to generate.”

---

### **Why This Works (RTFC Framework)**

“Now let’s connect this to the **RTFC framework**:

* **R – Role**: We clearly set the role as an ‘AI PDF Expert Assistant.’
* **T – Task**: The AI’s task is to summarize and answer strictly from the PDF.
* **F – Format**: We enforce JSON format for structured, consistent output.
* **C – Context**: We provide not only the PDF but also **one example**, which acts as extra context to guide the model.

So One-Shot Prompting combines RTFC with an illustrative example — making responses more reliable and closer to what we want.”

---

### **Wrap-Up**

“To summarize:

* **Zero-Shot** = Instructions only.
* **One-Shot** = Instructions + one example.
* This helps the AI understand both **what** to do and **how** to do it.


✅ End of Script


# 🎙️ Video Script: Multi-Shot Prompting

---

## **Introduction**

"Hi everyone, in this video, I’m going to explain **Multi-Shot Prompting**, how it works, and how I’ve implemented it in my project.

We’ve already seen **Zero-Shot Prompting**, where we provide the model with only a task description and no examples.

Then we looked at **One-Shot Prompting**, where we added a single example to guide the model.

Now, we move to the next step, which is **Multi-Shot Prompting**, where we provide multiple examples to the model so it can learn the expected pattern more clearly and generate consistent outputs."

---

## **What is Multi-Shot Prompting?**

"Multi-Shot Prompting means that instead of giving the model just one example, we provide several examples of inputs and outputs.

This way, the model doesn’t just rely on instructions—it has multiple reference points for how to respond.

Think of it as training by demonstration. The more examples we provide, the more consistent and accurate the output becomes."

---

## **Why Use Multi-Shot Prompting?**

"There are a few reasons why Multi-Shot Prompting is useful:

1. It **reduces ambiguity**. With multiple examples, the model clearly understands the pattern.
2. It **increases reliability**, especially for structured outputs like JSON.
3. It is very effective for **domain-specific tasks** where consistency is critical.

For example, in my project where the AI assistant extracts and explains content from PDFs, using multiple examples ensures that the output always follows the strict JSON format I’ve defined."

---

## **Code Implementation**

"Now let’s look at the code I used for Multi-Shot Prompting.

In my backend, I created a Python file for handling prompts. Inside it, I defined a function for **multi-shot prompting**.

Here’s the structure of the code:"

```python
from openai import OpenAI

client = OpenAI()

# Multi-Shot Prompt with multiple examples
multi_shot_prompt = """
Role: You are an AI PDF Expert Assistant.
Task: Help users understand and interact with their uploaded PDFs by answering questions strictly based on PDF content.
Format: Always respond in strict JSON format:
{
  "answer": "",
  "summary": "",
  "key_points": []
}

Here are some examples:

Example 1:
User Question: What is the title of the PDF?
Response:
{
  "answer": "The title of the PDF is 'Climate Change Report 2025'.",
  "summary": "The PDF discusses the impacts of climate change.",
  "key_points": ["Climate change", "Environmental impacts", "2025 report"]
}

Example 2:
User Question: Summarize the second chapter.
Response:
{
  "answer": "Chapter 2 provides an overview of renewable energy adoption.",
  "summary": "It explains solar, wind, and hydro energy trends.",
  "key_points": ["Renewable energy", "Solar", "Wind", "Hydro"]
}

Now here is the real user query:
User Question: {question}
"""

def multi_shot_prompting(question):
    prompt = multi_shot_prompt.format(question=question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    return response.choices[0].message["content"]


# Example usage
user_question = "What does Chapter 3 explain?"
print(multi_shot_prompting(user_question))
```

---

## **Explanation of the Code**

"Let me break this down step by step:

1. First, I defined the **role** of the assistant as a PDF Expert that answers questions based only on PDF content.
2. Then, I specified the **output format** in strict JSON, so the model always follows the same structure.
3. After that, I added **multiple examples**—one about the title of the PDF and another about summarizing a chapter.
4. Finally, I left space for the **real user query**, which gets inserted dynamically at runtime.

When the function runs, the AI model looks at both examples, identifies the pattern, and produces a consistent JSON response for the new question."

---

## **Why Multi-Shot Works Well in My Project**

"In my project, users might ask very different kinds of questions about their PDFs—like the title, summaries, key points, or explanations.

If I only used zero-shot or one-shot prompting, the responses might be inconsistent.

But with **multi-shot prompting**, the model sees multiple structured examples and learns that it must always:

* Provide a direct answer,
* Include a summary, and
* List key points.

This ensures **accuracy and uniformity** across all responses, which is critical for building a reliable assistant."

---

## **Conclusion**

"So to summarize:

* **Zero-Shot Prompting** → No examples, just instructions.
* **One-Shot Prompting** → One example, plus instructions.
* **Multi-Shot Prompting** → Multiple examples, plus instructions, which ensures consistency and better performance.

In my project, Multi-Shot Prompting helps the assistant always respond in the strict JSON format and stay reliable when handling different types of PDF-related queries.

That’s how I’ve used Multi-Shot Prompting in my backend implementation."

