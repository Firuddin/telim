import random
import re


responses = {
    r"(salam|hi|hello|hey|merhaba)": ["salam nece komek ede bilerem?"],
    r"(necesiz|naber)": ["tesekkurler!!! yaxsiyam siz necesiz?"],
    r"(tesekur|saqol)": ["size nece komek ede bilerem?"],
    r"(saqol|bye-bye|gorusuruz)": ["sende saqol"]
}


def respond (message):
    message=message.lower()
    for pattern,replies in responses.items():
        if re.search(pattern,message):
            return random.choice(replies)
    return "uzur isteyirem hecene anlamadm.Basqa birsey sorusmaq isteyirsen?"


if __name__ == "__main__":
    print("Chatbot: salam menimle sohbet ede bilersiniz.Cixmaq ucun ise 'bye' yazin ")
    while True:
        user_input=input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: gule-gule")
            break
        response=respond(user_input)
        print(f"Chatbot: {response}")