import flet as ft
import TaskManager

import json
def main(page: ft.Page):
    def readjson():
        
        readjson.data =[]
        
        with open('Taskjson.json') as f: #thanks to martijn pieters on stackoverflow for this solution from back in 2012!
            for line in f:
                task=json.loads(line)
                readjson.task_name = task['taskname'].strip("{}'\"")
                readjson.task_due = task['taskduedate'].strip("{}'\"") #had to cheat and use gpt to figure out how to clean this
                readjson.time_remaining = task['timeremaining']      # but i understand what its doing after i look at it
                #adding slashes to the date to make it readable
                readjson.formatted_task_due=f"{readjson.task_due[:2]}/{readjson.task_due[2:]}" #this was from DarinP on stackoverflow in 2020, thanks!
                readjson.formatted_task_due=f"{readjson.formatted_task_due[:5]}/{readjson.formatted_task_due[5:]}"
                # Store as a dictionary for easy access in the UI
                readjson.data.append({
                    'name': readjson.task_name,
                    'due': readjson.formatted_task_due,
                    'remaining': readjson.time_remaining
                })
        
    page.theme_mode=ft.ThemeMode.DARK
    page.title = "YAPTM" #yet another python task manager!
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    #top row
    page.add(
        ft.Row(spacing=0, alignment=ft.MainAxisAlignment.START,controls=[
            
            ft.Container(content=ft.Text("Task Name"),margin=0,padding=0,alignment=ft.Alignment(-0.5,0),bgcolor='#17292F',width=700),
            ft.Container(content=ft.Text("Due Date"),margin=0,padding=0,alignment=ft.alignment.center,bgcolor='#17292F',width=400),
            ft.Container(content=ft.Text("Time Remaining"),margin=0,padding=0,alignment=ft.alignment.center,bgcolor='#17292F',width=150),
            ft.Container(content=ft.Text(""),width=10000000,bgcolor='#17292F')
            ])
           
        )
    #reads json and adds tasks
    readjson()
    for x,task in enumerate(readjson.data):
        
        page.add(
        ft.Row(spacing=0,alignment=ft.MainAxisAlignment.START,controls=[
            ft.Container(content=ft.Text(task['name']),margin=0,padding=0,alignment=ft.Alignment(-1,0),bgcolor='#17292F',width=700),
            ft.Container(content=ft.Text(task['due']),margin=0,padding=0,alignment=ft.alignment.center,bgcolor='#17292F',width=400),
            ft.Container(content=ft.Text(task['remaining']),margin=0,padding=0,alignment=ft.alignment.center,bgcolor='#17292F',width=150),
            ft.Container(content=ft.Text(""),width=10000000,bgcolor='#17292F')
            ])
           
        )
    
ft.app(main)

