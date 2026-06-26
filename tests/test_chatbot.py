import unittest

from app.chatbot import Chatbot


class ChatbotTests(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_greeting_intent(self):
        response = self.chatbot.respond("Hello")
        self.assertIn("Hello", response)

    def test_help_intent(self):
        response = self.chatbot.respond("Can you help me?")
        self.assertIn("services", response.lower())

    def test_fallback_intent(self):
        response = self.chatbot.respond("random unknown input")
        self.assertIn("not sure", response.lower())


if __name__ == "__main__":
    unittest.main()
