import random
import time

moods = {
    "happy": [
        "That's awesome to hear!",
        "Keep smiling, life is good!",
        "Happiness looks good on you!"
    ],
    "sad": [
        "It's okay to feel this way.",
        "Tough times don’t last.",
        "I'm here for you."
    ],
    "angry": [
        "Take a deep breath.",
        "Calm minds make better decisions.",
        "Let it go, it's not worth it."
    ],
    "confused": [
        "Let's figure it out together.",
        "Take it step by step.",
        "Clarity comes with patience."
    ],
    "default": [
        "Interesting...",
        "Tell me more.",
        "I see."
    ]
}

def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ["happy", "joy", "great", "good"]):
        return "happy"
    elif any(word in text for word in ["sad", "down", "bad", "upset"]):
        return "sad"
    elif any(word in text for word in ["angry", "mad", "furious"]):
        return "angry"
    elif any(word in text for word in ["confused", "lost", "don't know"]):
        return "confused"
    else:
        return "default"

def ai_response():
    print("AI: Hello! Tell me how you're feeling (type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("AI: Goodbye! Take care.")
            break
        
        mood = detect_mood(user_input)
        response = random.choice(moods[mood])
        
        time.sleep(1)
        print("AI:", response)

ai_response()