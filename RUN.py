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
from Settings import background,foreground,salahTitles,fontStyle,JummahTimes,BMA_logoLength,BMA_logoWidth,BMA_logoPositioningRelx,BMA_logoPositioningRely,x2,x1,x,y1,y,jummahXpos,jummahYpos,jummahTitleXpos,jummahTitleYpos,salahContainerFont


root = Tk()
salahInfo= SalahInfo() ### updates times and receives time from file ###
# bot = Bot() ### checks times in website match that of file ####
# if not bot.checkTime()[0]:
#     bot.receiveTime()
#     s=SalahInfo()
tmrroData = salahInfo.checkAnnouncemennts()
changes = tmrroData[1]
announcements = tmrroData[0]
slideshow =Slideshow(root)
f =Footer(root)

salahContinerframe =Frame(root,bg=background,height=root.winfo_screenheight()-150,width=root.winfo_screenwidth())
fajr = SalahContainer(salahContinerframe,"Fajr",salahInfo.get(0),xpos=(x+0.1)-x2,ypos=y+0.70)
zuhr = SalahContainer(salahContinerframe,"Zuhr",salahInfo.get(1),xpos=x+0.35-x1,ypos=y+0.5+y1)
asr = SalahContainer(salahContinerframe,"Asr",salahInfo.get(2),xpos=x+0.5,ypos=y+0.25)
maghrib = SalahContainer(salahContinerframe,"Maghrib",salahInfo.get(3),xpos=x+0.65+x1,ypos=y+0.5+y1)
isha = SalahContainer(salahContinerframe,"Isha",salahInfo.get(4),xpos=(x+0.9)+x2,ypos=y+0.70)
salahLabels = [fajr,zuhr,asr,maghrib,isha]
Label(salahContinerframe,text="Jummah",font=(fontStyle,salahTitles),bg=background,fg=foreground).place(relx=jummahTitleXpos,rely=jummahTitleYpos,anchor='center')
Label(salahContinerframe,text=JummahTimes,font=(fontStyle,salahContainerFont),bg=background,fg=foreground).place(relx=jummahXpos,rely=jummahYpos,anchor='center')
baitulMamurLogo = Image.open("logo.png")
logo_pic = baitulMamurLogo.resize((BMA_logoWidth,BMA_logoLength),Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(logo_pic)
Label(salahContinerframe,image=new_logo).place(relx=BMA_logoPositioningRelx,rely=BMA_logoPositioningRely,anchor='center')

s1 = Slide(root,content="",frame=salahContinerframe,time=10)
s2 = Slide(root,title="Donations",content="Please donate to the masjid using the charity box or card machine near the entrance/exit\nor\nBy using online transfer\nOrganisation name: Baitul Mamur Academy\nAcc no. 31643290\nSort code: 40-01-18",contentFont=60)
s1.packSlide()
s3 = Slide(root,title="EID JAMA'AH",content="1st Jama'ah: 7:00 AM\n\n2nd Jama'ah: 8:30 AM\n\n3rd Jama'ah: 10:00 AM",contentFont=100,bg='black')

slideshow.addAll([s1,s2])	

r = Ramadan(slideshow,root)

t = Timer(root,salahInfo.salahTimesObj,[f,slideshow],changes,announcements,salahLabels,r)
slideshow.add(s3)
slideshow.redoTimes()
root.config(bg=background)
root.attributes('-fullscreen',True)
root.mainloop()
