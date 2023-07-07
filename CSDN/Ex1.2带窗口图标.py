import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 这个类继承自QWidget
class Example(QWidget):

    def __init__(self):
        # 继承类的初始化写法
        super().__init__()
        # 使用initUI()方法创建一个GUI。
        self.initUI()

    def initUI(self):
        # 下面的三个方法都继承自QWidget类。
        # setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
        # 第二个方法还是给窗口添加标题
        # 最后一个方法是给窗口添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标。
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('Ex2.jpg'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())