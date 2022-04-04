import requests
from bs4 import BeautifulSoup as bs

def quantita():
    n = int(input("quante notizie vuoi?"))
    return n
def scrivi():
    n=quantita()
    rq = requests.get("https://www.ansa.it")
    test=bs(rq.text,features="html.parser")
    test2 = test.findAll("h3", {"class": "news-title"})
    file = open("prova.txt", "w")
    for test in test2[:n]:
        file.write(test.text)
        file.write("\n")
    file.close()
    return test.text
def scelta():
    file = open("prova.txt", "w")
    a = input("inserisci la parola chiave")
    n = quantita()
    rq = requests.get("https://www.ansa.it")
    test = bs(rq.text, features="html.parser")
    test2 = test.findAll("h3", {"class": "news-title"})
    file = open("prova.txt", "w")
    for test in test2[:n]:
        i = test.text.find(a)
        if i != -1:
            print ("prova33")
            file.write(test.text)
            file.write("\n")
    file.close()
while True:
    print('''
        Inserire cosa fare:
        1) scegli e scrivi quante notizie vuoi di ansa.it
        2) scegliere una parola e vedere se è presente nelle prime 5 notizie di ansa.it
        3) uscire dal programma
    ''')
    a = input()
    if a == "1":
        scrivi()
    elif a == "2":
        scelta()
    elif a == "3":
        break

