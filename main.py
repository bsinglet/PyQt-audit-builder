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

        self.descriptionLabel = QLabel(self)
        self.descriptionLabel.setText('Description:')
        self.descriptionLine = QLineEdit(self)

        self.descriptionLine.move(SECOND_COLUMN_X, 20)
        self.descriptionLine.resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
        self.descriptionLabel.move(20, 20)
        self.descriptionLabel.adjustSize()

        self.infoLabel = QLabel(self)
        self.infoLabel.setText('Info:')
        self.infoLine = QLineEdit(self)

        self.infoLine.move(SECOND_COLUMN_X, 50)
        self.infoLine.resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
        self.infoLabel.move(20, 50)
        self.infoLabel.adjustSize()

        self.solutionLabel = QLabel(self)
        self.solutionLabel.setText('Solution:')
        self.solutionLine = QLineEdit(self)

        self.solutionLine.move(SECOND_COLUMN_X, 80)
        self.solutionLine.resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
        self.solutionLabel.move(20, 80)
        self.solutionLabel.adjustSize()

        self.cmdLabel = QLabel(self)
        self.cmdLabel.setText('cmd:')
        self.cmdLine = QLineEdit(self)

        self.cmdLine.move(SECOND_COLUMN_X, 110)
        self.cmdLine.resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
        self.cmdLabel.move(20, 110)
        self.cmdLabel.adjustSize()

        self.expectLabel = QLabel(self)
        self.expectLabel.setText('expect:')
        self.expectLine = QLineEdit(self)

        self.expectLine.move(SECOND_COLUMN_X, 140)
        self.expectLine.resize(LINE_EDIT_LENGTH, LINE_EDIT_HEIGHT)
        self.expectLabel.move(20, 140)
        self.expectLabel.adjustSize()

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
        message = f'<custom_item>\n' \
                  f'  type        : CMD_EXEC\n' \
                  f'  description : "{self.descriptionLine.text()}"\n' \
                  f'  info        : "{self.remove_double_quotes(self.infoLine.text())}"\n' \
                  f'  solution    : "{self.remove_double_quotes(self.solutionLine.text())}"\n' \
                  f'  cmd         : "{self.cmdLine.text()}"\n' \
                  f'  expect      : "{self.expectLine.text()}"\n' \
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
