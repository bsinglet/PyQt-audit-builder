#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '28 September 2021'
__version__ = '0.1.0'

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit

SECOND_COLUMN_X = 170
OK_BUTTON_Y = 170
LINE_EDIT_LENGTH = 200
LINE_EDIT_HEIGHT = 32


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        custom_font = QFont()
        custom_font.setPointSize(16)
        self.setFont(custom_font)
        self.setMinimumSize(QSize(640, 400))
        self.setWindowTitle("SQL Policy check builder")

        self.components = ['description', 'info', 'solution', 'cmd', 'expect']
        self.my_objects = dict()
        for index, each_key in enumerate(self.components):
            self.my_objects[each_key] = list()
            self.my_objects[each_key].append(QLabel(self))
            self.my_objects[each_key][0].setText(each_key)
            self.my_objects[each_key].append(QLineEdit(self))
            self.my_objects[each_key][1].move(SECOND_COLUMN_X, 20 + (index*30))
            self.my_objects[each_key][1].resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
            self.my_objects[each_key][0].move(20, 20 + (index*30))
            self.my_objects[each_key][0].adjustSize()

        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.onClick)
        ok_button.resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
        ok_button.move(SECOND_COLUMN_X, OK_BUTTON_Y)

        self.checkOutputEdit = QPlainTextEdit(self)
        self.checkOutputEdit.resize(SECOND_COLUMN_X + LINE_EDIT_LENGTH - 20, LINE_EDIT_HEIGHT * 4)
        self.checkOutputEdit.move(20, OK_BUTTON_Y + 50)


    def remove_double_quotes(self, my_string: str):
        return my_string.replace('"', '\'')


    def onClick(self):
        description = self.my_objects['description'][1].text()
        info = self.remove_double_quotes(self.my_objects['info'][1].text())
        solution = self.remove_double_quotes(self.my_objects['solution'][1].text())
        cmd = self.my_objects['cmd'][1].text()
        expect = self.my_objects['expect'][1].text()
        message = f'<custom_item>\n' \
                  f'  type        : CMD_EXEC\n' \
                  f'  description : "{description}"\n' \
                  f'  info        : "{info}"\n' \
                  f'  solution    : "{solution}"\n' \
                  f'  cmd         : "{cmd}"\n' \
                  f'  expect      : "{expect}"\n' \
                  f'</custom_item>'
        print(message)
        self.checkOutputEdit.setPlainText(message)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
