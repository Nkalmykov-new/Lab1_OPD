from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    lt=[]
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php' # передаем необходимы URL адрес
    page = requests.get(url, verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, 'html.parser') # передаем страницу в bs4

    tags=soup.find('div', id='pagecontent')

    for tag in tags.findAll('a'):
        lt.append(tag.text.strip())

    file=open('Список кафедр.txt','w')
    for l in lt:
        print(l)
        file.write(l)
        file.write("\n")
    file.close()

    print('Файл "Список кафедр.txt" создан')