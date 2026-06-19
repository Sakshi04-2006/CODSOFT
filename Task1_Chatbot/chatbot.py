import random


responses = {

"hello": [
    "Hello! How can I help you?",
    "Hi! Welcome to CODSOFT AI Assistant."
],


"how are you": [
    "I am doing great and ready to help you!"
],


"python": [
    "Python is a programming language used in AI, Machine Learning, web development and automation."
],


"java": [
    "Java is an object oriented programming language used for Android apps, web applications and software development."
],


"android": [
    "Android is a mobile operating system used in smartphones and tablets."
],


"ai": [
    "Artificial Intelligence is the field of creating machines that can perform tasks requiring human intelligence."
],


"machine learning": [
    "Machine Learning allows computers to learn patterns from data and make predictions."
],


"codsoft": [
    "CODSOFT provides internship opportunities for students to build technical projects."
],


"internship": [
    "The CODSOFT AI internship includes projects like chatbot, Tic Tac Toe AI, recommendation system and face detection."
],


"bye": [
    "Goodbye! Have a nice day."
]

}



def chatbot_response(message):

    message = message.lower()


    for key in responses:

        if key in message:

            return random.choice(responses[key])


    return (
        "I am still learning. "
        "Try asking about Python, Java, AI, Android, Machine Learning or CODSOFT."
    )



print("==============================")
print(" CODSOFT AI Assistant")
print(" Type exit to stop")
print("==============================")


while True:

    user = input("\nYou: ")


    if user.lower()=="exit":

        print("Bot: Goodbye!")
        break


    print(
        "Bot:",
        chatbot_response(user)
    )