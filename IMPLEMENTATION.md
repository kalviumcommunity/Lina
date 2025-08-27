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
