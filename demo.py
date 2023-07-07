import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle("start")

    # # 按钮控件
    # btn = QPushButton()
    # # 给这个按钮控件设置一个父控件
    # btn.setParent(w)

    label = QLabel("注册", w)

    # 显示位置与大小 ：x, y, w, h
    label.setGeometry(20, 20, 30, 20)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账户")
    edit.setGeometry(50, 20, 200, 20)

    btn = QPushButton("注册", w)
    btn.setGeometry(50, 80, 70, 30)

    w.resize(600, 600)
    w.setWindowFlag(Qt.FramelessWindowHint)

    w.show()

    app.exec_()
