
import json



def create_goal():    
    goal = {
       
        "title" : "create_goal",
        "gname" : input("What is the goal? : "),
        "gdes" : input("Please define your goal in 2-3 lines : "),
        "gdline" : input("By when do you want to achieve this goal? : "),
        "gtime" : input("How much daily time are you willing to invest for this goal? : ")
    }
    goal1 = str(goal).lower()
    return goal1

def create_routine():    
    routine = {
        "title" : "create_routine",
        "rtname" : input("What would be the title of the routine? : "),
        "rtdes" : input("Please describe a bit about this routine : "),
        "rtrept" : input("Please select the repeatition mode? :\n\n-Daily \n-Weekly \n-Monthly -\nYearly \n\nRepeat : "), #how to show in UI?
        "rttime" : input("For what time would you like to set reminder for this routine? : ")
    }
    routine1 = str(routine).lower()
    return routine1

def create_task():    
    task = {
        "title" : "create_task",
        "tkname" : input("What would be the goal title? : "),
        "tkdes" : input("Please describe a bit about this goal : "),
        "tkdline" : input("By when do you want to achieve this goal? : "),
        "tktime" : input("How much daily time would you like to give for this goal? : ")
    }
    task1 = str(task).lower()
    return task1

def create_note():    
    note = {
        "title" : "create_note",
        "ntname" : input("What would be the goal title? : "),
        "ntdes" : input("Please describe a bit about this goal : "),
        "ntdline" : input("By when do you want to achieve this goal? : "),
        "nttime" : input("How much daily time would you like to give for this goal? : ")
    }
    return note
 
def create_reminder():    
    reminder = {
        "title" : "create_reminder",
        "rename" : input("What would be the goal title? : "),
        "redes" : input("Kindly describe a bit about this goal : "),
        "redline" : input("By when do you want to achieve this goal? : "),
        "retime" : input("How much daily time would you like to give for this goal? : ")
    }
    return reminder
 
def create_event():    
    event = {
        "title" : "create_event",
        "evname" : input("What would be the goal title? : "),
        "evdes" : input("Kindly describe a bit about this goal : "),
        "evdline" : input("By when do you want to achieve this goal? : "),
        "evtime" : input("How much daily time would you like to give for this goal? : ")
    }
    return event

def create_project():    
    project = {
        "title" : "create_project",
        "prname" : input("What would be the goal title? : "),
        "prdes" : input("Kindly describe a bit about this goal : "),
        "prdline" : input("By when do you want to achieve this goal? : "),
        "prtime" : input("How much daily time would you like to give for this goal? : ")
    }
    return project

def create_todo():    
    todo = {
        "title" : "create_todo",
        "tdname" : input("What would be the goal title? : "),
        "tddes" : input("Kindly describe a bit about this goal : "),
        "tddline" : input("By when do you want to achieve this goal? : "),
        "tdtime" : input("How much daily time would you like to give for this goal? : ")
    }
    return todo

def create_post():    
    post = {
        "title" : "create_post",
        "pstname" : input("What would be the goal title? : "),
        "pstdes" : input("Kindly describe a bit about this goal : "),
        "pstdline" : input("By when do you want to achieve this goal? : "),
        "psttime" : input("How much daily time would you like to give for this goal? : ")
    }
    post1 = str(post).lower()
    return post1

def create_page():    
    todo = {
        "title" : "create_page",
        "pgname" : input("What would be the goal title? : "),
        "pgdes" : input("Kindly describe a bit about this goal : "),
        "pgdline" : input("By when do you want to achieve this goal? : "),
        "pgtime" : input("How much daily time would you like to give for this goal? : ")
    }
    return todo

def create_group():    
    todo = {
        "title" : "create goal",
        "gname" : input("What would be the goal title? : "),
        "gdes" : input("Kindly describe a bit about this goal : "),
        "gdline" : input("By when do you want to achieve this goal? : "),
        "gtime" : input("How much daily time would you like to give for this goal? : ")
    }
    return todo

def view_goal():    
    todo = {
        "title" : "create goal",
        "gname" : input("What would be the goal title? : "),
        "gdes" : input("Kindly describe a bit about this goal : "),
        "gdline" : input("By when do you want to achieve this goal? : "),
        "gtime" : input("How much daily time would you like to give for this goal? : ")
    }
    return todo
    