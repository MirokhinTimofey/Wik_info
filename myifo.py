#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
 QHBoxLayout, QVBoxLayout,
  QGroupBox, QButtonGroup, 
  QRadioButton, QPushButton, 
  QLabel, QListWidget, QTextEdit, QLineEdit, QInputDialog)

import json
notes = {
    "Китай" : {
        "текст" : "Китай",
        "теги" : ["добро", "инструкция"]
    }
}
import json
notes2 = {
    "Россия" : {
        "текст" : "Основанна",
        "теги" : ["", "инструкция"]
    }
}
with open("notes_data.json", "w")  as file:
    json.dump(notes, file, sort_keys=True, ensure_ascii=False)
with open("notes_data.json", "w")  as file:
    json.dump(notes2, file, sort_keys=True, ensure_ascii=False)

def add():
    note_name, ok = QInputDialog.getText(window, "Добавить страну", "Название страны")
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])

def delete():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        text_field.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Странные заметки')

v_layout = QVBoxLayout()
text_field = QLabel("Информация")
v_layout.addWidget(text_field)

v_layout1_1 = QVBoxLayout()
text_field = QLabel("Название")
v_layout.addWidget(text_field)

v_layout1_2 = QVBoxLayout()
text_field = QLabel("Флаг")
v_layout.addWidget(text_field)

v_layout1_3 = QHBoxLayout()
text1 = QLabel("Гимн")
v_layout1_3.addWidget(text1)

v_layout2 = QHBoxLayout()
list_notes = QListWidget()
v_layout2.addWidget(list_notes)

v_layout3 = QHBoxLayout()
B_Delete = QPushButton("Удалить страну")
v_layout3.addWidget(B_Delete)
B_Create = QPushButton("Записать страну")
v_layout3.addWidget(B_Create)
v_layout4 = QHBoxLayout()
B_vik = QPushButton("Викторина")
v_layout4.addWidget(B_vik)

v_layout6 = QHBoxLayout()
list_tags = QListWidget()
v_layout6.addWidget(list_tags)

h_layout1 = QVBoxLayout()
h_layout1.addLayout(v_layout2)
h_layout1.addLayout(v_layout3)
h_layout2 = QVBoxLayout()
h_layout2.addLayout(v_layout)
h_layout2.addLayout(v_layout1_1)
h_layout2.addLayout(v_layout1_2)
h_layout2.addLayout(v_layout1_3)
h_layout2.addLayout(v_layout4)

main_layout = QHBoxLayout()
main_layout.addLayout(h_layout1)
main_layout.addLayout(h_layout2)
window.setLayout(main_layout)

def show_note():
    key = list_notes.selectedItems()[0].text()
    text_field.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

list_notes.itemClicked.connect(show_note)

with open ("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

B_Create.clicked.connect(add)
B_Delete.clicked.connect(delete)

window.show()
app.exec()