# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 650)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(86, 86, 86); color: white;\n"
"/*\n"
"qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"*/\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet(u"QTabBar::tab { background: rgba(255, 255, 255, 75); color: white; padding: 10px; } \n"
"      QTabBar::tab:selected { background: rgba(255, 255, 255, 10); \n"
"					  						 border: 1px solid rgba(255, 255, 255, 40);\n"
"											 border-radius: 3px;} \n"
"      QTabWidget::pane { border: 0; } \n"
"      QWidget { background: rgba(255, 255, 255, 10); \n"
"						 border: 1px solid rgba(255, 255, 255, 40);\n"
"						 border-radius: 7px; } \n"
"/*Qtabbar: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;*/")
        self.tab_rasp = QWidget()
        self.tab_rasp.setObjectName(u"tab_rasp")
        self.gridLayout_2 = QGridLayout(self.tab_rasp)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.tab_rasp)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_sort = QLabel(self.frame)
        self.label_sort.setObjectName(u"label_sort")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sort.sizePolicy().hasHeightForWidth())
        self.label_sort.setSizePolicy(sizePolicy)
        self.label_sort.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; color: white;")

        self.horizontalLayout_3.addWidget(self.label_sort)

        self.comboBox_sort_col = QComboBox(self.frame)
        self.comboBox_sort_col.setObjectName(u"comboBox_sort_col")
        self.comboBox_sort_col.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 2px; color: white;")

        self.horizontalLayout_3.addWidget(self.comboBox_sort_col)

        self.comboBox_sort_spos = QComboBox(self.frame)
        self.comboBox_sort_spos.addItem("")
        self.comboBox_sort_spos.addItem("")
        self.comboBox_sort_spos.setObjectName(u"comboBox_sort_spos")
        self.comboBox_sort_spos.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 2px; color: white;")

        self.horizontalLayout_3.addWidget(self.comboBox_sort_spos)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_otp = QLabel(self.frame)
        self.label_otp.setObjectName(u"label_otp")
        sizePolicy.setHeightForWidth(self.label_otp.sizePolicy().hasHeightForWidth())
        self.label_otp.setSizePolicy(sizePolicy)
        self.label_otp.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; color: white;")

        self.horizontalLayout.addWidget(self.label_otp)

        self.comboBox_otp = QComboBox(self.frame)
        self.comboBox_otp.setObjectName(u"comboBox_otp")
        self.comboBox_otp.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 2px; color: white;")

        self.horizontalLayout.addWidget(self.comboBox_otp)

        self.label_prib = QLabel(self.frame)
        self.label_prib.setObjectName(u"label_prib")
        sizePolicy.setHeightForWidth(self.label_prib.sizePolicy().hasHeightForWidth())
        self.label_prib.setSizePolicy(sizePolicy)
        self.label_prib.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; color: white;")

        self.horizontalLayout.addWidget(self.label_prib)

        self.comboBox_prib = QComboBox(self.frame)
        self.comboBox_prib.setObjectName(u"comboBox_prib")
        self.comboBox_prib.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 2px; color: white;")

        self.horizontalLayout.addWidget(self.comboBox_prib)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.start_but = QPushButton(self.frame)
        self.start_but.setObjectName(u"start_but")
        self.start_but.setFont(font)
        self.start_but.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 4px; color: white;")

        self.verticalLayout.addWidget(self.start_but)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QTableView (\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-bottom-right-radius: 7px; border-bottom-left-radius: 7px; }\n"
"\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50); }\n"
"\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"})")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        self.verticalLayout.addWidget(self.tableWidget)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_rasp, "")
        self.tab_news = QWidget()
        self.tab_news.setObjectName(u"tab_news")
        self.gridLayout_3 = QGridLayout(self.tab_news)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame1 = QFrame(self.tab_news)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.gridLayout_4 = QGridLayout(self.frame1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.updateNews_but = QPushButton(self.frame1)
        self.updateNews_but.setObjectName(u"updateNews_but")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.updateNews_but.sizePolicy().hasHeightForWidth())
        self.updateNews_but.setSizePolicy(sizePolicy1)
        self.updateNews_but.setFont(font)
        self.updateNews_but.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 4px; color: white;")

        self.horizontalLayout_2.addWidget(self.updateNews_but)

        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox_Sort_News = QComboBox(self.frame1)
        self.comboBox_Sort_News.addItem("")
        self.comboBox_Sort_News.addItem("")
        self.comboBox_Sort_News.setObjectName(u"comboBox_Sort_News")
        sizePolicy.setHeightForWidth(self.comboBox_Sort_News.sizePolicy().hasHeightForWidth())
        self.comboBox_Sort_News.setSizePolicy(sizePolicy)
        self.comboBox_Sort_News.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_2.addWidget(self.comboBox_Sort_News)

        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_News = QSpinBox(self.frame1)
        self.spinBox_News.setObjectName(u"spinBox_News")
        sizePolicy.setHeightForWidth(self.spinBox_News.sizePolicy().hasHeightForWidth())
        self.spinBox_News.setSizePolicy(sizePolicy)
        self.spinBox_News.setMinimum(1)

        self.horizontalLayout_2.addWidget(self.spinBox_News)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.listWidget_News = QListWidget(self.frame1)
        self.listWidget_News.setObjectName(u"listWidget_News")
        self.listWidget_News.setWordWrap(True)

        self.gridLayout_4.addWidget(self.listWidget_News, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame1, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_news, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.label_New_News = QLabel(self.centralwidget)
        self.label_New_News.setObjectName(u"label_New_News")

        self.gridLayout.addWidget(self.label_New_News, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_sort.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u043e", None))
        self.comboBox_sort_spos.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e", None))
        self.comboBox_sort_spos.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e", None))

        self.label_otp.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_prib.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u0435", None))
        self.start_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rasp), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.updateNews_but.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.comboBox_Sort_News.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043d\u0430\u0447\u0430\u043b\u0430 \u043d\u043e\u0432\u044b\u0435", None))
        self.comboBox_Sort_News.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u0442\u0430\u0440\u044b\u0435", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_news), QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438", None))
        self.label_New_News.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

