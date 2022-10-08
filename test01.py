from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox #？第1020行左右的①②中要用前两个模块，消息提示框要用第三个模块，所以要导入
#？如果用from PyQt5 import QtWidgets.QApplication，则下面所有的QApplication都要替换为QtWidgets.QApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap #？给界面添加背景图时要用，第81-84行为添加背景代码
from PyQt5 import QtCore, QtWidgets,QtGui #QtGui没有QtWidgets等亮，说明QtGui没被直接用上，但是第二行可看出它所包含的模块被使用了
import sys#？第1020行左右的①③中要用
class data0:#默认管理员账号及密码
    name={"1":"1"}#用字典存数据
    information=[]
#登录界面（已完成）
# #初始类名都是Ui_Form，多个类时为区分需将其重命名，初始继承的父类是object，这里改成QMainWindow
class Login(QMainWindow):
    def __init__(self):#一开始没有这个，要加上
         super(Login,self).__init__()#super里的Login即类名
         self.setupUi(self)
         self.retranslateUi(self)
    def setupUi(self, MainWindow):#？如第81-84行为添加背景代码    登录界面的控件、布局等的设置，qt designer自动生成，也可自己设置，如第81-84行为添加背景代码
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 630)#窗口尺寸前为横长度，后为纵长度
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 170, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 170, 51, 31))
        self.label.setStyleSheet("font: 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 230, 51, 31))
        self.label_2.setStyleSheet("font: 14pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 340, 93, 28))
        self.pushButton.setStyleSheet("font: 14pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 0, 281, 91))
        self.label_3.setStyleSheet("font: 20pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(380, 270, 71, 21))
        self.radioButton.setStyleSheet("font: 7pt \"Arial\";")
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 230, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(460, 270, 71, 21))
        self.radioButton_2.setStyleSheet("font: 7pt \"Arial\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 300, 121, 21))
        self.lineEdit_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 230, 131, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.radioButton.raise_()
        self.lineEdit_3.raise_()
        self.radioButton_2.raise_()
        self.lineEdit_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 839, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu.menuAction())

        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))#"D:\p1.jpg"是图片路径
        # ？加.scaled(MainWindow.width(),MainWindow.height())可将图片适应界面大小，但不能适应拉伸窗口，即使你进行了布局设置，里面的MainWindow就是1020行左右的②
        MainWindow.setPalette(palette)#？MainWindow就是1020行左右的②

        self.retranslateUi(MainWindow)
        self.radioButton.clicked.connect(self.lineEdit_3.hide)#？自己写，也可以designer中设置信号与槽
        self.radioButton_2.clicked.connect(self.lineEdit_3.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_4.hide()
        #将控件动作（信号）联接到方法（槽函数）
        self.pushButton.clicked.connect(self.firstpage_)#？自己写，也可以designer中设置信号与槽，里面的函数是自己定义
    with open("D:/StudentScore.txt","a") as f:  # 创建一个文件存放学生成绩
        f.close()
    with open("D:/Manage.txt","a") as f:  # 创建一个文件存放管理员信息
        f.close()
    def firstpage_(self):#实现管理员信息核对及界面跳转至首页
        book=0
        zhanghao=self.lineEdit_2.text()#从文本框中接收管理员账号
        mima = self.lineEdit_3.text()#从文本框中接收管理员密码
        if zhanghao=='' or mima =='':#账号或密码为空时报错
            QMessageBox.warning(ui_log, "  ","账号或密码不能为空")
            book=1
        elif zhanghao in data0.name.keys() and data0.name[zhanghao]==mima:#输入的为默认账号和密码，可以登录
            MainWindow.close()#当前这个登录窗口关闭
            ui_fir.show()#首页窗口打开
            self.lineEdit_4.hide()
        else:
            f = open("D:/Manage.txt", "r")
            ff = list(f.readlines())
            fi = len(ff)
            for i in range(0, fi, 2):
                #输入的为添加的管理员的账号和密码，可以登录
                if '账号：'+zhanghao + '\n' == ff[i] and '密码：'+mima + '\n' == ff[i+1]:
                    MainWindow.close()
                    ui_fir.show()
                    self.lineEdit_4.hide()
                    book=1
                    break
        if book==0:#book==0说明账号或密码错误
            self.lineEdit_4.show()#该文本框显示"账号或密码错误!"
    def retranslateUi(self, MainWindow):#登录界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))#?第二个参数原本是"MainWindow"(窗口上会显示"MainWindow"字符串），而不是" "(一个空格）,不要设置为""（会自动变成"python"字符串）
        self.label.setText(_translate("MainWindow", "账号："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label_3.setText(_translate("MainWindow", "学生成绩管理系统"))
        self.radioButton.setText(_translate("MainWindow", "隐藏密码"))
        self.radioButton_2.setText(_translate("MainWindow", "显示密码"))
        self.lineEdit_4.setText(_translate("MainWindow", "账号或密码错误!"))
        self.label_4.setText(_translate("MainWindow", "********************"))
        self.menu.setTitle(_translate("MainWindow", "学生成绩管理系统"))
#首页
class Firstpage(QMainWindow):
    def __init__(self):
        super(Firstpage,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):#首页界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 562)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("font: 12pt \"Arial\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("font: 10pt \"Arial\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)
        #将控件动作（信号）联接到方法（槽函数）
        self.pushButton.clicked.connect(self.add_)
        self.pushButton_2.clicked.connect(self.del_)
        self.pushButton_3.clicked.connect(self.que_)
        self.pushButton_4.clicked.connect(self.mod_)
        self.pushButton_6.clicked.connect(self.gua_)
        self.pushButton_5.clicked.connect(self.bye_)
    def add_(self):#跳转添加界面
        ui_add.show()
    def del_(self):#跳转删除界面
        ui_del.show()
    def que_(self):#跳转查询界面
        ui_que.show()
    def mod_(self):#跳转修改界面
        ui_mod.show()
    def gua_(self):#跳转添加管理员界面
        ui_gua.show()
    def bye_(self):#退出（关闭首页界面）
        ui_fir.close()
    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "增加学生成绩"))
        self.pushButton_2.setText(_translate("MainWindow", "删除学生成绩"))
        self.pushButton_3.setText(_translate("MainWindow", "查询学生成绩"))
        self.pushButton_4.setText(_translate("MainWindow", "修改学生成绩"))
        self.pushButton_6.setText(_translate("MainWindow", "添加管理员"))
        self.pushButton_5.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "首页"))
#添加
class Addb(QMainWindow):
    def __init__(self):
         super(Addb,self).__init__()
         self.setupUi(self)
         self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 500, 81, 31))
        self.pushButton.setStyleSheet("font: 10pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 70, 191, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 10pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 120, 191, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(280, 170, 191, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setStyleSheet("font: 10pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(280, 220, 191, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setStyleSheet("font: 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(280, 270, 191, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_5.setStyleSheet("font: 10pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(280, 320, 191, 41))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_6.setStyleSheet("font: 10pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(280, 370, 191, 41))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_7.setStyleSheet("font: 10pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        self.layoutWidget7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget7.setGeometry(QtCore.QRect(280, 420, 191, 41))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_8.setStyleSheet("font: 10pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget7)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 20, 141, 31))
        self.label_9.setStyleSheet("font: 11pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("一")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)
        self.pushButton.clicked.connect(self.add_close)
    def add_close(self):
        book=1
        xuehao = self.lineEdit_2.text()  # ？从文本框中接收学号（为字符串类型）
        f=open("D:/StudentScore.txt","r")#？打开文件并赋给f
        ff=list(f.readlines())#？以每一行为列表的一个元素，将文件内容赋值给ff
        fi=len(ff)
        f.close()
        if (xuehao !='') and (self.lineEdit_2.text()!='')and(self.lineEdit_3.text()!='')\
                and(self.lineEdit_4.text()!='')and(self.lineEdit_5.text()!='')\
                and(self.lineEdit_6.text()!='')and(self.lineEdit_7.text()!='')\
                and(self.lineEdit_8.text()!=''):#成绩等信息的添加不为空
            for i in range(1,fi,8):#？当可迭代序列为列表时，这样实现步长不为1
                if '学号：'+xuehao+'\n'==ff[i]:
                    #？因为ff[i]是字符串加'\n',例如：’0001\n'.注：两个都转为int(xuehao)==int(ff[i])也行
                    book=0
                    #根据学号的唯一性检测信息输入是否正确
                    QMessageBox.warning(ui_add, "  ", "此学生信息已存在，请确认学号输入是否正确！")
                    break
            if book==1:
                #？以可写模式打开文件，实现数据的添加，"w"模式会覆盖数据，而"a"模式则是在文件后面追加
                f=open("D:/StudentScore.txt","a")
                f.write('【姓名】：'+self.lineEdit.text()+'\n')#通过+'\n'实现存入数据的换行
                f.write('学号：'+self.lineEdit_2.text()+'\n')
                f.write('语文：'+self.lineEdit_3.text()+'\n')
                f.write('数学：'+self.lineEdit_4.text()+'\n')
                f.write('英语：'+self.lineEdit_5.text()+'\n')
                f.write('物理：'+self.lineEdit_6.text()+'\n')
                f.write('化学：'+self.lineEdit_7.text()+'\n')
                f.write('生物：'+self.lineEdit_8.text()+'\n')
                f.close()
                QMessageBox.information(ui_add,"  ","添加成功!")#？ui_add也可为self
        else:
            QMessageBox.warning(ui_add, "  ", "项目不能为空！")
    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">姓名<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">学号<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">语文<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">数学<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">英语<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">物理<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">化学<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">生物<span style=\" font-weight:600;\">:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "请输入学生信息："))
        self.menu.setTitle(_translate("MainWindow", "首页->"))
        self.menu_2.setTitle(_translate("MainWindow", "添加学生成绩信息"))
#删除
class Delete(QMainWindow):
    def __init__(self):
         super(Delete,self).__init__()
         self.setupUi(self)
         self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 120, 141, 41))
        self.label.setStyleSheet("font: 10pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 190, 141, 41))
        self.label_2.setStyleSheet("font: 10pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 120, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 190, 141, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 310, 93, 28))
        self.pushButton.setStyleSheet("font: 9pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)
        self.pushButton.clicked.connect(self.dele_close)
    def dele_close(self):
        book = 0  # 默认学生不存在
        name = self.lineEdit.text()  # 从文本框中接收姓名
        xuehao=self.lineEdit_2.text()#学号
        f = open("D:/StudentScore.txt", "r")
        ff = list(f.readlines())
        fi = len(ff)
        f.close()
        if name=='' or xuehao=='':#删除数据时要指明姓名和学号
            QMessageBox.warning(ui_del, "  ", "姓名和学号不能为空！")
        else:
            w = open("D:/StudentScore.txt", "w")#以’w'模式打开文件，可以实现文件内容的覆盖，以更新文件内容
            for i in range(0, fi):#从头开始查找待删除数据的位置
                if ('【姓名】：'+name + '\n' == ff[i]) and ('学号：'+xuehao +'\n'==ff[i+1]):#是待删除数据
                    book = 1#标记一下，说明用户输入的数据存在
                    k=i+8#跳过8行，在文件中刚好跳过待删除的数据
                    for j in range(k,fi):#将剩下的数据存入文件
                        w.write(ff[j])
                    break#跳出循环
                else:#不是待删除的数据，重新写入文件
                    w.write(ff[i])
            if book == 1:
                QMessageBox.information(ui_del, "  ", "删除成功!")#设置窗口提示成功
            else:
                QMessageBox.warning(ui_del, "  ", '该学生不存在，请确认姓名或学号输入是否正确！')
            f.close()
    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "请输入学生姓名:"))
        self.label_2.setText(_translate("MainWindow", "请输入学生学号:"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.menu.setTitle(_translate("MainWindow", "首页->"))
        self.menu_2.setTitle(_translate("MainWindow", "删除学生成绩信息"))
#查询（选择查询方式）
class Queryb(QMainWindow):
    def __init__(self):
        super(Queryb,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 70, 221, 41))
        self.label.setStyleSheet("font: 16pt \"Arial\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 140, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 210, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 280, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)

        self.pushButton.clicked.connect(self.que1_)
        self.pushButton_2.clicked.connect(self.que2_)
        self.pushButton_3.clicked.connect(self.que3_)
    def que1_(self):
        ui_que1.show()#打开以姓名查询的界面
    def que2_(self):
        ui_que2.show()#打开以学号查询的界面
    def que3_(self):#显示所有学生的成绩信息，就不设界面了，直接显示在一个消息窗口里吧
        f = open("D:/StudentScore.txt", "r")
        ff = list(f.readlines())
        fi = len(ff)
        f.close()
        cj = []#创建一个列表存放学生数据
        if fi==0:
            QMessageBox.warning(ui_que, "  ", '尚未录入学生信息！')#文件长度为0，即未录入
        else:
            k=1#标个序号
            for i in range(0, fi, 8):#从头开始将文件数据加工后存入cj
                # #因为文件中存的是数据加'\n'所构成的字符串,用切片的方式，不将最后的'\n'存入列表cj中(\n占一个位置，不是两个哦)
                cj.append('。<br>'+str(k)+'、' + ff[i][0:len(ff[i]) - 1])
                cj.append(ff[i + 1][0:len(ff[i + 1]) - 1])#QMessageBox里的换行是<br>,不是\n
                cj.append(ff[i + 2][0:len(ff[i + 2]) - 1]+'分')
                cj.append(ff[i + 3][0:len(ff[i + 3]) - 1]+'分')
                cj.append(ff[i + 4][0:len(ff[i + 4]) - 1]+'分')
                cj.append(ff[i + 5][0:len(ff[i + 5]) - 1]+'分')
                cj.append(ff[i + 6][0:len(ff[i + 6]) - 1]+'分')
                cj.append(ff[i + 7][0:len(ff[i + 7]) - 1]+'分')
                k=k+1
            cj.append('<br>')
            QMessageBox.information(ui_que, "成绩信息",str(cj))#将列表cj存放的数据（学生成绩信息）显示在消息窗口
    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "请选择查询方式:"))
        self.pushButton.setText(_translate("MainWindow", "按姓名查询"))
        self.pushButton_2.setText(_translate("MainWindow", "按学号查询"))
        self.pushButton_3.setText(_translate("MainWindow", "显示所有学生信息"))
        self.menu.setTitle(_translate("MainWindow", "查询学生成绩->"))
        self.menu_2.setTitle(_translate("MainWindow", "查询方式"))
#查询（姓名方式）（已完成）
class Queryb1(QMainWindow):
    def __init__(self):
        super(Queryb1,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 80, 191, 41))
        self.label.setStyleSheet("font: 16pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 200, 191, 41))
        self.lineEdit.setStyleSheet("font: 10pt \"Agency FB\";")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)
        self.pushButton.clicked.connect(self.que1)
    def que1(self):
        book=0#默认学生不存在
        name = self.lineEdit.text()  # 从文本框中接收姓名
        f = open("D:/StudentScore.txt", "r")
        ff = list(f.readlines())
        f.close()
        fi = len(ff)
        cj = []
        k=1#序号
        if name=='':
            QMessageBox.warning(self, "  ", '姓名输入不能为空！')
        else:
            for i in range(0, fi, 8):#从头开始将姓名符合的文件数据加工后存入cj
                if '【姓名】：'+name + '\n' == ff[i]:
                    #因为文件中存的是数据加'\n'所构成的字符串,用切片的方式，不将最后的'\n'存入列表cj中
                    cj.append('<br>'+str(k)+'、' + ff[i][0:len(ff[i]) - 1])
                    cj.append(ff[i + 1][0:len(ff[i + 1]) - 1])
                    cj.append(ff[i + 2][0:len(ff[i + 2]) - 1]+'分')
                    cj.append(ff[i + 3][0:len(ff[i + 3]) - 1]+'分')
                    cj.append(ff[i + 4][0:len(ff[i + 4]) - 1]+'分')
                    cj.append(ff[i + 5][0:len(ff[i + 5]) - 1]+'分')
                    cj.append(ff[i + 6][0:len(ff[i + 6]) - 1]+'分')
                    cj.append(ff[i + 7][0:len(ff[i + 7]) - 1]+'分')
                    book=1
                    k=k+1
            cj.append('<br>')
            if book==1:
                QMessageBox.information(ui_que1, "信息", str(cj))
            else:
                QMessageBox.warning(ui_que1, "  ",'该学生不存在，请确认姓名输入是否正确！')

    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "请输入学生姓名"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.menu.setTitle(_translate("MainWindow", "查询学生成绩->"))
        self.menu_2.setTitle(_translate("MainWindow", "按学生姓名查询"))
#查询（学号方式）（已完成）
class Queryb2(QMainWindow):
    def __init__(self):
        super(Queryb2,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 80, 191, 41))
        self.label.setStyleSheet("font: 16pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 200, 191, 41))
        self.lineEdit.setStyleSheet("font: 10pt \"Agency FB\";")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        picture = QPalette()
        picture.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(picture)
        self.pushButton.clicked.connect(self.que2)
    def que2(self):#和que1基本相同
        book = 0  # 默认学生不存在
        xuehao = self.lineEdit.text()  # 从文本框中接收姓名
        f = open("D:/StudentScore.txt", "r")
        ff = list(f.readlines())
        f.close()
        fi = len(ff)
        cj = []
        if xuehao=='':
            QMessageBox.warning(self, "  ", '学号输入不能为空！')
        else:
            for i in range(1, fi, 8):
                if '学号：'+xuehao + '\n' == ff[i]:
                    cj.append(ff[i - 1][0:len(ff[i - 1]) - 1])
                    cj.append(ff[i][0:len(ff[i]) - 1])
                    cj.append(ff[i + 1][0:len(ff[i + 1]) - 1]+'分')
                    cj.append(ff[i + 2][0:len(ff[i + 2]) - 1]+'分')
                    cj.append(ff[i + 3][0:len(ff[i + 3]) - 1]+'分')
                    cj.append(ff[i + 4][0:len(ff[i + 4]) - 1]+'分')
                    cj.append(ff[i + 5][0:len(ff[i + 5]) - 1]+'分')
                    cj.append(ff[i + 6][0:len(ff[i + 6]) - 1]+'分')
                    book = 1
            if book == 1:
                QMessageBox.information(ui_que2, "信息", str(cj))
            else:
                QMessageBox.warning(ui_que2, "  ", '该学生不存在，请确认学号输入是否正确！')

    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "请输入学生学号"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.menu.setTitle(_translate("MainWindow", "查询学生成绩->"))
        self.menu_2.setTitle(_translate("MainWindow", "按学生学号查询"))
#修改
class Modify0(QMainWindow):
    def __init__(self):
         super(Modify0,self).__init__()
         self.setupUi(self)
         self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 210, 50, 25))
        self.label_4.setStyleSheet("font: 13pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 210, 171, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 250, 50, 25))
        self.label_5.setStyleSheet("font: 13pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 250, 171, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 290, 50, 25))
        self.label_6.setStyleSheet("font: 13pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 290, 171, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 330, 50, 25))
        self.label_7.setStyleSheet("font: 13pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 330, 171, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 370, 50, 25))
        self.label_8.setStyleSheet("font: 13pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(280, 370, 171, 24))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 410, 50, 25))
        self.label_9.setStyleSheet("font: 13pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(280, 410, 171, 24))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 130, 71, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 170, 61, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(130, 80, 391, 21))
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 231, 38))
        self.label_3.setStyleSheet("font: 20pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 170, 50, 25))
        self.label_2.setStyleSheet("font: 13pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 170, 171, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 130, 171, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 130, 50, 25))
        self.label.setStyleSheet("font: 13pt \"Arial\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 470, 93, 34))
        self.pushButton.setStyleSheet("font: 13pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)
        self.pushButton.clicked.connect(self.modi)
    def modi(self):#和删除操作类似
        book = 0  # 默认学生不存在
        name = self.lineEdit.text()  # 从文本框中接收姓名
        xuehao = self.lineEdit_2.text()  # 学号
        f = open("D:/StudentScore.txt", "r")
        ff = list(f.readlines())
        fi = len(ff)
        f.close()
        if name == '' or xuehao == '':#修改数据时要指明姓名和学号
            QMessageBox.warning(ui_del, "  ", "姓名和学号不能为空！")
        else:
            w = open("D:/StudentScore.txt", "w")#以’w'模式打开文件，可以实现文件内容的覆盖，以更新文件内容
            for i in range(0, fi):#从头开始查找待修改数据的位置
                if ('【姓名】：'+name + '\n' == ff[i]) and ('学号：'+xuehao + '\n' == ff[i + 1]):#是待修改的学生的数据
                    book = 1#用户数据输入正确
                    w.write(ff[i])#姓名
                    w.write(ff[i + 1])#学号
                    #以下六个条件判断语句将要修改的数据重写入文件
                    if self.lineEdit_3.text()!='':#不为空，说明用户输入了修改后的数据，将修改后的数据重写入文件
                        w.write('语文：'+self.lineEdit_3.text()+'\n')
                    else:#为空，说明用户没有输入修改后的数据，将原数据重写入文件
                        w.write(ff[i+2])
                    if self.lineEdit_4.text()!='':
                        w.write('数学：'+self.lineEdit_4.text()+'\n')
                    else:
                        w.write(ff[i+3])
                    if self.lineEdit_5.text()!='':
                        w.write('英语：'+self.lineEdit_5.text()+'\n')
                    else:
                        w.write(ff[i+4])
                    if self.lineEdit_6.text()!='':
                        w.write('物理：'+self.lineEdit_6.text()+'\n')
                    else:
                        w.write(ff[i+5])
                    if self.lineEdit_7.text()!='':
                        w.write('化学：'+self.lineEdit_7.text()+'\n')
                    else:
                        w.write(ff[i+6])
                    if self.lineEdit_8.text()!='':
                        w.write('生物：'+self.lineEdit_8.text()+'\n')
                    else:
                        w.write(ff[i+7])
                    k = i + 8#跳过8行，在文件中刚好跳过待修改的数据
                    for j in range(k, fi):#将剩下的数据存入文件
                        w.write(ff[j])
                    break
                else:#不是待修改的学生的数据，重新写入文件
                    w.write(ff[i])
            if book == 1:
                QMessageBox.information(self, "  ", "修改成功!")
            else:
                QMessageBox.warning(self, "  ", "该学生不存在,请确认姓名或学号输入是否正确！")
            f.close()
    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label_4.setText(_translate("MainWindow", "语文:"))
        self.label_5.setText(_translate("MainWindow", "数学:"))
        self.label_6.setText(_translate("MainWindow", "英语:"))
        self.label_7.setText(_translate("MainWindow", "物理:"))
        self.label_8.setText(_translate("MainWindow", "化学:"))
        self.label_9.setText(_translate("MainWindow", "生物:"))
        self.label_10.setText(_translate("MainWindow", "【必填】"))
        self.label_11.setText(_translate("MainWindow", "【必填】"))
        self.label_12.setText(_translate("MainWindow", "注:在需要修改的课程栏填写修改后的成绩后点击确定即可"))
        self.label_3.setText(_translate("MainWindow", "请输入学生信息"))
        self.label_2.setText(_translate("MainWindow", "学号:"))
        self.label.setText(_translate("MainWindow", "姓名:"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.menu.setTitle(_translate("MainWindow", "修改学生成绩->"))
        self.menu_2.setTitle(_translate("MainWindow", "学生信息"))
#添加管理员（已完成）
class Guanli(QMainWindow):
    def __init__(self):
        super(Guanli,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):#界面的控件、布局等的设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 171, 41))
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 110, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 61, 31))
        self.label_2.setStyleSheet("font: 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 170, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 170, 61, 31))
        self.label_3.setStyleSheet("font: 11pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 240, 93, 28))
        self.pushButton.setStyleSheet("font: 9pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 背景设置部分
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("D:\p1.jpg").scaled(MainWindow.width(),MainWindow.height())))
        MainWindow.setPalette(palette)
        self.pushButton.clicked.connect(self.gua_close)
    def gua_close(self):
        book = 1
        zhanghao = self.lineEdit.text()  # 从文本框中接收账号
        mima=self.lineEdit_2.text()  # 从文本框中接收账号
        f = open("D:/Manage.txt", "r")
        ff = list(f.readlines())
        fi = len(ff)
        for i in range(0,fi,2):
            if '账号：'+zhanghao+'\n' == ff[i]:  # 检测账号是否已经存在
                book = 0
                # 根据账号的唯一性检测信息输入是否正确
                QMessageBox.warning(ui_gua,"  ","账号已存在，请确认账号输入是否正确！")
                break
        f.close()
        if zhanghao=='' or mima =='':#"账号或密码不能为空"
            QMessageBox.warning(ui_log, "  ","账号或密码不能为空")
        elif book == 1:#不是上面两种情况，说明为正常情况
            f = open("D:/Manage.txt","a")
            f.write('账号：'+str(self.lineEdit.text())+"\n")#将设置的账号添加到Manage文件中
            f.write('密码：'+self.lineEdit_2.text()+"\n")#将设置的密码添加到Manage文件中
            f.close()
            QMessageBox.information(ui_gua, "  ", "添加成功!")
    def retranslateUi(self, MainWindow):#界面的控件、布局等的设置
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "请输入管理员信息:"))
        self.label_2.setText(_translate("MainWindow", "账    号:"))
        self.label_3.setText(_translate("MainWindow", "密    码:"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.menu.setTitle(_translate("MainWindow", "主页->"))
        self.menu_2.setTitle(_translate("MainWindow", "添加管理员"))
if __name__ == '__main__':#自己加的
    app = QApplication(sys.argv)#①
    MainWindow = QMainWindow()#②   和设计界面时的窗口类型有关
    #下面创建一些界面对象
    ui_fir= Firstpage()
    ui_log=Login()
    ui_add=Addb()
    ui_del = Delete()
    ui_mod = Modify0()
    ui_que = Queryb()
    ui_que1 = Queryb1()
    ui_que2=Queryb2()
    ui_gua=Guanli()

    ui_log.setupUi(MainWindow)#从哪个界面开始
    MainWindow.show()
    sys.exit(app.exec_())#③


