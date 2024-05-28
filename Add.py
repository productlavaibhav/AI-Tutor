def get_emotional_reply(response):
    # Expanded and organized keywords for various emotional states
    positive_keywords = ["good", "great", "well", "amazing", "happy", "excited", "joyful"]
    negative_keywords = ["bad", "not good", "terrible", "sad", "ill", "sick", "distracted", "upset", "depressed"]
    concern_keywords = ["ill", "sick", "sad", "depressed", "upset", "distracted"]  # Specific keywords for showing extra concern

    # Check for specific concern-related keywords to give a more thoughtful response
    for keyword in concern_keywords:
        if keyword in response.lower():
            return f"I'm sorry to hear you're feeling {keyword}. 😔 Math can be a good distraction. Let's try solving some problems together!"

    # Check for general negative emotions if no specific concern was detected
    for keyword in negative_keywords:
        if keyword in response.lower():
            return "Oh, it's sad to hear that. 😔 Maybe some math problems can help you feel better! Let’s try it!"

    # Check for positive emotions
    for keyword in positive_keywords:
        if keyword in response.lower():
            return "That's awesome! 😊 Let's dive into some math problems!"

    # Default response if no specific emotions are detected
    return "Okay, let's get started! 🚀"
