import random
import re

# Chatbot'un cevaplarını ve kurallarını içeren sözlük
responses = {
    r"merhaba|selam|hey|hi|hello": ["Merhaba! Nasıl yardımcı olabilirim?", "Selam! Size nasıl yardımcı olabilirim?"],
    r"nasılsın|naber": ["Teşekkürler, iyiyim siz nasılsınız?", "İyiyim, teşekkür ederim. Siz nasılsınız?"],
    r"teşekkürler|sağ ol|teşekkür ederim": ["Rica ederim!", "Ne demek, yardımcı olabildiysem ne mutlu bana."],
    r"üzerine|sonra|konuşuruz": ["Tabii, başka bir şey sorabilirsiniz veya görüşmek üzere!"],
    r"bye|güle güle|görüşürüz": ["Güle güle, başka zaman tekrar bekleriz!", "Görüşmek üzere!"],
    r"": ["Üzgünüm, anlamadım. Başka bir şey sormak ister misiniz?"]
}

def respond(message):
    """
    Kullanıcı mesajına uygun bir cevap döndürür.
    """
    for pattern, replies in responses.items():
        if re.match(pattern, message.lower()):
            return random.choice(replies)
    return random.choice(responses[r""])

if __name__ == "__main__":
    print("Chatbot: Merhaba! Benimle sohbet edebilirsiniz. Çıkmak için 'bye' yazın.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Güle güle!")
            break
        response = respond(user_input)
        print(f"Chatbot: {response}")

