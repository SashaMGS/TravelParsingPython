#pyside6-uic ui_mainwindow.ui > ui_mainwindow.py

import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QStyle, QProxyStyle, QListWidgetItem
from ui_mainwindow import Ui_MainWindow

import requests
from bs4 import BeautifulSoup as BS

urlBegin = "https://www.vl.ru/transport/search?from="
urlOtp = "Артём"
urlMid = "&to="
urlPrib = "Владивосток"
urlEnd = "&day=&ts=0&te=24&route_number=&transport=train"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("WayToVibe")

        self.ui.start_but.clicked.connect(self.parcing)
        self.ui.comboBox_otp.currentIndexChanged.connect(self.changeStationOtp)
        self.ui.comboBox_prib.currentIndexChanged.connect(self.changeStationPrib)
        self.ui.comboBox_sort_col.currentIndexChanged.connect(self.changeSort)
        self.ui.comboBox_sort_spos.currentIndexChanged.connect(self.changeSort)
        self.ui.comboBox_Sort_News.currentIndexChanged.connect(self.changeSortNews)

        self.ui.updateNews_but.clicked.connect(self.parcingNews)

        i = 0
        while i < 3:
            self.ui.tableWidget.insertColumn(0)
            i += 1
# ------------------------ParcingStart---------------------------------------------------------------

        stations = ['Артём', 'Угловая', 'Геологическая', 'Угольная', 'Весенняя', 'Садгород', 'Спутник', 'Океанская',
                    'Санаторная', 'Седанка', 'Чайка', '2+речка', 'Моргородок', '1+речка', 'Владивосток']
        for i in stations:
            self.ui.comboBox_otp.insertItem(len(stations), i)
            self.ui.comboBox_prib.insertItem(len(stations), i)
        self.ui.comboBox_prib.setCurrentIndex(len(stations) - 1)

        self.ui.tableWidget.insertColumn(0)
        self.ui.tableWidget.insertColumn(0)
        self.ui.tableWidget.insertColumn(0)
        headersNews = ['Дата', 'Заголовок', 'Основной текст']
        i = 0
        while i < 3:
            item = QTableWidgetItem()
            item.setText(headersNews[i])
            self.ui.tableWidget.setHorizontalHeaderItem(i, item)
            i += 1

        url = requests.get(urlBegin + urlOtp + urlMid + urlPrib + urlEnd)  # отправка GET-запроса на сайт
        html = BS(url.text, "lxml")
        table = html.find("table")

        # Заполняем массив заголовками
        headers = []
        for i in table.find("thead").findAll("th")[1:-2]:
            title = i.text.replace("  ", "").replace("\n", "")
            headers.append(title)

        # Заполняем таблицу данными
        self.ui.tableWidget.setRowCount(0)
        for j in table.find("tbody").findAll("tr"):
            row_data = j.find_all("td")[1:-1]
            row = [i.text.replace("  ", "").replace("\n", "") for i in row_data]
            self.ui.tableWidget.insertRow(0)
            iNum = 0
            for i in row:
                item = QTableWidgetItem()
                item.setText(i)
                self.ui.tableWidget.setItem(0, iNum, item)
                iNum += 1
        # Заполняем заголовки таблицы и сортировочный comboBox
        self.ui.comboBox_sort_col.clear()
        iNum = 0
        for i in headers:
            item = QTableWidgetItem()
            item.setText(headers[iNum])
            if iNum < 4:
                self.ui.comboBox_sort_col.insertItem(iNum, i)
            self.ui.tableWidget.setHorizontalHeaderItem(iNum, item)
            iNum += 1
        header = self.ui.tableWidget.horizontalHeader()  # Подгоняем размер столбцам
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Подгоняем размер столбцам
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # Подгоняем размер столбцам
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Подгоняем размер столбцам
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Подгоняем размер столбцам
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Подгоняем размер столбцам
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Подгоняем размер столбцам
        if self.ui.comboBox_sort_spos.currentIndex() == 0:
            self.ui.tableWidget.sortItems(
                self.ui.comboBox_sort_col.currentIndex(),
                QtCore.Qt.AscendingOrder)  # (Сортировка) DescendingOrder  AscendingOrder
        else:
            self.ui.tableWidget.sortItems(
                self.ui.comboBox_sort_col.currentIndex(),
                QtCore.Qt.DescendingOrder)  # (Сортировка) DescendingOrder  AscendingOrder
# ------------------------ParcingStart---------------------------------------------------------------
# ------------------------ParcingNEWS_START---------------------------------------------------------------
        url = requests.get("https://www.newsvl.ru/?page=" + str(self.ui.spinBox_News.value()))  # отправка GET-запроса на сайт
        html = BS(url.text, "lxml")
        table = html.find("body")

        timeNews = []
        for i in table.find("div", class_='page__content_main').findAll("span", class_='story-list__item-date'):
            title = i.text
            timeNews.append(title.split(",")[1] + ", " + title.split(",")[0])

        titleNews = []
        for i in table.find("div", class_='page__content_main').findAll("h3", class_='story-list__item-title'):
            title = i.text.replace("(ФОТО)", "")
            titleNews.append(title)

        fullTextNews = []
        for i in table.find("div", class_='page__content_main').findAll("p", class_="story-list__item-overview"):
            title = i.text.replace("(ФОТО)", "")
            fullTextNews.append(title)

            # Заполняем таблицу всеми данными
            self.ui.listWidget_News.clear()
            iNum = 0
        for j in timeNews:
            if len(titleNews) > iNum and len(fullTextNews) > iNum:
                item = QListWidgetItem("_"*150 + "\n" + j + "\n" + titleNews[iNum] + "\n\n" + fullTextNews[iNum])
                self.ui.listWidget_News.addItem(item)
            else:
                return
            iNum += 1
        self.ui.label_New_News.setText(timeNews[0] + " Новость: " + titleNews[0])
        if self.ui.comboBox_Sort_News.currentIndex() == 0:
            self.ui.listWidget_News.sortItems(
                QtCore.Qt.DescendingOrder)  # Сортировка по дате DescendingOrder AscendingOrder
        else:
            self.ui.listWidget_News.sortItems(
                QtCore.Qt.AscendingOrder)  # Сортировка по дате DescendingOrder AscendingOrder
# ------------------------ParcingNEWS_START---------------------------------------------------------------
    def parcing(self):
        if (urlOtp != urlPrib):
            url = requests.get(urlBegin + urlOtp + urlMid + urlPrib + urlEnd)  # отправка GET-запроса на сайт
            html = BS(url.text, "lxml")
            table = html.find("table")

            # Заполняем массив заголовками
            headers = []
            for i in table.find("thead").findAll("th")[1:-2]:
                title = i.text.replace("  ", "").replace("\n", "")
                headers.append(title)

            # Заполняем таблицу данными
            self.ui.tableWidget.setRowCount(0)
            for j in table.find("tbody").findAll("tr"):
                row_data = j.find_all("td")[1:-1]
                row = [i.text.replace("  ", "").replace("\n", "") for i in row_data]
                self.ui.tableWidget.insertRow(0)
                iNum = 0
                for i in row:
                    item = QTableWidgetItem()
                    item.setText(i)
                    self.ui.tableWidget.setItem(0, iNum, item)
                    iNum += 1
            # Заполняем заголовки таблицы и сортировочный comboBox
            self.ui.comboBox_sort_col.clear()
            iNum = 0
            for i in headers:
                item = QTableWidgetItem()
                item.setText(headers[iNum])
                if iNum < 4:
                    self.ui.comboBox_sort_col.insertItem(iNum, i)
                self.ui.tableWidget.setHorizontalHeaderItem(iNum, item)
                iNum += 1
            header = self.ui.tableWidget.horizontalHeader() # Подгоняем размер столбцам
            header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents) # Подгоняем размер столбцам
            header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch) # Подгоняем размер столбцам
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents) # Подгоняем размер столбцам
            header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents) # Подгоняем размер столбцам
            header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents) # Подгоняем размер столбцам
            header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents) # Подгоняем размер столбцам
            if self.ui.comboBox_sort_spos.currentIndex() == 0:
                self.ui.tableWidget.sortItems(
                    self.ui.comboBox_sort_col.currentIndex(),
                    QtCore.Qt.AscendingOrder)  # (Сортировка) DescendingOrder  AscendingOrder
            else:
                self.ui.tableWidget.sortItems(
                    self.ui.comboBox_sort_col.currentIndex(),
                    QtCore.Qt.DescendingOrder)  # (Сортировка) DescendingOrder  AscendingOrder

        else:
            return

# ------------------------Parcing---------------------------------------------------------------

# ------------------------ParcingNEWS---------------------------------------------------------------
    def parcingNews(self):
        url = requests.get("https://www.newsvl.ru/?page=" + str(self.ui.spinBox_News.value()))  # отправка GET-запроса на сайт
        html = BS(url.text, "lxml")
        table = html.find("body")

        timeNews = []
        for i in table.find("div", class_='page__content_main').findAll("span", class_='story-list__item-date'):
            title = i.text
            timeNews.append(title.split(",")[1] + ", " + title.split(",")[0])

        titleNews = []
        for i in table.find("div", class_='page__content_main').findAll("h3", class_='story-list__item-title'):
            title = i.text.replace("(ФОТО)", "")
            titleNews.append(title)

        fullTextNews = []
        for i in table.find("div", class_='page__content_main').findAll("p", class_="story-list__item-overview"):
            title = i.text.replace("(ФОТО)", "")
            fullTextNews.append(title)

            # Заполняем таблицу всеми данными
            self.ui.listWidget_News.clear()
            iNum = 0
        for j in timeNews:
            if len(titleNews) > iNum and len(fullTextNews) > iNum:
                item = QListWidgetItem("_"*150 + "\n" + j + "\n" + titleNews[iNum] + "\n\n" + fullTextNews[iNum])
                self.ui.listWidget_News.addItem(item)
            else:
                return
            iNum += 1
        self.ui.label_New_News.setText(timeNews[0] + " Новость: " + titleNews[0])
        if self.ui.comboBox_Sort_News.currentIndex() == 0:
            self.ui.listWidget_News.sortItems(
                QtCore.Qt.DescendingOrder)  # Сортировка по дате DescendingOrder AscendingOrder
        else:
            self.ui.listWidget_News.sortItems(
                QtCore.Qt.AscendingOrder)  # Сортировка по дате DescendingOrder AscendingOrder

# ------------------------ParcingNEWS---------------------------------------------------------------
    def changeStationOtp(self):
        global urlOtp
        urlOtp = self.ui.comboBox_otp.currentText()

    def changeStationPrib(self):
        global urlPrib
        urlPrib = self.ui.comboBox_prib.currentText()

    def changeSort(self):
        if self.ui.comboBox_sort_spos.currentIndex() == 0:
            self.ui.tableWidget.sortItems(
            self.ui.comboBox_sort_col.currentIndex(),
            QtCore.Qt.AscendingOrder)  # (Сортировка) DescendingOrder  AscendingOrder
        else:
            self.ui.tableWidget.sortItems(
            self.ui.comboBox_sort_col.currentIndex(),
            QtCore.Qt.DescendingOrder)  # (Сортировка) DescendingOrder  AscendingOrder

    def changeSortNews(self):
        if self.ui.comboBox_Sort_News.currentIndex() == 0:
            self.ui.listWidget_News.sortItems(
                QtCore.Qt.DescendingOrder)  # Сортировка по дате DescendingOrder AscendingOrder
        else:
            self.ui.listWidget_News.sortItems(
                QtCore.Qt.AscendingOrder)  # Сортировка по дате DescendingOrder AscendingOrder
# Класс для изменения цвета заголовков TableWidget
class ColoredTableHeaderStyle(QProxyStyle):
    def drawControl(self, element, option, painter, widget=None):
        if element == QStyle.ControlElement.CE_HeaderSection and isinstance(widget, QHeaderView):
            fill = option.palette.brush(QtGui.QPalette.ColorRole.Window)  # Реализация Qt фактически устанавливает фоновую кисть на роль цвета окна, стиль Windows по умолчанию просто игнорирует ее
            painter.fillRect(option.rect, fill)  # Заполняем секцию заголовка фоновой кистью
        else:
            self.baseStyle().drawControl(element, option, painter, widget)

if __name__ == '__main__':
    app = QApplication()
    app.setStyle(ColoredTableHeaderStyle(app.style())) # Устанавливаем стиль заголовков стилю окна
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
