# 引入PyQt5.QtWidgets模块，这个模块包含基本的组件
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。使得Python脚本可以在shell里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)

    # QWidget控件是一个用户界面的基本控件，也被称为窗口（window）控件。
    w = QWidget()
    # resize()方法表示鼠标能改变控件的大小，这里的意思是窗口默认大小为宽250px，高150px。
    w.resize(500, 400)
    # move()方法表示鼠标能改变控件的位置，这里的意思是窗口默认位置在(300, 300)。注：屏幕坐标系的原点是屏幕的左上角。
    w.move(300, 300)
    # 给窗口添加标题
    w.setWindowTitle('百助广告项目组工具集合')
    # show()能让控件在桌面上显示出来
    w.show()

    # 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件派发到应用控件里。
    # 当调用exit()方法或直接销毁主控件时，主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境会收到主控件如何结束的信息。
    sys.exit(app.exec_())