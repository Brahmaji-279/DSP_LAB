from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
CORPUS_FILE = "/home/brahmajikavya/Downloads/chat.txt"
chatbot = ChatBot("Chatbot")
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
for i in range(len(cleaned_corpus) - 1):
    trainer.train([
        cleaned_corpus[i],
        cleaned_corpus[i + 1]
    ])
exit_conditions = ("bye")
while True:
    query = input("> ").strip().lower()
    if query in exit_conditions:
        print("👋 Goodbye!")
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
