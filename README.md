# ChatBot M1

A simple terminal-based chatbot powered by the **Groq API** and Meta's **LLaMA 3.3 70B** model.

## Features

- Conversational AI in your terminal
- Powered by `llama-3.3-70b-versatile` via Groq
- Lightweight — no frameworks, just Python

## Requirements

```
groq
python-dotenv
```

Install with:

```bash
pip install groq python-dotenv
```

## Setup

1. Clone the repo
2. Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
3. Get your free API key at [console.groq.com](https://console.groq.com)

## Usage

```bash
python chatbotM1.py
```

Type your message and press Enter. Type `quit` or `bye` to exit.

## Example

```
You: What is machine learning?
Bot: Machine learning is a subset of AI that enables systems to learn from data...
```

---
