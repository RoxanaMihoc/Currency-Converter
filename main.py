from tkinter import *
import requests
from bs4 import BeautifulSoup
import re

converter = Tk()
converter.title("Currency Converter")
converter.geometry("800x600")
converter.configure(background='#b8cadc')
photo = PhotoImage(file=r"C:\Users\Mihoc\OneDrive\Desktop\1.png")

def extractData():
    URL = "https://www.cursbnr.ro/"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')

    soup.prettify()

    table = soup.find('div', attrs={'class': 'table-responsive'})
    data_curs = table.find('th', attrs={'colspan': '2'}).text
    print("Data de astazi este: ", data_curs)
    table2 = table.find('tbody')
    data = []
    for row in table2.findAll('td', attrs={'class': "text-center"}):
        r1 = re.compile("[A-Z]")
        r2 = re.compile("[0-9].[0-9]")
        if r1.match(row.text):
            data.append(row.text)
        else:
            if r2.match(row.text):
                data.append(row.text)
    i = 2
    while i <= len(data):
        data[i] = 0
        data[i + 1] = 0
        i = i + 4

    for i in data:
        data.remove(0)
    i = 1
    while i <= len(data):
        data[i] = float(data[i])
        i = i + 2

    it = iter(data)
    DICT = dict(zip(it, it))
    return DICT, data_curs



def Conversie():
    price = Suma.get()
    answer1 = variable1.get()
    answer2 = variable2.get()
    if answer1!="RON" and answer2=="RON":
        DICT = data.get(answer1)
        converted = round(float(price)*float(DICT))
        Rezultat.insert(INSERT,"Prețul în ",INSERT,'RON',INSERT," = ",INSERT,converted)
        Rezultat.insert(END,'\n')
    if answer2!="RON" and answer1=="RON":
        DICT = data.get(answer2)
        converted = round(float(price)/float(DICT))
        Rezultat.insert(INSERT,"Prețul în ",INSERT,answer2,INSERT," = ",INSERT,converted)
        Rezultat.insert(END, '\n')
def clear_all():
    Suma.delete(0, END)
    Rezultat.delete(1.0, END)




if __name__ == "__main__":
    data,data_curs=extractData()
    nume = Label(converter, text="Convertor Valutar", font=("arial", 25, "bold"), fg="black",bg="#a884fb")
    nume.place(x=270, y=10)
    data_azi= Label(converter, text=data_curs, font=("arial", 20, "bold"), fg="black",bg="#a884fb")
    data_azi.place(x=340, y=58)
    data["RON"]=0




    Suma= Entry(converter, font=("arial", 20))
    Suma.place(x=260, y=120)
    text1 = Label(converter, text="Suma:", font = ("arial", 20, "bold"), fg ="black",bg="#8080ff")
    text1.place(x=140, y=120)

    Rezultat = Text(converter, height=2, width=42, font=("arial", 10, "bold"), bd=5)
    Rezultat.place(x=260, y=500)
    text2 = Label(converter, text="Rezultat:", font=("arial", 20, "bold"), fg="black", bg="#8080ff")
    text2.place(x=348, y=450)

    variable1 = StringVar(converter)
    variable1.set(None)
    variante_monede1 = OptionMenu(converter, variable1, *data)
    variante_monede1.place(x=310, y=180, width=200, height=42)
    text3 = Label(converter, text="Schimba din:", font=("arial", 19, "bold"), fg="black",bg="#8080ff")
    text3.place(x=100, y=180)

    variable2 = StringVar(converter)
    variable2.set(None)
    variante_monede2 = OptionMenu(converter, variable2, *data)
    variante_monede2.place(x=310, y=230, width=200, height=42)
    text4 = Label(converter, text="În:", font=("arial", 17, "bold"), fg="black", bg="#8080ff")
    text4.place(x=100, y=230)

    button1 = Button(converter, text="Convert", fg="black", font="arial", bg="powder blue", command=Conversie)
    button1.place(x=335, y=310, height=40, width=150)

    button2 = Button(converter, text="Clear", fg="black", font="arial", bg="light blue", command=clear_all)
    button2.place(x=335, y=350, height=40, width=150)

    converter.mainloop()
