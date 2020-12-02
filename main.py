from bs4 import BeautifulSoup as bs
from plyer import notification
import requests
import urllib
from tkinter import *
from tkinter.ttk import *

url = "https://www.worldometers.info/coronavirus/country/"

class Application:
    def __init__(self,cname):
        #print(cname)
        self.country = cname
        self.url =  url+self.country   #"https://www.worldometers.info/coronavirus/country/"

    def run(self):
        #print("Starting the script...\n \n")
        page = requests.get(self.url)
        data = self.scrapeData(page)
        return data
        
    def scrapeData(self,page):
        soup = bs(page.content,"html.parser")
        container = soup.find('div',class_="col-md-8")
        # print(container)
        containers = container.find_all(id="maincounter-wrap")
        # print(containers)
        listt =[self.country.upper()]
        for _ in containers:
            var = _.find('h1').get_text()
            rater = _.find('div',class_="maincounter-number")
            rate = rater.get_text().strip("\n")
            final = f"{var}{rate}"
            listt.append(final)
           # print(var)

        return listt

if __name__ == "__main__":
    icon = 'rk.ICO'
    def start(varf):
        start = Application(varf)
        data = start.run()
        stri =" \n"
        notification.notify(
        title=f"Quick  Corona Report for : {data[0]}",
        message = stri.join(data[1:]),
        timeout = 20,
        app_icon=icon)

    
## screens
    root = Tk()
    root.geometry("300x150")
    root.title("Corona Report")
    root.iconbitmap(icon)

    l1 = Label(root,text="**This is a corona report generator app**",background='#42f593', foreground='#f54248')#.place(x=20,y=20)
    l1.config(font=("Harlow Solid Italic",12))
    l1.pack()
    l2 = Label(root,text="Enter the name of country:").place(x=20,y=50)
    cname = Entry(root,width=30)
    cname.pack()
    # varf = cname.get()
    # # varf = "india"
    cname.place(x=20,y=70)
    btn = Button(root,text="Show Report",command=(lambda : start(cname.get())))
    btn.place(x=100,y=100)
    root.mainloop()