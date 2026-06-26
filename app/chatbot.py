import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    HAS_NLTK = True
except Exception:
    HAS_NLTK = False
    word_tokenize = None
    stopwords = None


class Chatbot:
    def __init__(self, intents_path: str | None = None):
        self.intents_path = Path(intents_path or Path(__file__).with_name("intents.json"))
        self.intents = self._load_intents()
        self.intents_by_tag = {item["tag"]: item for item in self.intents}
        self.context: Dict[str, str | None] = {"last_intent": None, "last_topic": None}
        self.history: List[Dict[str, str]] = []

    def _load_intents(self) -> List[Dict[str, object]]:
        with self.intents_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        return data.get("intents", [])

    def preprocess_text(self, message: str) -> List[str]:
        message = message.lower()
        message = re.sub(r"[^a-z0-9\s]", " ", message)

        if HAS_NLTK and word_tokenize is not None:
            try:
                tokens = word_tokenize(message)
            except LookupError:
                tokens = re.findall(r"[a-z0-9]+", message)
        else:
            tokens = re.findall(r"[a-z0-9]+", message)

        if HAS_NLTK and stopwords is not None:
            try:
                stop_words = set(stopwords.words("english"))
                tokens = [token for token in tokens if token not in stop_words]
            except LookupError:
                pass

        return tokens

    def match_intent(self, message: str) -> Tuple[str, Dict[str, object]]:
        tokens = set(self.preprocess_text(message))
        best_tag = "fallback"
        best_intent = self.intents_by_tag[best_tag]
        best_score = 0

        for intent in self.intents:
            tag = intent["tag"]
            patterns = intent.get("patterns", [])
            score = 0

            for pattern in patterns:
                pattern_text = pattern.lower()
                if pattern_text in message.lower():
                    score += 8
                pattern_tokens = set(self.preprocess_text(pattern))
                score += len(pattern_tokens & tokens)

            if self.context.get("last_intent") and tag == self.context["last_intent"] and any(
                word in message.lower() for word in ["more", "tell", "continue", "about"]
            ):
                score += 4

            if score > best_score:
                best_score = score
                best_tag = tag
                best_intent = intent

        if best_score < 2:
            return "fallback", self.intents_by_tag["fallback"]

        return best_tag, best_intent

    def respond(self, message: str) -> str:
        tag, intent = self.match_intent(message)
        response = self._build_response(tag, intent, message)
        self.history.append({"user": message, "bot": response})
        self.context["last_intent"] = tag
        self.context["last_topic"] = intent.get("topic")
        return response

    def _build_response(self, tag: str, intent: Dict[str, object], message: str) -> str:
        if tag == "fallback":
            return "I am not sure how to help with that yet. Try asking about services, pricing, hours, or contact information."

        if tag == "greeting":
            return "Hello! I am your AI assistant. How can I help you today?"

        if tag == "goodbye":
            return "Goodbye! Feel free to come back if you need more help."

        if tag == "help":
            return "You can ask me about services, pricing, hours, contact details, or say hello."

        if tag == "thanks":
            return "You are welcome! I am happy to help."

        if tag == "about":
            return "I am a simple AI chatbot built with Python, Flask, and JSON-based intents."

        if tag == "services" and self.context.get("last_intent") == "services":
            return "We provide onboarding, support, and training services."

        if tag == "pricing" and self.context.get("last_intent") == "pricing":
            return "Our pricing has a basic plan, a professional plan, and an enterprise plan."

        if tag == "hours" and self.context.get("last_intent") == "hours":
            return "We are available Monday through Friday from 9 AM to 6 PM."

        if tag == "contact" and self.context.get("last_intent") == "contact":
            return "You can reach us by email at support@example.com."

        responses = intent.get("responses", [])
        if isinstance(responses, list) and responses:
            return responses[0]
        return "I can help with that."

    def get_history(self) -> List[Dict[str, str]]:
        return self.history

    def clear_history(self) -> None:
        self.history.clear()
