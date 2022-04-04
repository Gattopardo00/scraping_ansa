import requests
from bs4 import BeautifulSoup as bs
def scrivi():
    file = open("prova.txt","w")
    rq = requests.get("https://www.ansa.it")
    test=bs(rq.text,features="html.parser")
    test2=test.findAll("h3",{"class":"news-title"})
    for test in test2[:5]:
        print(test.text)
        file.write(test.text)
        file.write("\n")
    file.close()
def scelta():
   print("ciao")
while True:
    print('''
        Inserire cosa fare:
        1) scrivere le prime 5 notizie di ansa.it
        2) scegliere una parola e vedere se è presente nelle prime 5 notizie di ansa.it
        3) uscire dal programma
    ''')
    a=input()
    if a == "1":
        scrivi()
    elif a == "2":
        scelta()
    elif a == "3":
        break

