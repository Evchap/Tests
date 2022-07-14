'''
Задача 2
В нашей школе мы не можем разглашать персональные данные пользователей,
но чтобы преподаватель и ученик смогли объяснить нашей поддержке,
кого они имеют в виду (у преподавателей, например, часто учится несколько Саш),
мы генерируем пользователям уникальные и легко произносимые имена.
Имя у нас состоит из прилагательного, имени животного и двузначной цифры.
В итоге получается, например, "Перламутровый лосось 77".
Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR)
и вывести количество животных на каждую букву алфавита.
Результат должен получиться в следующем виде:
А: 642
Б: 412
В:....
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen


url = [
    "https://inlnk.ru/jElywR",

]


def urls_of_other_pages(url):
    url_other_pages: list = []

    for x in url:
        html_code = str(urlopen(x).read(), 'utf=8')
        soup = BeautifulSoup(html_code, 'html.parser')
        s = soup.find_all("div", class_="mw-pages")

        for link in soup.find_all('a')[6:37]:
            new_href = link.get('href')
            url_other_pages.append(new_href)

    url.extend(url_other_pages)
    return url


def writing_to_file():
    file = open('names_of_animals.txt', 'a')

    for x in url:
        html_code = str(urlopen(x).read(), 'utf=8')
        soup = BeautifulSoup(html_code, 'html.parser')
        p = soup.find("body").find_all("li")[2:-63]
        for i in p:
            file.write(i.text + ' ')

    file.close()


def count_of_wodrs():
    letter_chr = 1040
    file = open('names_of_animals.txt', 'r')
    names_of_animals: str = file.read()
    for i in range(0, 32):
        count = names_of_animals.count(chr(letter_chr))
        print(chr(letter_chr), ":", count)
        letter_chr += 1

    file.close()

def main():
    urls_of_other_pages(url)
    writing_to_file()
    count_of_wodrs()


if __name__ == '__main__':
    main()
