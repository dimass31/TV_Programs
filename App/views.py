from django.shortcuts import render_to_response, render
from .models import Broadcast, SearchResults
from selenium import webdriver
from time import sleep

class Parser():
    title =[]  #список названий передач
    description=[] #список описаний передач
    driver = webdriver.Firefox()
    driver.get("https://www.tricolor.tv/program/?type=list")
    sleep(8)
    element = driver.find_element_by_xpath("//*[@class='program-arrow js-program-arrow arrow-next']")
    for i in range(6):
        names = driver.find_elements_by_xpath("//div[@data-hint-title]")
        elems = driver.find_elements_by_xpath("//div[@data-hint-text]")
        for i in range(len(names)):
            title.append(names[i].text)
        for i in range(len(elems)):
            description.append(elems[i].text)
        for i in range(3):
            element.click()
    title = list(set(title))
    description = list(set(description))
    def name(self):
        return self.title
    def desc(self):
        return self.description



def create():
    parser = Parser()
    a = parser.name() # Получаю списки
    b = parser.desc()
    for i in range(len(a)):
        broadcast = Broadcast(name=a[i], description=b[i])
        broadcast.save()


def search_form(request):
    return render_to_response('search-form.html')


def search(request):
    create()
    broadcast =[]
    try:
        s = request.GET['s']
        broadcast = Broadcast.objects.filter(name=s)
        d = SearchResults(word=s,)
        d.save()
    except:
        s = 'Ничего не найдено'
    return render_to_response('search.html', {'s':s, 'broadcast':broadcast,})
