// Return a bot response string based on the user message.
function getBotResponse(message) {
    console.log("Received message:", message);
    const normalized = normalizeMessage(message);
    console.log("Normalized message:", normalized);

    if (!normalized) {
        return "Please type a message so I can help you.";
    }

    // Greeting responses for Hi / Hii / Hello / Hey / Good morning / Good evening.
    if (isGreeting(normalized)) {
        return "Hello! 👋 I am your AI assistant. How can I help you today?";
    }

    // Dynamic date response using JavaScript Date.
    if (isDateQuestion(normalized)) {
        return getDateResponse();
    }

    // Dynamic time response using JavaScript Date.
    if (isTimeQuestion(normalized)) {
        console.log("Matched time question");
        return getTimeResponse();
    }

    // Basic identity and capability questions.
    if (isWhoAreYou(normalized)) {
        return "I am an intelligent assistant built to answer questions, share contact information, and help you with simple tasks.";
    }

    if (isWhatCanYouDo(normalized)) {
        return "I can tell you the current date and time, share contact details, answer common questions, and help with your chatbot needs.";
    }

    // Help queries should point the user to supported commands.
    if (normalized.includes("help")) {
        return "Sure! Ask me about the date, time, contact information, available services, or just say hello.";
    }

    // Contact information queries.
    if (isContactQuestion(normalized)) {
        return getContactResponse();
    }

    // Support and service related queries.
    if (isServiceQuestion(normalized)) {
        return "We offer customer support, onboarding, training, and consulting services. Ask me for contact information if you want to get in touch.";
    }

    // Thank you responses.
    if (normalized.includes("thank") || normalized.includes("thanks")) {
        return "You’re welcome! I’m happy to help you anytime.";
    }

    // Goodbye response for polite exits.
    if (normalized.includes("bye") || normalized.includes("goodbye") || normalized.includes("see you")) {
        return "Goodbye! Feel free to come back if you have more questions.";
    }

    // Fallback for unknown messages.
    return "I don't know the answer to that yet. Try asking about the date, time, contact information, or available services.";
}

// Normalize the input by trimming whitespace and converting to lowercase.
function normalizeMessage(message) {
    return message.trim().toLowerCase();
}

// Detect simple greetings.
function isGreeting(text) {
    return /^(hi|hii|hello|hey|good morning|good evening)\b/.test(text) ||
        text.includes(" hello") ||
        text.includes(" hey") ||
        text.includes(" hi") ||
        text.includes(" hii") ||
        text.includes(" good morning") ||
        text.includes(" good evening");
}

// Detect questions related to the current date.
function isDateQuestion(text) {
    return /(what( is|'s)? the date|today|current date|date today|what day)/.test(text);
}

// Detect questions related to the current time.
function isTimeQuestion(text) {
    return /(what( is|'s)? the time|current time|time now|clock|can you tell me the time|tell me the time|what time is it)/.test(text);
}

// Detect identity questions.
function isWhoAreYou(text) {
    return /(who are you|what are you|about you|tell me about yourself)/.test(text);
}

// Detect capability questions.
function isWhatCanYouDo(text) {
    return /(what can you do|what do you do|your capabilities|can you do)/.test(text);
}

// Detect contact-related queries.
function isContactQuestion(text) {
    return /(contact|email|phone|reach you|call you|support)/.test(text);
}

// Detect service-related queries.
function isServiceQuestion(text) {
    return /(service|services|pricing|support|offer)/.test(text) && !isContactQuestion(text);
}

// Build a date response string.
function getDateResponse() {
    const today = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const formattedDate = today.toLocaleDateString(undefined, options);
    return `Today is ${formattedDate}.`;
}

// Build a time response string.
function getTimeResponse() {
    const now = new Date();
    const formattedTime = now.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit', hour12: true });
    return `The current time is ${formattedTime}.`;
}

// Returns the company contact details.
function getContactResponse() {
    const email = 'support@example.com';
    const phone = '+1-555-123-4567';
    return `You can contact us at ${email} or call us at ${phone}.`;
}
