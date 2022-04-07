# -*- coding: UTF-8 -*-
# Python
from tkinter import Tk,Label
from ramadan import Ramadan
from PIL import ImageTk,Image
# Classes
from SalahContainer import *
from Slide import *
from SalahInfo import *
# from Bot import *
from Footer import *
from Slideshow import *

from salahTimer import Timer
# Other
from Settings import background,foreground,salahTitles,fontStyle,JummahTimes,BMA_logoLength,BMA_logoWidth,BMA_logoPositioningRelx,BMA_logoPositioningRely,x1,x,y1,y


root = Tk()
salahInfo= SalahInfo() ### updates times and receives time from file ###
# bot = Bot() ### checks times in website match that of file ####
# if not bot.checkTime()[0]:
#     bot.receiveTime()
#     s=SalahInfo()
tmrroData = salahInfo.checkAnnouncemennts()
changes = tmrroData[1]
announcements = tmrroData[0]
slideshow =Slideshow()
f =Footer(root)

salahContinerframe =Frame(root,bg=background,height=root.winfo_screenheight()-150,width=root.winfo_screenwidth())
Label(salahContinerframe,text=JummahTimes,font=(fontStyle,salahTitles),bg=background,fg=foreground).place(relx=0.5,rely=0.5,anchor='center')
fajr = SalahContainer(salahContinerframe,"Fajr",salahInfo.get(0),xpos=(x+0.15),ypos=y+0.70)
zuhr = SalahContainer(salahContinerframe,"Zuhr",salahInfo.get(1),xpos=x+0.35-x1,ypos=y+0.5+y1)
asr = SalahContainer(salahContinerframe,"Asr",salahInfo.get(2),xpos=x+0.5,ypos=y+0.25)
maghrib = SalahContainer(salahContinerframe,"Maghrib",salahInfo.get(3),xpos=x+0.65+x1,ypos=y+0.5+y1)
isha = SalahContainer(salahContinerframe,"Isha",salahInfo.get(4),xpos=(x+0.85),ypos=y+0.70)
salahLabels = [fajr,zuhr,asr,maghrib,isha]

baitulMamurLogo = Image.open("logo.png")
logo_pic = baitulMamurLogo.resize((BMA_logoWidth,BMA_logoLength),Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(logo_pic)
Label(salahContinerframe,image=new_logo).place(relx=BMA_logoPositioningRelx,rely=BMA_logoPositioningRely,anchor='center')

s1 = Slide(root,content="",frame=salahContinerframe,time=2)
s2 = Slide(root,title="Donations",content="Please donate to the masjid using the charity box or card machine near the entrance/exit\nor\nBy using online transfer\nOrganisation name: Baitul Mamur Academy\nAcc no. 31643290\nSort code: 40-01-18",contentFont=60)
s1.packSlide()
slideshow.addAll([s1,s2])	

r = Ramadan(slideshow,root)

t = Timer(root,salahInfo.salahTimesObj,[f,slideshow],changes,announcements,salahLabels,r)
slideshow.redoTimes()
root.config(bg=background)
root.attributes('-fullscreen',True)
root.mainloop()