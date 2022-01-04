from tkinter import *
import requests
from bs4 import BeautifulSoup
import re

converter = Tk()
converter.title("Currency Converter")
converter.geometry("800x600")
converter.configure(background='light blue')
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
        data[i] = 0;
        data[i + 1] = 0;
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
    return 0
def clear_all():
    return 0

if __name__ == "__main__":
    data,data_curs=extractData()
    nume = Label(converter, text="Convertor Valutar", font=("arial", 25, "bold"), fg="red")
    nume.place(x=250, y=10)
    data_azi= Label(converter, text=data_curs, font=("arial", 20, "bold"), fg="red")
    data_azi.place(x=310, y=58)
    data["RON"]=0




    Suma = Entry(converter, font=("arial", 20))
    Suma.place(x=250, y=120)
    text1 = Label(converter, text="Suma:", font = ("arial", 10, "bold"), fg ="red",bg="light blue")
    text1.place(x=180, y=120)

    Rezultat = Text(converter, height=2, width=42, font=("arial", 10, "bold"), bd=5)
    Rezultat.place(x=250, y=500)


    variable1 = StringVar(converter)
    variable1.set(None)
    variante_monede1 = OptionMenu(converter, variable1, *data)
    variante_monede1.place(x=290, y=170, width=200, height=40)
    text3 = Label(converter, text="Schimba din:", font=("arial", 10, "bold"), fg="red",bg="light blue")
    text3.place(x=140, y=180)

    variable2 = StringVar(converter)
    variable2.set(None)
    variante_monede2 = OptionMenu(converter, variable2, *data)
    variante_monede2.place(x=290, y=220, width=200, height=40)
    text4 = Label(converter, text="In:", font=("arial", 10, "bold"), fg="red", bg="light blue")
    text4.place(x=140, y=230)

    button1 = Button(converter, text="Convert", fg="black", font="arial", bg="powder blue", command=Conversie)
    button1.place(x=300, y=310, height=40, width=150)

    button2 = Button(converter, text="Clear", fg="black", font="arial", bg="light blue", command=clear_all)
    button2.place(x=300, y=350, height=40, width=150)




    converter.mainloop()