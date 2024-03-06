
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import os
# start to create smart notes app
global text_
text_ = ""
class Note_fuc():
    def __init__(self , notefile):
        self.notefile = str(notefile)
    def createtxtfile(self):
        item = QListWidgetItem(notes_list)
        notes_list.addItem(item)
        with open(self.notefile, "w", encoding="utf-8") as file:
            file.write("")

# name_input_box_data
saved = False


app = QApplication([])
note_window = QWidget()
notes_list_label = QLabel("list of notes")
notes_list = QListWidget()
text_field = QTextEdit()
button_note_create = QPushButton("Create Note")
button_note_delete = QPushButton("Delete note")
button_note_save = QPushButton("Save note")
confirmnotename = QPushButton("Enter")
confirmnotename.hide()
button_note_load = QPushButton('Load note')
search_note = QLineEdit("Search note")
search_note_button_enter = QPushButton("Search")


mainlayout = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(button_note_load)
col_1.addWidget(text_field)


col_2 = QVBoxLayout()
col_2.addWidget(notes_list_label)
col_2.addWidget(notes_list)
col_2.addWidget(search_note)
col_2.addWidget(search_note_button_enter)
row1 = QHBoxLayout()
row1.addWidget(button_note_create)
row1.addWidget(button_note_delete)
col_2.addLayout(row1)

row2 = QHBoxLayout()
row2.addWidget(button_note_save)
col_2.addLayout(row2)

def get_text_set_file_name():
    notes_list.clear()
    global new_file
    new_file = Note_fuc(text_+ ".txt")
    with open("notesdata.txt" , "a" , encoding="utf-8") as file:
        file.write(new_file.notefile)
        file.write("\n")
    with open("notesdata.txt" , "r" , encoding="utf-8") as file:
        for line in file:
            notes_list.addItem(line.strip())
    new_file.createtxtfile()
    nameinputwindow.hide()

def on_text_changed(text): 
    global text_
    text_ = text

# def search_notes(item):
#     global text_
#     global items
#     text_ = ""
#     search_note.textChanged.connect(on_text_changed)
#     for item in :
#         if text_ == item:
#             print("yes")
#         else:
#             print("no")
#             print(item)

print(text_)
def save_text():
    global saved
    saved = False
    global new_file
    new_file = Note_fuc(text_+ ".txt")
    textbox_value = text_field.toPlainText()
    with open(str(new_file.notefile) , "w" , encoding="utf-8") as file:
        file.write(textbox_value)
    with open(str(new_file.notefile) , "r" , encoding="utf-8") as file:
        readfile = file.read()
        print(1 , readfile)

def create_note_file():
    global nameinputwindow
    global inputbox_name
    global entersbutton
    nameinputwindow = QWidget()
    popup_layout = QVBoxLayout(nameinputwindow)
    inputbox_name = QLineEdit("")
    inputbox_name.textChanged.connect(on_text_changed)
    entersbutton = QPushButton("Enter")
    popup_layout.addWidget(inputbox_name)
    popup_layout.addWidget(entersbutton)
    entersbutton.clicked.connect(get_text_set_file_name)
    nameinputwindow.show()

def delet_note_file():
    os.remove(new_file.notefile)
    with open("notesdata.txt" , "r" , encoding="utf-8") as file:
        lines = file.readlines()
    with open("notesdata.txt" , "w" , encoding="utf-8") as file:
        for line in lines:
            if str(new_file.notefile) not in line:
                file.write(line)
    for i in range(notes_list.count()):
        if notes_list.item(i).text() == str(new_file.notefile):
            notes_list.takeItem(i)
            break

def openfile(item):
    if saved == False:
        q_input_ask = QWidget()
        askwindowlayout = QVBoxLayout(q_input_ask)
        nameofaskwindowlayout = QLabel("ARE YOU SURE WANT TO EXIT ?")
        askwindowlayout.addWidget(nameofaskwindowlayout)
        Ok_button = QPushButton("OK")
        askwindowlayout.addWidget(Ok_button)
        Cancel = QPushButton("Cancel")
        askwindowlayout.addWidget(Cancel)
        Ok_button.clicked.connect(save_text)
        Cancel.clicked.connect(notsavetext)
    text_field.clear()
    try:
        with open((item.text()).replace("\n" , ""), "r", encoding="utf-8") as file:
            data = file.read()
            text_field.insertPlainText(data)

    except FileNotFoundError:
        for i in range(notes_list.count()):
            if notes_list.item(i).text() == str(new_file.notefile):
                notes_list.takeItem(i)

def notsavetext():
    global saved
    saved = False

while True:
    new_file = Note_fuc(text_+ ".txt")
    with open("notesdata.txt" , "r" , encoding="utf-8") as file:
        for lines in file:
            notes_list.addItem(str(lines))
        for i in range(notes_list.count()):
            if notes_list.item(i).text() == str(new_file.notefile):
                notes_list.takeItem(i)
    break


            
row3 = QHBoxLayout()
col_2.addLayout(row3)
row_4 = QHBoxLayout()
col_2.addLayout(row_4)
mainlayout.addLayout(col_1 , stretch= 4)
mainlayout.addLayout(col_2 , stretch=1)
note_window.setLayout(mainlayout)
button_note_save.clicked.connect(save_text)
button_note_create.clicked.connect(create_note_file)
button_note_delete.clicked.connect(delet_note_file)
notes_list.itemClicked.connect(openfile)
# search_note_button_enter.clicked.connect(search_notes)
# button_note_load.clicked.connect(loadfile)
note_window.show()
app.exec()
    
