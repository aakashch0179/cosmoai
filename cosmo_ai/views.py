from django.http import HttpResponse
from django.template import loader
import numpy as np
# import pandas as pd
from rest_framework.views import APIView
# from rest_framework.response import Response

from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import comparisons, response_selection
from chatterbot.filters import get_recent_repeated_responses
# from transformers import AutoModelForCausalLM, AutoTokenizer
import re
import json
from datetime import datetime
from cosmo_ai.tasks import *
from django.http import JsonResponse


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
# print("Initialising done!")

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

chatbot = ChatBot(
            'Cosmo',
            filters=[get_recent_repeated_responses],
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                # 'chatterbot.logic.TimeLogicAdapter',
                'chatterbot.logic.BestMatch',
                {
                    'import_path':'chatterbot.logic.BestMatch',
                    "statement_comparison_function": comparisons.LevenshteinDistance,
                    "response_selection_method": response_selection.get_first_response,
                    'default_response':'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold':0.90
                }
            ],
            database_uri='sqlite:///database.sqlite3'
        )


# f = open('Data/log.txt', 'r').read().splitlines() 

# train_data = []

# for line in f:
#     m = re.search('(You : |Cosmo : )?(.+)', line)
#     if m:
#         train_data.append(m.groups()[1])
# trainer = ListTrainer(chatbot)
# trainer.train(train_data)


# trainercorpus = ChatterBotCorpusTrainer(chatbot)
# trainercorpus.train("chatterbot.corpus.english")


def remember(input):
        msg = input.replace("remember that", "")
        def write_file(data):
            with open("Data/base.json", "w") as f:
                json.dump(data, f, indent=4)
            
        with open('Data/base.json') as file:
            data = json.load(file)
            newrec = data["rem"]
            record = {
                "msg": msg,
                "time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
            newrec.append(record)
            
        write_file(data)
        return msg



def del_rem(num):
    new_data = []
    with open('Data/base.json') as file:
        data = json.load(file)
        rec = data["rem"]
    i=1 
    for entry in rec:
        if i == int(num):
            pass
            i+=1
        else:
            new_data.append(entry)
            i+=1
            
    with open('Data/base.json', 'w') as file:
        json.dump(new_data, file, indent=4)
        
def main(query):
    
    FileLog = open("Data/log.txt", "r")
    chat_log = FileLog.read()
    FileLog.close()
    # logdata = f'{chat_log} You : {query}\nCosmo : '
    #  new_user_input_ids = tokenizer.encode(command + tokenizer.eos_token, return_tensors='pt')
    #     bot_input_ids = torch.cat([new_user_input_ids], dim=-1)
    #     chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    #     response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
       
       
    response = chatbot.get_response(query)
    chat_log_template_update = chat_log + f"\nYou : {query} \nCosmo : {response}"
    FileLog = open("Data/log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return response
    


class WeightPrediction(APIView):
    def post(self, request):
    
        # data = request.data
        # query = data['text']
        data = json.loads(request.body.decode("utf-8"))
        query = data['text']
        print(f"Query: {query}")
        query = str(query).lower()
        if "remember that" in query:
            print(f"Cosmo : Ok, I will remember that {remember(query)}")
        if "what do you remember" in query:
            with open("Data/base.json") as file:
                num = 1
                data = json.load(file)
                for i in data["rem"]:
                    print(f"Cosmo : {num}. {i['msg']} at {i['time']}")
                    num+=1
        if "forget everything" in query:
            with open("Data/base.json") as file:
                data = json.load(file)
                data["rem"] = []
                with open("Data/remember.json", "w") as f:
                    json.dump(data, f, indent=4)
                print("Cosmo : Ok, I have forgotten everything")
        if "forget" in query:
            selecnum = input("Cosmo : Which number do you want me to forget? ")
            del_rem(selecnum)
            print(f"Cosmo : Ok, I have forgotten point {selecnum}")
        if "create a goal" in query:
            goal = create_goal()
            with open("Data/goals.json") as file:
                data = json.load(file)
                newrec = data["goals"]
                record = {
                    "gname": goal["gname"],
                    "time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "status": "incomplete",
                    "priority": "high",
                    "notes": "  learn python",
                    "gdline": "24/11/2022 00:26:20",
                    "gtinvest": "2 hours",
                }
                newrec.append(record)
                with open("Data/goals.json", "w") as f:
                    json.dump(data, f, indent=4)
                print(f"Cosmo : Ok, I have created the goal {goal}")
        else:
            response = main(query)
            print("Cosmo : ", response)
            return JsonResponse({
            # 'uuid': result.uuid,
            'messages': response
     })
                


    
 