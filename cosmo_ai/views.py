from django.http import HttpResponse
from django.template import loader
import numpy as np
# import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
import openai
# import re
import random
import json
# from datetime import datetime
# from cosmo_ai.tasks import *
from django.http import JsonResponse
from cosmo_ai.keys.open_api import API_KEY
# from cosmo_ai.neural.executequery import ExecuteQuery
# from cosmo_ai.neural.getvalues import getValues
# from googletrans import Translator


openai.api_key = API_KEY

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# load_dotenv()
completion = openai.Completion()

def OpenBrain(question):
    FileLog = open("cosmo_ai/Data/chatgptlog.txt", "r")
    chat_log = FileLog.read()
    FileLog.close()

    # if chat_log is None:
    #     chat_log = chat_log_template

    # prompt = f'{chat_log} You : {question}\nCosmo : '
    response = completion.create(
        model = "text-babbage-001",
        prompt = question,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0
        )
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log + f"\nYou : {question} \nCosmo : {answer}"
    FileLog = open("cosmo_ai/Data/chatgptlog.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer 
    
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
    # print(result.text)



class CosmoAi(APIView):
    def post(self, request):
        
        raval = random.randint(1, 100000)
        idval = str(raval)
        
        data = json.loads(request.body.decode("utf-8"))
        query = data['text']
        coin = data['coin']
        # lang = data['lang']
        print(f"Query: {query}")
        dialoq = str(query).lower()
        # response = ExecuteQuery(dialoq)
        # trawmsg = translator.translate(response[0], dest= lang)
        # tranmsg = trawmsg.text
        # values = getValues(dialoq)
        # if values[4] is None:
        #     repeat = 'Once'
        # elif values[4] is 'daily':
        #     repeat = 'Daily'
        
        if coin >=1:
            return JsonResponse({
                'messages': OpenBrain(dialoq),
                'action': 'usecoin'
            })
        elif coin == 0: 
            return JsonResponse({
                'messages': 'You have reached your limit kindly recharge your account to continue or use free commands',
                'action': 'payment'
            })
            
        # if response[1] == 'opencosmo':
        #     print("something went wrong")
        #     return JsonResponse({
        #         'messages': OpenBrain(dialoq)
        #     })      
        # elif response[1] == "create_reminder":
        #     # if values[4] == 'notime':
        #     #     return JsonResponse({
        #     #         'messages': 'At what time do you want me to remind you?',
        #     #     })
        #     # else:
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1],
        #         'function': {
        #                 'id': idval,
        #                 'sound': 'General',
        #                 'subTitle': 'Task',
        #                 'type': 'Note',
        #                 'title': values[0],
        #                 'description': '',
        #                 'time': values[1].upper(),
        #                 'timestamp' : datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f"),
        #                 'enable': False,
        #                 'report': [],
        #                 'icon': 'https://firebasestorage.googleapis.com/v0/b/cosmo-f5007.appspot.com/o/categories%2FIcons%2Ftaskicon.svg?alt=media&token=56f3fc55-8eda-4463-bceb-7bf3198dff3c',
        #                 'color': 'FFD700',
        #                 'sharedToMe': [],
        #                 'sharedByMe': [],
        #                 'repeat': 'Once',
        #                 'reminders': [{
        #                     'time': values[1].upper(),
        #                     'enable': False,
        #                     'repeat': 'Once',
        #                     'title': values[0],
        #                     'id': idval,
        #                     'note': '',
        #                     'dates': [],
        #                     }],
        #             }
        #     })
            
        # elif response[1] == 'create_todo':
        #     return JsonResponse({
        #     'messages': response[0],
        #     'action': response[1],
        #     'function': {
        #         'name': 'defaulttodo',
        #         'id': idval,
        #         'subTasks': [{
        #             'task':values[0].replace("create a todo", ""),
        #             'done': False
        #         }],
        #         'shared': [],
        #         'sharedByMe': [],
        #             },
        #     })
            
        # elif response[1] == 'create_note':
        #     return JsonResponse({
        #     'messages': response[0],
        #     'action': response[1],
        #     'function': {
        #         'title': 'defaultnote',
        #         'id': idval,
        #         'type': 'Note',
        #         'description': values[0],
        #         'time': datetime.now().strftime("%d/%m/%Y"),
        #         'mainTime': datetime.now().strftime("%I:%M %p"),
        #         'complete': False,
        #         'shared': [],
        #         'sharedByMe': [],
        #         }
        #     })
            
        # elif response[1] == 'show_people':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     })
            
        # elif response[1] == 'show_friends':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     })
            
        # elif response[1] == 'show_allgroups':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     })
        # elif response[1] == 'show_mygroups':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     })  
        # elif response[1] == 'show_allcommunities':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     })
        # elif response[1] == 'show_mycommunities':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     }) 
        # elif response[1] == 'name':
        #     return JsonResponse({
        #         'messages': response[0]
        #     })
        # elif response[1] == 'creator':
        #     return JsonResponse({
        #         'messages': response[0]
        #     })
            
        # elif response[1] == 'greeting':
        #     return JsonResponse({
        #         'messages': response[0]
        #     })
            
        # elif response[1] == 'commands':
        #     return JsonResponse({
        #         'messages': response[0]
        #     })
        # elif response[1] == 'goodbye':
        #     return JsonResponse({
        #         'messages': response[0]
        #     })
        # elif response[1] == 'nocoinuse':
        #     return JsonResponse({
        #         'messages': response[0]
        #     })
        # elif response[1] == 'view_commands':
        #     return JsonResponse({
        #         'messages': response[0],
        #         'action': response[1]
        #     })
        
        
            
            
        # else:
        #     return JsonResponse({
        #         'messages': "Sorry I don't understand what you mean"
        #     })
     
        # elif coin >= 1:
        #     return JsonResponse({
        #         'messages': oprespo,
        #         'action': 'usecoin'
        #     })  
        
            
        
            
        
        
        
       
                



    
 