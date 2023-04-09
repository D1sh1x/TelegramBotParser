import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
   "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34"
}

def work_url():
    for count in range(0, 4):
        url = f"https://krasnodar.hh.ru/vacancies/programmist?page={count}"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all("div", class_='serp-item')
        for i in data:
            work_url_card = i.find("a", class_='serp-item__title').get("href")
            yield work_url_card


for card in work_url():
    sleep(1)
    response = requests.get(url=card, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find("div", class_="bloko-column bloko-column_container bloko-column_xs-4 bloko-column_s-8 bloko-column_m-12 bloko-column_l-10")
    def nameZP():
        title = data.find("div", class_="vacancy-title")
        name = title.find("h1", class_="bloko-header-section-1").text
        zp = title.find("span", class_="bloko-header-section-2 bloko-header-section-2_lite").text
        return name, zp
    def skills():
        list_skills = []
        skill_div = data.find_all("div", class_="bloko-tag bloko-tag_inline")
        for i in skill_div:
            skill_span = i.find("span", class_="bloko-tag__section bloko-tag__section_text").text
            list_skills.append(skill_span)
        return list_skills




