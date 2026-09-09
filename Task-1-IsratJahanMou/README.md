# 🤖 Rule-Based AI Chatbot — Project 1

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![DecodeLabs](https://img.shields.io/badge/DecodeLabs-Batch%202026-orange)](https://decodelabs.tech)

A deterministic, rule‑based chatbot built in pure Python as **Project 1** of the DecodeLabs **AI Engineer Industrial Training Kit** (Batch 2026).  

> *“Before you build systems that learn on their own, master the art of teaching a machine through explicit if‑else instructions.”*  
> — DecodeLabs Project Brief

This chatbot demonstrates **control flow**, **hash‑map lookups**, and **deterministic decision‑making** — the foundational skills every AI engineer must master before moving to probabilistic models.

---

## 📌 Features

- **Continuous conversation loop** – runs until an exit command is given.
- **Input sanitisation** – normalises case and whitespace so `Hello`, `HELLO`, and `  hello ` all match the same intent.
- **9 exact‑match intents** – handles greetings, identity questions, thanks, and help.
- **Keyword‑based fallback** – if no exact match, it checks for whole‑word keywords (e.g., `"python"`, `"joke"`, `"weather"`) to give context‑aware replies.
- **Default fallback** – a polite “I do not understand” response for completely unrecognised input.
- **Clean exit** – recognises multiple exit words (`bye`, `exit`, `quit`, `goodbye`, `see you`) and also exits gracefully on `Ctrl+C` / `Ctrl+D`.
- **Robust empty‑input handling** – pressing Enter with no text is simply ignored.
- **White‑box traceability** – every response is fully deterministic and auditable, with zero hallucination risk.

---

## 🏗️ Architecture & Design Philosophy

The bot follows the classic **IPO (Input‑Process‑Output)** model:

1. **Input** – raw user text.
2. **Process** – sanitise, then apply a three‑tier logic pipeline:
   - **Tier 1 (Exact match)** – O(1) lookup using a Python dictionary (hash map). This is the preferred approach over a long `if-elif` ladder, as highlighted in the project guidelines.
   - **Tier 2 (Keyword rules)** – if no exact match, we split the input into a set of words and check for intersection with pre‑defined keyword sets (whole‑word matching, avoiding accidental substring triggers).
   - **Tier 3 (Default)** – a generic fallback reply.
3. **Output** – the chosen reply is printed, and the loop repeats.

> 💡 **Why this matters:**  
> This architecture implements a **deterministic “white box”** – every decision path is transparent and predictable. It serves as a **guardrail** for future probabilistic systems (like LLMs), ensuring safety and compliance in critical domains (finance, healthcare, etc.).

---

## 📦 Requirements

- **Python 3.7** or higher  
- No external dependencies – only the standard library is used.

---

## 🚀 Installation & Usage

1. **Clone or download** this repository.
2. **Navigate** to the project folder.
3. **Run** the chatbot:

```bash
python chatbot.py
```

4. **Interact** with the bot by typing your messages. Type `bye` (or any exit command) to end the session.

---

## 🧩 Code Structure

```
.
├── chatbot.py          # Main script containing all logic
└── README.md           # This file
```

### Key Components in `chatbot.py`

| Component                | Description                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------|
| `responses`              | Dictionary mapping exact‑match phrases to replies (9 intents).                                     |
| `keyword_rules`          | List of `(set_of_keywords, reply)` tuples – used when no exact match is found.                     |
| `exit_commands`          | Set of words that trigger a clean exit.                                                            |
| `get_response()`         | Core decision function – implements the three‑tier logic.                                          |
| `run_chatbot()`          | Manages the main loop, input sanitisation, and error handling (EOF/KeyboardInterrupt).             |
| `if __name__ == "__main__"` | Entry point that starts the bot.                                                                |

---

## 🔧 Extending the Bot

The modular design makes it easy to add new capabilities:

- **Add a new exact‑match intent** – simply add a new key‑value pair to the `responses` dictionary:
  ```python
  "good morning": "Good morning! How can I assist you?"
  ```

- **Add a new keyword rule** – append a tuple `(set_of_keywords, reply)` to `keyword_rules`:
  ```python
  ({"coffee", "tea", "drink"}, "I'm not a barista, but I can help with code!")
  ```

- **Add a new exit word** – add it to the `exit_commands` set:
  ```python
  exit_commands.add("stop")
  ```

- **Change the bot’s personality** – simply rewrite the reply strings or the `BOT_NAME` constant.

---

## 💬 Example Conversation

```
PikaBot: Hello! Type 'bye' to exit anytime.
You: Hello
PikaBot: Hi there! How can I help you today?
You: Tell me a joke
PikaBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: What is your name?
PikaBot: I'm PikaBot, a rule-based chatbot built for DecodeLabs Project 1.
You: how are you
PikaBot: I'm just a program, but I'm running smoothly! How about you?
You: I'm fine, thanks
PikaBot: You're welcome!
You: what's the weather like?
PikaBot: I can't check the weather yet — I'm rule-based, not connected to the internet!
You: bye
PikaBot: Goodbye!
```

---

## 📚 Why This Approach?

This project is not just a chatbot – it’s a **demonstration of core AI engineering principles**:

- **Deterministic over probabilistic** – every output is hard‑coded, making it safe, explainable, and auditable.
- **Hash maps over linear scans** – using dictionaries gives O(1) average lookup, avoiding the technical debt of long `if-elif` chains.
- **Single atomic lookup** – the `.get()` method combines retrieval and fallback in one operation, as recommended in the course material.
- **Hybrid architecture** – exact matches provide precision; keyword rules add flexibility; fallback ensures graceful degradation.

This foundation prepares you to later build **guardrails** for generative AI systems, ensuring they stay within safe, compliant boundaries.

---

## 🏁 Future Improvements

- **Synonym / stem matching** – use a simple stemmer or synonym dictionary to broaden coverage.
- **Conversation memory** – store the last few messages to handle context (e.g., follow‑up questions).
- **External API integration** – add real‑time data (weather, news) while keeping the core deterministic.
- **GUI / Web interface** – wrap the bot in a graphical or web front‑end.

---

## 👩‍💻 Author

**Israt Jahan Mou**  
B.Sc. in CSE, University of Asia Pacific  
DecodeLabs AI Engineer Industrial Training Kit — Batch 2026

---

## 🙏 Acknowledgements

- DecodeLabs for the comprehensive training material and project structure.
- The open‑source Python community for the tools and inspiration.

---

## 📄 License

This project is provided for educational purposes under the [MIT License](https://opensource.org/licenses/MIT).
```
