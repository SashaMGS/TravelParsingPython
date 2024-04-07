import requests  # импорт библиотеки для отправки HTTP-запросов
from bs4 import BeautifulSoup as BS  # импорт класса BeautifulSoup из библиотеки bs4

url = requests.get("https://www.vl.ru")  # отправка GET-запроса на сайт
html = BS(url.content, "html.parser")  # создание объекта BeautifulSoup для анализа содержимого сайта

for el in html.select(".body > .layout_default.layout_fixed > .layout__content > .news > .news__latest-posts"):
    # выбор всех элементов с указанным CSS-селектором
    timeEl = el.select("span")  # выбор всех элементов по тегу 'span'
    title = el.select("h3 > a")  # выбор всех элементов по тегу 'h3', вложенным в 'a'
    fullElement = ""  # инициализация переменной для хранения результирующей информации
    i = 0  # инициализация счётчика

    while i < len(timeEl):  # цикл для объединения текстов времени и заголовков
        fullElement += timeEl[i].text + " " + title[i].text + "\n"
        i += 1  # увеличение счётчика

print("Новости Г.Владивосток\n" + fullElement)  # вывод всех текстов времени и заголовков (результирующей информации) после завершения выполнения кода

