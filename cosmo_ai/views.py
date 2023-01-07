from django.http import HttpResponse
from django.template import loader
import numpy as np
# import pandas as pd
from rest_framework.views import APIView
# from rest_framework.response import Response
import openai
import re
import json
from datetime import datetime
from cosmo_ai.tasks import *
from django.http import JsonResponse
from keys.open_api import API_KEY


openai.api_key = API_KEY

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# load_dotenv()
completion = openai.Completion()

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
        

def ReplyBrain(question):
    FileLog = open("Data/chatgptlog.txt", "r")
    chat_log = FileLog.read()
    FileLog.close()

    # if chat_log is None:
    #     chat_log = chat_log_template

    # prompt = f'{chat_log} You : {question}\nCosmo : '
    response = completion.create(
        model = "text-davinci-003",
        prompt = question,
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
    
    


class CosmoAi(APIView):
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
            response = ReplyBrain(query)
            print("Cosmo : ", response)
            return JsonResponse({
            # 'uuid': result.uuid,
            'messages': response
     })
                


    
 