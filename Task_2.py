# Task 2
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def task_2():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  
    url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(url)
    letter = browser.find_element_by_class_name("mw-category-group h3").text
    li = browser.find_elements_by_class_name("mw-category-group ul li")
    result = dict()
    count = 0
    while letter != 'Я':
        li = browser.find_elements_by_class_name("mw-category-group ul li")
        if li[199].text[0] != letter:
            for i in li:
                if i.text[0] == letter:
                    count += 1           
                else:
                    if letter in result.keys():
                        result[letter] += count
                    else:
                        result[letter]=count
                    print(letter, count, i.text)
                    count = 1
                    letter = i.text[0]
        else:
            count += 200
        browser.find_element_by_xpath("//*[contains(text(), 'Следующая страница')]").click()

    print("Без повторений, сортировка по первой букве")
    for k, v in result.items():
        print(k, ":",  v)
    return result


# Или при помощи парсера как второй вариант
url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
# и т. д. аналогично первому варианту