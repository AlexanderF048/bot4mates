import time
import uuid
import random
from collections import UserDict
from datetime import datetime
import json

#---------------------------------------------------------------------------------------------
class NoteBase(UserDict):
    def add_record(self, record):
        self.data[record.note_id] = record
    def __str__(self):
        return f"{self.values()}" 
  

class Tag:
    def __init__(self):
        self.note_id=str(uuid.uuid1()) #Автоматически будет присвоен уникальный токен UUID1 формата
        self.note_tag=[]
        self.note_keyword=""
    

class NoteRecord(Tag):
    def __init__(self):
        super().__init__() #Подтягиваем __init__ из Tag
        self.note_data: str  = "" 
        self.note_date=datetime.now() #Автоматически будет присвоено время создания
    def __str__(self):
        return f"\nID: {self.note_id}\nDate: {self.note_date}\nTag: {self.note_tag}\nKeyword: {self.note_keyword}\n\nNote:\n_________________________________\n\n{self.note_data}" 
    def __repr__(self):
        return f"{self}"

NOTEBASE=NoteBase()

#---------------------------------------------------------------------------------------------    
def flasher(text, speed=0.099):
    
    for i in text:
        time.sleep(speed)
        print(i, end='', flush=True)
    print('\r', end='')

def add_note():
    input_data=input('Write your notes right here and press "Enter" when you are done:\n>>>')

    new_note=NoteRecord()
    new_note.note_data=input_data

    particles_note=new_note.note_data.split(" ")
    new_note.note_keyword: str = 'No keyword (phrase).' if len(particles_note) == 0 else str(random.choices(particles_note, k=1))
    print("{:*^40}".format("Your note have random keyword"))
    
    
    while True:
        input_data=input('Would you like to assign a tag?\nInput next: yes/no\n>>>')
        
        if input_data == "yes":
            new_note.note_tag.append(input('Assign first tag: '))
            print("{:*^40}".format("Your note have first tag"))
            break
        elif input_data == "no":
            print("{:*^40}".format("Your note don\'t have any tags"))
            break
        else:
            flasher('Something went wrong!',0.05)
           

    
    input_data_2=input('Would you like to save your note in stream? yes/no:\n')
    if input_data_2 == 'yes':
        cl_notebase_input=NOTEBASE.add_record(new_note)
        print('\n.....Your was saved in stream.....')
        print(NOTEBASE)

def find_in_note():
    input_data=input('Please, input the phrase, you want to de finded:\n>>>')
    matches_id_list=[]
    match_counter=0
    
    for value in NOTEBASE.values():
        
        if value.note_data.find(input_data) > -1:
            matches_id_list.append(value.note_id)
    
    if len(matches_id_list) > 0:
        for i in map(lambda id: id, matches_id_list):
            match_counter+=1
            print("{:=^70}".format("="))
            print(f"Match {match_counter} in NOTEBASE:")
            print(i)
            print(NOTEBASE[i].note_data)

def delete_note():
    input_data=input('Please, input the note ID, you want to de burned:\n>>>')

    if input_data in NOTEBASE.keys():
        NOTEBASE.pop(input_data)
    print(f"\nRecord {input_data} sucsessfuly deleated.")

def burn_base():
    NOTEBASE.clear()
    print("{:-^70}".format("BASE TOTALY BURNED"))

def change_note():
    input_data=input('Please, input the note ID, you want to de changed:\n>>>')
    while True:
        if input_data in NOTEBASE.keys():
            input_data_2=input('Please, input new content:\n>>>')
            if input("You shure, you want to cave changes?\nyes/no>>>") == "yes":
                NOTEBASE[input_data].note_data=input_data_2
                print(f"\nRecord {input_data} sucsessfuly changed.")
                break

def show_all():
    for i in map(lambda id: id, NOTEBASE):
        print("{:=^70}".format("="))
        print(NOTEBASE[i])

def set_tag():
    input_data=input('Please, input the note ID, to add tag:\n>>>')
    if input_data in NOTEBASE.keys():
        input_data_2=input('Please, input new tag:\n>>>')
        NOTEBASE[input_data].note_tag.append(input_data_2)
        print(f"\nRecord {input_data} have new tag.")

def clear_tags():
    input_data=input('Please, input the note ID, to clear ALL tags:\n>>>')
    while True:
        if input_data in NOTEBASE.keys():
            if input("You shure, you want to delete tags?\nyes/no>>>") == "yes":
                NOTEBASE[input_data].note_tag.clear()
                print(f"\nRecord {input_data} sucsessfuly cleanded from all tags.")
                break

def save_handler(book=NOTEBASE):
    
    inner_val=[]
    json_dict_pattern={"note_base":inner_val} 
   
    for val_id, all_fields in book.data.items():         
        note_data={val_id:[
            {"Tag":str(all_fields.note_tag)},
            {"Keyword":str(all_fields.note_keyword)},
            {"Notes":str(all_fields.note_data)},
            {"Date":str(all_fields.note_date)}
            ]}
        inner_val.append(note_data)
        print(inner_val)
    with open("note_base.json", "w") as fh:
        json.dump(json_dict_pattern, fh)
        print("Saved on your HardDrive. Current directory.")
                
#---------------------------------------------------------------------------------------------
def call_notebook():
    notebook_commands={
        "add note":add_note,
        "find in note":find_in_note, #Поиск внутри заметок, согласно пункту №7 ТЗ, ищет в тексте и выдает ID
        "delete":delete_note,
        "burn":burn_base,
        "change":change_note,
        "show base":show_all,
        "tag":set_tag,
        "clear tags":clear_tags,
        "save on HD":save_handler 
    }
    
    flasher('Welcome on board "Notepad 1.0" !')

    while True:

        input_data=input('''\n\nPlease, choose your command regarding to:
"add note"- create new note
"stop notes"- exit from notebook
"find in note"- can find lines in base
"delete"- delete note
"burn" - burn base
"change" - change note
"show base" - show all positions in base
"tag" - add tag to note
"clear tags" - clear ALL tags in note
"save on HD" - exactley that
>>>''')
            
        for command, action in notebook_commands.items():
            
            if input_data == "stop notes":
                print('\nYou finished with notes.\n')
                break
    
            elif input_data == command:
                push=notebook_commands[command]
                push()

            elif input_data not in notebook_commands.keys():
                flasher('Something went wrong!',0.05)

def main():

    call_notebook()
    
if __name__ == '__main__':  
    exit(main())