# AI Chatbot Project

A beginner-friendly AI chatbot built with Python, Flask, and JSON-based intents.

## Project structure

- app/ - main application package
  - chatbot.py - chatbot logic and intent matching
  - routes.py - Flask routes
  - intents.json - predefined intents and responses
  - templates/ - HTML templates for the chat UI
  - static/ - CSS styles
- docs/ - project documentation
- tests/ - automated tests
- app.py - app entry point
- run.py - alternate startup script

## How to run

1. Activate the virtual environment
2. Run the app with:
   - python app.py
   - or python run.py

## Features

- predefined intents
- simple NLP-style matching
- context-aware responses
- conversation history
- basic web interface

## Open the chatbot

After starting the app, open one of these links in your browser:

- http://127.0.0.1:5000/
- http://localhost:5000/

## Deploy on Render

1. Push this project to GitHub.
2. Create a new Web Service on Render.a
3. Connect the GitHub repository.
4. Use these settings:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn wsgi:app
5. Deploy the service.

Render will then host your chatbot at a public URL.

## Deploy on Vercel

Vercel can host this app as a serverless Python function.

1. Push the project to GitHub.
2. Open Vercel and create a new project.
3. Import the GitHub repository.
4. Set the framework to Python or use the default.
5. Use these settings:
   - Build Command: pip install -r requirements.txt
   - Output Directory: .
6. Add a file named vercel.json with the Python runtime config.
7. Deploy.

Vercel will give you a public URL for the chatbot.
