from django.http import HttpResponse
from django.template import loader
import numpy as np
# import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
# import openai
# import re
import random
import json
from datetime import datetime
from cosmo_ai.tasks import *
from django.http import JsonResponse
from cosmo_ai.godel import generate
# from keys.open_api import API_KEY
from cosmo_ai.neural.executequery import ExecuteQuery
from cosmo_ai.neural.getvalues import getValues
# from googletrans import Translator


# openai.api_key = API_KEY

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# load_dotenv()
# completion = openai.Completion()

# def remember(input):
#         msg = input.replace("remember", "")
#         def write_file(data):
#             with open("Data/base.json", "w") as f:
#                 json.dump(data, f, indent=4)
            
#         with open('Data/base.json') as file:
#             data = json.load(file)
#             newrec = data["rem"]
#             record = {
#                 "msg": msg,
#                 "time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#             }
#             newrec.append(record)
            
#         write_file(data)
#         return msg

# def del_rem(num):
#     new_data = []
#     with open('Data/base.json') as file:
#         data = json.load(file)
#         rec = data["rem"]
#     i=1 
#     for entry in rec:
#         if i == int(num):
#             pass
#             i+=1
#         else:
#             new_data.append(entry)
#             i+=1
            
#     with open('Data/base.json', 'w') as file:
#         json.dump(new_data, file, indent=4)
        
# def ReplyBrain(question):
#     FileLog = open("Data/chatgptlog.txt", "r")
#     chat_log = FileLog.read()
#     FileLog.close()

#     # if chat_log is None:
#     #     chat_log = chat_log_template

#     # prompt = f'{chat_log} You : {question}\nCosmo : '
#     response = completion.create(
#         model = "text-davinci-003",
#         prompt = question,
#         temperature = 0.5,
#         max_tokens = 60,
#         top_p = 0.3,
#         frequency_penalty = 0.5,
#         presence_penalty = 0
#         )
#     answer = response.choices[0].text.strip()
#     chat_log_template_update = chat_log + f"\nYou : {question} \nCosmo : {answer}"
#     FileLog = open("Data/chatgptlog.txt", "w")
#     FileLog.write(chat_log_template_update)
#     FileLog.close()
#     return answer 
    
# # Translation
# def TranslationHinToEng(Text):
#     line = str(Text)
#     translate = Translator()
#     result = translate.translate(line, dest='en')
#     data = result.text
#     return data   

# translator = Translator()

# def transl():
#     result = translator.translate("what is this written explain it", dest='hi')
#     print(result.text)



instruction = f'Instruction: given a dialog context and related knowledge, you need to empathically answer the question based on the knowledge.'
# knowledge = ''
know = open("cosmo_ai/Data/knowledge.txt", "r")
knowledge = know.read()




class CosmoAi(APIView):
    def post(self, request):
    
        # data = request.data
        # query = data['text']
        data = json.loads(request.body.decode("utf-8"))
        query = data['text']
        print(f"Query: {query}")
        # input(f"Query: {query}")
        dialoq = str(query).lower()
        # if "remember" in query:
        #     print(f"Cosmo : Ok, I will remember {remember(query)}")
        # if "what do you remember" in query:
        #     with open("Data/base.json") as file:
        #         num = 1
        #         data = json.load(file)
        #         for i in data["rem"]:
        #             print(f"Cosmo : {num}. {i['msg']} at {i['time']}")
        #             num+=1
        # if "forget everything" in query:
        #     with open("Data/base.json") as file:
        #         data = json.load(file)
        #         data["rem"] = []
        #         with open("Data/remember.json", "w") as f:
        #             json.dump(data, f, indent=4)
        #         print("Cosmo : Ok, who am I? lol")
        # if "forget" in query:
        #     selecnum = input("Cosmo : Which number do you want me to forget? ")
        #     del_rem(selecnum)
        #     print(f"Cosmo : Ok, I have forgotten point {selecnum}")
        # if "create a goal" in query:
        #     goal = create_goal()
        #     with open("Data/goals.json") as file:
        #         data = json.load(file)
        #         newrec = data["goals"]
        #         record = {
        #             "gname": goal["gname"],
        #             "time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        #             "status": "incomplete",
        #             "priority": "high",
        #             "notes": "  learn python",
        #             "gdline": "24/11/2022 00:26:20",
        #             "gtinvest": "2 hours",
        #         }
        #         newrec.append(record)
        #         with open("Data/goals.json", "w") as f:
        #             json.dump(data, f, indent=4)
        #         print(f"Cosmo : Ok, I have created the goal {goal}")
        # else:
        
        response = ExecuteQuery(dialoq)
        values = getValues(dialoq)
        # if values[4] is None:
        #     repeat = 'Once'
        # elif values[4] is 'daily':
        #     repeat = 'Daily'
        
        
        
        if response[1] == "create_reminder":
            # if values[4] == 'notime':
            #     return JsonResponse({
            #         'messages': 'At what time do you want me to remind you?',
            #     })
            # else:
            return JsonResponse({
                'messages': response[0],
                'action': response[1],
                'function': [{
                        'id': random.randint(1, 100000),
                        'sound': 'General',
                        'subTitle': 'Task',
                        'type': 'Note',
                        'title': values[0],
                        'description': '',
                        'time': values[1].upper(),
                        'timestamp' : datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f"),
                        'enable': False,
                        'report': [],
                        'icon': 'https://firebasestorage.googleapis.com/v0/b/cosmo-f5007.appspot.com/o/categories%2FIcons%2Ftaskicon.svg?alt=media&token=56f3fc55-8eda-4463-bceb-7bf3198dff3c',
                        'color': 'FFD700',
                        'sharedToMe': [],
                        'sharedByMe': [],
                        'repeat': 'Once',
                        'reminders': [{
                            'time': values[1].upper(),
                            'enable': False,
                            'repeat': 'Once',
                            'title': values[0],
                            'id': random.randint(1, 100000),
                            'note': '',
                            'dates': [],
                            }],
                    }]
            })
            
        elif response[1] == 'create_todo':
            return JsonResponse({
            'messages': response[0],
            'action': response[1],
            'function': [{
                'name': 'defaulttodo',
                'id': random.randint(1, 100000),
                'subTasks': [{
                    'task':values[0].replace("create a todo", ""),
                    'done': False
                }],
                'shared': [],
                'sharedByMe': [],
                    }],
            })
            
        elif response[1] == 'create_note':
            return JsonResponse({
            'messages': response[0],
            'action': response[1],
            'function': {
                'title': 'defaultnote',
                'id': random.randint(1, 100000),
                'type': 'Note',
                'description': values[0],
                'time': datetime.now().strftime("%d/%m/%Y"),
                'mainTime': datetime.now().strftime("%I:%M %p"),
                'complete': False,
                'shared': [],
                'sharedByMe': [],
                }
            })
            
        elif response[1] == 'show_people':
            return JsonResponse({
                'messages': response[0],
                'action': response[1]
            })
            
        elif response[1] == 'show_friends':
            return JsonResponse({
                'messages': response[0],
                'action': response[1]
            })
            
        elif response[1] == 'show_allgroups':
            return JsonResponse({
                'messages': response[0],
                'action': response[1]
            })
        elif response[1] == 'show_mygroups':
            return JsonResponse({
                'messages': response[0],
                'action': response[1]
            })  
        elif response[1] == 'show_allcommunities':
            return JsonResponse({
                'messages': response[0],
                'action': response[1]
            })
        elif response[1] == 'show_mycommunities':
            return JsonResponse({
                'messages': response[0],
                'action': response[1]
            }) 
        elif response[1] == 'name':
            return JsonResponse({
                'messages': response[0]
            })
            
        elif response[1] == 'greeting':
            return JsonResponse({
                'messages': response[0]
            })
            
        elif response[1] == 'commands':
            return JsonResponse({
                'messages': response[0]
            })
        elif response[1] == 'goodbye':
            return JsonResponse({
                'messages': response[0]
            })
        else: 
            return JsonResponse({
                'messages': generate(instruction, knowledge, dialoq)
            })
            
        
            
        
            
        
        
        
       
                



    
 