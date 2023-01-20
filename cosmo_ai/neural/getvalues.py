import re
# from listen import *

# find time in the string input provided by the user
def findTime(input):
    # time = re.search(r'\d{1,2}:\d{2}', input)
    # meridiem = re.search(r'\b(am|pm)\b', input)
    # if time:
    #     tvalue = f"{time.group()} {meridiem.group()}"
    #     return tvalue
    # else:
    #     return "notime"
    time_regex1 = r"(1[0-2]|[1-9]):[0-5][0-9] (am|AM|PM|pm)"
    time_search = re.search(time_regex1, input)
    if time_search:
        time = time_search.group(0)
        # meridian = time_search.group(2)
        return time
    else:
        time_regex2 = r"(1[0-2]|[1-9])\s?(am|AM|pm|PM)"
        time_search = re.search(time_regex2, input)
        if time_search:
            time = time_search.group(0)
            # meridian = time_search.group(2)
            return time
        else:
            return "5:04 PM"
    
# find number in the string input provided by the user
def findNumber(input):
    number = re.search(r'\d+', input)
    if number:
        return number.group()
    else:
        return "nonum"
    
# # find date in the string input provided by the user
def findDate(input):
    date = re.search(r'\d{1,2}/\d{1,2}/\d{4}', input)
    if date:
        return date.group()
    else:
        return "nodate"

# find month in the string input provided by the user
def findMonth(input):
    month = re.search(r'\b(january|february|march|april|may|june|july|august|september|october|november|december|next month)\b', input)
    if month:
        return month.group()
    else:
        return "nomonth"
    
# find day in the string input provided by the user
def findDay(input):
    day = re.search(r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow|day after tomorrow|this week|next week|today)\b', input)
    if day:
        return day.group()
    else:
        return "noday"
    
def findrepeat(input):
    repeat = re.search(r'\b(daily|everyday|every week|every month|every sunday|every monday|every tuesday|every wednesday|every thursday|every friday|every saturday)\b', input)
    if repeat:
        return repeat.group()
    else:
        return "norepeat"
    
    
def getValues(query):
    time = findTime(query)
    num = findNumber(query)
    reps = findrepeat(query)
    date = findDate(query)
    month = findMonth(query)
    day = findDay(query)
    message = query.lower().replace(time, "").replace(day, "").replace(reps, "").replace("create a reminder", "").replace("remind me to", "").replace("cosmo", ""). replace("remind", "")
    return message, time, day, date, reps, num, month
    
# query = "remind me to work on my portfolio at 5:00 pm tomorrow"
# print(getValues(query))    
    
# query = input("Enter your query : ")
# # time = findTime(query)
# # date = findDate(query)
# # day = findDay(query)
# # if day == "noday":
# #     print("No day")
# # elif time == "notime":
# #         print("Time not found")
# # else:
# #     print("Time found")
        

# # query = MicExecution()
# print(findDay(query))