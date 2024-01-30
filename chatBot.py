def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm good, thanks for asking!"

    elif "name of the training" in user_input:
        return "python programming for SoF students."
    
    elif "name of the school" in user_input:
        return "mirzapur girls high school."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I don't understand that. Can you please ask another question?"

# Simple interactive loop
while True:
    user_message = input("You: ")
    if user_message.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    bot_response = simple_chatbot(user_message)
    print("Chatbot:", bot_response)
