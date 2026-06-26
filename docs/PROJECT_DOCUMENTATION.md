# Project Documentation

## Overview
This project is a beginner-friendly AI chatbot built with Python and Flask.

## Architecture
- Frontend: HTML + CSS + JavaScript
- Backend: Flask
- Logic: Python class for intent matching
- Data: JSON file with predefined intents

## How it works
1. The user sends a message from the browser.
2. Flask receives the message.
3. The chatbot matches the message to the best intent.
4. A response is returned and shown in the chat UI.

## Files
- app/chatbot.py: chat logic and intent matching
- app/routes.py: web routes
- app/intents.json: chatbot intents and responses
- app/templates/index.html: chat UI
- app/static/style.css: styling
