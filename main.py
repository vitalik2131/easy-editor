import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QFiledialog,
    QLabel, QPushButton, QListWidget, 
    QHBoxLayout, QVBoxLayout
)

app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('EasyEditor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
main_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Право")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
btn_flip = QPushButton("Зеркало")
row = QHBoxLayout()
row2 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(main_files)
col2.addWidget(lb_image)


row2.addWidget(btn_left)
row2.addWidget(btn_right)
row2.addWidget(btn_flip)
row2.addWidget(btn_sharp)
row2.addWidget(btn_bw)


col2.addLayout(row2)
row.addLayout(col1)
row.addLayout(col2)



workdir = ''
def chooseWorkdir():
     global workdir
     wordir = QFileDialog.getExistingDirectory()
def filter(files,extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)

   return result


def showFilenamesList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = flinter(listdir(workdir),extensions)
    lw_files.clear()
    for filename in filenames:
    lw_diles.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)
















main_win.setLayout(row)
main_win.show()
app.exec_()