#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QLineEdit,
    QListWidget,
    QInputDialog,
    QMessageBox)
import json

'''notes = {
"Добро пожаловать!" : {
"text" : "Это самое лучшее приложение для заметок в мире!",
"tags" : ["добро", "инструкция"]
}
}
with open("notes_data.json", "w", encoding = 'utf-8') as file:
    json.dump(notes, file)'''

def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]['text'])
    list_tags.clear()
    list_tags.addItems(notes[key]['tags'])

def add_note():
    note_name, ok = QInputDialog.getText(min_win,'Добавить заметку','Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'text':'','tags':[]}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['tags'])
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['text'] = field_text.toPlainText()
        with open('notes_data.json','w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        info('Заметка для сохранения не выбрана')

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItem(notes)
        with open('notes_data.json','w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        info('Заметка для удаления не выбрана')

def info(txt):
    mes = QMessageBox()
    mes.setWindowTitle('Message')
    mes.setText(txt)
    mes.show()
    mes.exec_()

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tags.text()
        if not tag in notes[key]['tags']:
            notes[key]['tags'].append(tag)
            list_tags.addItem(tag)
            field_tags.clear()
        with open('notes_data.json','w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        info('Заметка для добавления тэга не выбрана')

def del_tags():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['tags'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['tags'])
        with open('notes_data.json','w', encoding='utf-8') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        info('Тэг для удаления не выбран')

def search_tags():
    tag = field_tags.text()
    if btn6.text() == 'Искать заметку по тегу' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['tags']:
                notes_filtered[note]=notes[note]
        btn6.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif btn6.text() == 'Сбросить поиск':
        field_tags.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        btn6.setText('Искать заметку по тегу')
    else:
        pass





#главное окно

app = QApplication([])
min_win = QWidget()
min_win.resize(500,350)
min_win.setWindowTitle('Умные заметки ')
#список виджетов
text1 = QLabel('Список заметок:')
text2 = QLabel('Список тегов:')

btn1 = QPushButton('Создать заметку')
btn2 = QPushButton('Удалить заметку')
btn3 = QPushButton('Сохранить заметку')
btn4 = QPushButton('Добавит к заметке')
btn5 = QPushButton('Открепить от заметки')
btn6 = QPushButton('Искать заметку по тегу')

list_notes = QListWidget()
list_tags = QListWidget()

field_text = QTextEdit()

field_tags = QLineEdit()

#Список Лэйаутов
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

r_line1 = QVBoxLayout()
l_line1 = QVBoxLayout()

main_line = QHBoxLayout()

line1.addWidget(btn1)
line1.addWidget(btn2)
line2.addWidget(btn4)
line2.addWidget(btn5)
line1.addWidget(btn1)

r_line1.addWidget(text1)
r_line1.addWidget(list_notes)
r_line1.addLayout(line1)
r_line1.addWidget(btn3)
r_line1.addWidget(text2)
r_line1.addWidget(list_tags)
r_line1.addWidget(field_tags)
r_line1.addLayout(line2)
r_line1.addWidget(btn6)

l_line1.addWidget(field_text)

main_line.addLayout(l_line1)
main_line.addLayout(r_line1)
min_win.setLayout(main_line)


list_notes.itemClicked.connect(show_note)

#работа с заметками
btn1.clicked.connect(add_note)
btn2.clicked.connect(del_note)
btn3.clicked.connect(save_note)
#работа с тэгами
btn4.clicked.connect(add_tag)
btn5.clicked.connect(del_tags)
btn6.clicked.connect(search_tags)

min_win.show()

with open('notes_data.json','r', encoding='utf-8') as file:
   notes = json.load(file)
list_notes.addItems(notes)


app.exec_()































































































