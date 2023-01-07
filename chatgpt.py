import openai
from keys.open_api import API_KEY


openai.api_key = API_KEY


# load_dotenv()
completion = openai.Completion()


def ReplyBrain(question):
    FileLog = open("Data/chatgptlog.txt", "r")
    chat_log = FileLog.read()
    FileLog.close()

    # if chat_log is None:
    #     chat_log = chat_log_template

    prompt = f'{chat_log} You : {question}\nCosmo : '
    response = completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0
        )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log + f"\nYou : {question} \nCosmo : {answer}"
    FileLog = open("Data/chatgptlog.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer 


while True:
    kk = input("You : ")
    print("Cosmo : ", ReplyBrain(kk))
