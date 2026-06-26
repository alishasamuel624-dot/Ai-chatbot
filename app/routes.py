from flask import Blueprint, jsonify, render_template, request, session

from app.chatbot import Chatbot

bp = Blueprint("main", __name__)
chatbot = Chatbot()


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not message.strip():
        return jsonify({"response": "Please enter a message."})

    response = chatbot.respond(message)
    session["history"] = chatbot.get_history()
    return jsonify({"response": response, "history": chatbot.get_history()})
