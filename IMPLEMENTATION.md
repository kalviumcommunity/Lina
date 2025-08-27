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
