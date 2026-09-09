"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - AI Engineer Industrial Training Kit (Batch 2026)

A deterministic chatbot that responds via:
  1. Exact-match dictionary lookup using .get() (atomic + fallback)
  2. Whole-word keyword rules for broader intent matching
  3. Default fallback for completely unknown inputs

Pure control flow + hash-map logic — no machine learning involved.
"""

from typing import Optional

BOT_NAME: str = "PikaBot"  # Customise bot's name here

# --- Exact-match knowledge base (9 intents) ---
responses: dict[str, str] = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "hey": "Hey! What's up?",
    "how are you": "I'm just a program, but I'm running smoothly! How about you?",
    "what is your name": f"I'm {BOT_NAME}, a rule-based chatbot built for DecodeLabs Project 1.",
    "who are you": f"I'm {BOT_NAME}, your friendly rule-based assistant.",
    "help": "You can greet me, ask how I am, ask my name, or type 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

# --- Keyword-based fallback rules (checked only after exact match fails) ---
# Each tuple: (set of trigger keywords, reply)
keyword_rules: list[tuple[set[str], str]] = [
    ({"weather", "forecast", "rain", "sunny"},
     "I can't check the weather yet — I'm rule-based, not connected to the internet!"),
    ({"python", "code", "coding", "programming", "script"},
     "I love talking about code! What are you working on?"),
    ({"joke", "funny", "laugh", "humor"},
     "Why do programmers prefer dark mode? Because light attracts bugs!"),
]

# Exit commands — typing any of these ends the session
exit_commands: set[str] = {"bye", "exit", "quit", "goodbye", "see you"}


def get_response(user_input: str) -> str:
    """
    Generate a reply using three-tier logic:
      1. Exact match from dictionary (.get() with fallback to None)
      2. Whole-word keyword match from rules
      3. Default fallback if nothing matches
    """
    # --- Tier 1: Exact match (professional .get() approach) ---
    reply = responses.get(user_input)  # returns None if not found
    if reply is not None:
        return reply

    # --- Tier 2: Whole-word keyword matching ---
    # Split input into a set of individual words for precise intersection
    input_words = set(user_input.split())
    for keywords, rule_reply in keyword_rules:
        if keywords & input_words:  # set intersection — any keyword present?
            return rule_reply

    # --- Tier 3: Default fallback ---
    return "I do not understand. Type 'help' to see what I can do."


def run_chatbot() -> None:
    """Start the interactive chatbot session."""
    print(f"{BOT_NAME}: Hello! Type 'bye' to exit anytime.")

    while True:
        try:
            raw_input_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            # Graceful shutdown on Ctrl+D or Ctrl+C
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        # Sanitisation: strip whitespace and convert to lowercase
        clean_input = raw_input_text.strip().lower()

        # Skip empty lines
        if not clean_input:
            continue

        # Exit strategy
        if clean_input in exit_commands:
            print(f"{BOT_NAME}: Goodbye!")
            break

        # Get and display the response
        reply = get_response(clean_input)
        print(f"{BOT_NAME}: {reply}")


if __name__ == "__main__":
    run_chatbot()