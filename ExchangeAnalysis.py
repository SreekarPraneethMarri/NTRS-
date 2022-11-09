import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, mpld3
import seaborn as sns
from tkinter import *
from tkinter import messagebox
import datetime
from datetime import date

root=Tk()
variable1 = StringVar(root)
root.title("Currency Conversion Analysis")
root.geometry("500x450")

data = pd.read_csv("D:\\Amrita\\Programming\\Python\\NTRS\\Code\\Exchange.csv")
data.head()
df = data.iloc[:,[0,1]]

df['Date'] = pd.to_datetime(df['Date'])
df.info()
df = df.set_index('Date')
def home():
    global df
    f1=Frame(background='green')
    f1.place(x=0,y=0,width=500,height=650)

    u=Label(f1,text="WELCOME",font=("Helvetica",20))
    u.config(background='green',foreground="black")
    u.place(x=175,y=50)

    u1=Label(f1,text="!!Exchange Rate Analysis!!",font=("Helvetica",20))
    u1.config(background='green',foreground="black")
    u1.place(x=100,y=125)

    u2=Label(f1,text="From",font=("Helvetica",12))
    u2.config(background='green',foreground="black")
    u2.place(x=10,y=225)

    bfr=Button(f1,text="USD")
    bfr.place(x=10,y=250,width=85,height=40)

    u2=Label(f1,text="--->",font=("Helvetica",15))
    u2.config(background='green',foreground="black")
    u2.place(x=240,y=247)

    u2=Label(f1,text="<---",font=("Helvetica",15))
    u2.config(background='green',foreground="black")
    u2.place(x=240,y=265)

    u3=Label(f1,text="To",font=("Helvetica",12))
    u3.config(background='green',foreground="black")
    u3.place(x=470,y=225)

    CurrenyCode_list = ["DZD","AUD","BHD","VEF","BWP","BRL","BND","CAD","CLP","CNY","COP","CZK","DKK","EUR","HUF",
    "ISK","INR","IDR","IRR","ILS","JPY","KZT","KRW","KWD","LYD","MYR","MUR","MXN","NPR","NZD","NOK","OMR","PKR",
    "PEN","PHP","PLN","QAR","RUB","SAR","SGD","ZAR","LKR","SEK","CHF","THB","TTD","TND","AED","GBP","USD","UYU"]

    variable1.set("Select")

    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
    FromCurrency_option.place(x=405,y=250,width=85,height=40)

    u4=Label(f1,text="!!Select the option for which you want to visualize!!",font=("Helvetica",12))
    u4.config(background='green',foreground="black")
    u4.place(x=80,y=320)

    b1=Button(f1,text="Weekly",command=weekly, fg="black", activebackground = "grey")
    b1.place(x=20,y=375,width=100,height=40)
    b2=Button(f1,text="Monthly",command=monthly, fg="black", activebackground = "grey")
    b2.place(x=140,y=375,width=100,height=40)
    b3=Button(f1,text="Quarterly",command=quarterly, fg="black", activebackground = "grey")
    b3.place(x=260,y=375,width=100,height=40)
    b4=Button(f1,text="Annually",command=annually, fg="black", activebackground = "grey")
    b4.place(x=380,y=375,width=100,height=40)
    a = variable1.get()
    if a=="DZD":
        df = data.iloc[:,[0,1]]
    elif a=="AUD":
        df = data.iloc[:,[0,2]]
    elif a=="BHD":
        df = data.iloc[:,[0,3]]
    elif a=="VEF":
        df = data.iloc[:,[0,4]]
    elif a=="BWP":
        df = data.iloc[:,[0,5]]
    elif a=="BRL":
        df = data.iloc[:,[0,6]]
    elif a=="BND":
        df = data.iloc[:,[0,7]]
    elif a=="CAD":
        df = data.iloc[:,[0,8]]
    elif a=="CLP":
        df = data.iloc[:,[0,9]]
    elif a=="CNY":
        df = data.iloc[:,[0,10]]
    elif a=="COP":
        df = data.iloc[:,[0,11]]
    elif a=="CZK":
        df = data.iloc[:,[0,12]]
    elif a=="DKK":
        df = data.iloc[:,[0,13]]
    elif a=="EUR":
        df = data.iloc[:,[0,14]]
    elif a=="HUF":
        df = data.iloc[:,[0,15]]
    elif a=="ISK":
        df = data.iloc[:,[0,16]]
    elif a=="INR":
        df = data.iloc[:,[0,17]]
    elif a=="IDR":
        df = data.iloc[:,[0,18]]
    elif a=="IRR":
        df = data.iloc[:,[0,19]]
    elif a=="ILS":
        df = data.iloc[:,[0,20]]
    elif a=="JPY":
        df = data.iloc[:,[0,21]]
    elif a=="KZT":
        df = data.iloc[:,[0,22]]
    elif a=="KRW":
        df = data.iloc[:,[0,23]]
    elif a=="KWD":
        df = data.iloc[:,[0,24]]
    elif a=="LYD":
        df = data.iloc[:,[0,25]]
    elif a=="MYR":
        df = data.iloc[:,[0,26]]
    elif a=="MUR":
        df = data.iloc[:,[0,27]]
    elif a=="MXN":
        df = data.iloc[:,[0,28]]
    elif a=="NPR":
        df = data.iloc[:,[0,29]]
    elif a=="NZD":
        df = data.iloc[:,[0,30]]
    elif a=="NOK":
        df = data.iloc[:,[0,31]]
    elif a=="OMR":
        df = data.iloc[:,[0,32]]
    elif a=="PKR":
        df = data.iloc[:,[0,33]]
    elif a=="PEN":
        df = data.iloc[:,[0,34]]
    elif a=="PHP":
        df = data.iloc[:,[0,35]]
    elif a=="PLN":
        df = data.iloc[:,[0,36]]
    elif a=="QAR":
        df = data.iloc[:,[0,37]]
    elif a=="RUB":
        df = data.iloc[:,[0,38]]
    elif a=="SAR":
        df = data.iloc[:,[0,39]]
    elif a=="SGD":
        df = data.iloc[:,[0,40]]
    elif a=="ZAR":
        df = data.iloc[:,[0,41]]
    elif a=="LKR":
        df = data.iloc[:,[0,42]]
    elif a=="SEK":
        df = data.iloc[:,[0,43]]
    elif a=="CHF":
        df = data.iloc[:,[0,44]]
    elif a=="THB":
        df = data.iloc[:,[0,45]]
    elif a=="TTD":
        df = data.iloc[:,[0,46]]
    elif a=="TND":
        df = data.iloc[:,[0,47]]
    elif a=="AED":
        df = data.iloc[:,[0,48]]
    elif a=="GBP":
        df = data.iloc[:,[0,49]]
    elif a=="USD":
        df = data.iloc[:,[0,50]]
    elif a=="UYU":
        df = data.iloc[:,[0,51]]
def weekly():

    def checkpred():
        startyearinitial = pr1.get()
        month = pr2.get()
        if startyearinitial>="2012" and startyearinitial<="2022":
            if month=="1":
                startweekfinal=startyearinitial+'-01-01'
                endweekfinal=startyearinitial+'-01-31'
            elif month =="2":
                if startyearinitial == "2012" or "2016" or "2020":
                    startweekfinal=startyearinitial+'-02-01'
                    endweekfinal=startyearinitial+'-02-29'
                else:
                    startweekfinal=startyearinitial+'-02-01'
                    endweekfinal=startyearinitial+'-02-28'
            elif month =="3":
                startweekfinal=startyearinitial+'-03-01'
                endweekfinal=startyearinitial+'-03-31'
            elif month =="4":
                startweekfinal=startyearinitial+'-04-01'
                endweekfinal=startyearinitial+'-04-30'
            elif month =="5":
                startweekfinal=startyearinitial+'-05-01'
                endweekfinal=startyearinitial+'-05-31'
            elif month =="6":
                startweekfinal=startyearinitial+'-06-01'
                endweekfinal=startyearinitial+'-06-30'
            elif month =="7":
                startweekfinal=startyearinitial+'-07-01'
                endweekfinal=startyearinitial+'-07-31'
            elif month =="8":
                startweekfinal=startyearinitial+'-08-01'
                endweekfinal=startyearinitial+'-08-30'
            elif month =="9":
                startweekfinal=startyearinitial+'-09-01'
                endweekfinal=startyearinitial+'-09-30'
            elif month =="10":
                startweekfinal=startyearinitial+'-10-01'
                endweekfinal=startyearinitial+'-10-31'
            elif month =="11":
                startweekfinal=startyearinitial+'-11-01'
                endweekfinal=startyearinitial+'-11-30'
            elif month =="12":
                startweekfinal=startyearinitial+'-12-01'
                endweekfinal=startyearinitial+'-12-31'
            else:
                print("!!Invalid Month!!")
            dataframeweek = df[startweekfinal:endweekfinal]
            dataframeweek.min()
            dataframeweek.max()
            dataframeweek.plot()
            plt.show()

    f2=Frame(background='LightGoldenrod1')
    f2.place(x=0,y=0,width=500,height=650)

    u=Label(f2,text="!!Weekly Analysis!!",font=("Helvetica",20))
    u.config(background='LightGoldenrod1',foreground="black")
    u.place(x=125,y=25)

    u1=Label(f2,text="Year: ",font=("Helvetica",14))
    u1.place(x=100,y=110)
    pr1=Entry(f2,font=("Quintessential",14))
    pr1.place(x=225,y=110,width=150)

    u2=Label(f2,text="Month (In No): ",font=("Helvetica",14))
    u2.place(x=100,y=150)
    pr2=Entry(f2,font=("Quintessential",14))
    pr2.place(x=225,y=150,width=150)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=0,y=0,width=20,height=20)
    b3=Button(f2,text="Analyze",command=checkpred)
    b3.place(x=200,y=200,width=100,height=40)
    

def quarterly():

    def checkpred():
        orpred = pr1.get()
        dapred = pr2.get()
        if orpred>="2012" and orpred<="2022":
            if dapred==1:
                startmonthfinal=orpred+'-01-01'
                endmonthfinal=orpred+'-03-31'
            elif dapred==2:
                startmonthfinal=orpred+'-04-01'
                endmonthfinal=orpred+'-06-30'
            elif dapred==3:
                startmonthfinal=orpred+'-07-01'
                endmonthfinal=orpred+'-09-30'
            elif dapred==4:
                startmonthfinal=orpred+'-10-01'
                endmonthfinal=orpred+'-12-31'
            else:
                print("!!Invalid Quarter!!")
            startmonthfinal=orpred+'-10-01'
            endmonthfinal=orpred+'-12-31'
            dataframequarter = df[startmonthfinal:endmonthfinal]
            dataframequarter.min()
            dataframequarter.max()
            dataframequarter.plot()
            plt.show()

    f2=Frame(background='IndianRed1')
    f2.place(x=0,y=0,width=500,height=650)

    u=Label(f2,text="!!Quarterly Analysis!!",font=("Helvetica",20))
    u.config(background='IndianRed1',foreground="black")
    u.place(x=125,y=25)

    u1=Label(f2,text="Year: ",font=("Helvetica",14))
    u1.place(x=100,y=110)
    pr1=Entry(f2,font=("Quintessential",14))
    pr1.place(x=225,y=110,width=150)

    u2=Label(f2,text="Quarter No: ",font=("Helvetica",14))
    u2.place(x=100,y=150)
    pr2=Entry(f2,font=("Quintessential",14))
    pr2.place(x=225,y=150,width=150)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=0,y=0,width=20,height=20)
    b3=Button(f2,text="Analyze",command=checkpred)
    b3.place(x=200,y=200,width=100,height=40)

def annually():

    def checkpred():
        orpred = pr1.get()
        dapred = pr2.get()
        if orpred>="2012" and dapred<="2022":
            startyearfinal=orpred+'-01-01'
            endyearfinal=dapred+'-12-31'
            dataframeyear = df[startyearfinal:endyearfinal]
            dataframeyear.min()
            dataframeyear.max()
            dataframeyear.plot()
            plt.show()

    f2=Frame(background='DeepSkyBlue2')
    f2.place(x=0,y=0,width=500,height=650)

    u=Label(f2,text="!!Annual Analysis!!",font=("Helvetica",20))
    u.config(background='DeepSkyBlue2',foreground="black")
    u.place(x=125,y=25)

    u1=Label(f2,text="Start Year: ",font=("Helvetica",14))
    u1.place(x=100,y=110)
    pr1=Entry(f2,font=("Quintessential",14))
    pr1.place(x=225,y=110,width=150)

    u2=Label(f2,text="Till Year: ",font=("Helvetica",14))
    u2.place(x=100,y=150)
    pr2=Entry(f2,font=("Quintessential",14))
    pr2.place(x=225,y=150,width=150)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=0,y=0,width=20,height=20)
    b3=Button(f2,text="Analyze",command=checkpred)
    b3.place(x=200,y=200,width=100,height=40)

def monthly():

    def checkpred():
        orpred = pr1.get()
        if orpred>="2012" and orpred<="2022":
            startmonthfinal=orpred+'-01-01'
            endmonthfinal=orpred+'-12-31'
            dataframemonth = df[startmonthfinal:endmonthfinal]
            dataframemonth.min()
            dataframemonth.max()
            dataframemonth.plot()
            plt.show()

    f2=Frame(background='seashell2')
    f2.place(x=0,y=0,width=500,height=650)

    u=Label(f2,text="!!Monthly Analysis!!",font=("Helvetica",20))
    u.config(background='seashell2',foreground="black")
    u.place(x=125,y=25)

    u1=Label(f2,text="Year: ",font=("Helvetica",14))
    u1.place(x=100,y=110)
    pr1=Entry(f2,font=("Quintessential",14))
    pr1.place(x=225,y=110,width=150)

    b2=Button(f2,text="<-",command=home)
    b2.place(x=0,y=0,width=20,height=20)
    b3=Button(f2,text="Analyze",command=checkpred)
    b3.place(x=200,y=200,width=100,height=40)

home()
root.mainloop()