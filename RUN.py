# -*- coding: UTF-8 -*-
# Python
from tkinter import Tk,Label
from ramadan import Ramadan,PostRamadan,EidAdha
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
from Settings import background,foreground,salahTitles,fontStyle,JummahTimes,BMA_logoLength,BMA_logoWidth,BMA_logoPositioningRelx,BMA_logoPositioningRely,x2,x1,x,y1,y,jummahXpos,jummahYpos,jummahTitleXpos,jummahTitleYpos,salahContainerFont,isRamadan
from datetime import datetime,date
from hijri_converter import Gregorian
import json
try:
    db = open('db.json')
    data = json.load(db)
    db.close()
    dateAndTime = data["dateAndTime"]
    time = dateAndTime['time']
    gDate = dateAndTime['gregorianDate']
    hDate = dateAndTime['hijriDate']
    announcementsData = data['announcements']
    countdown = data['countdown']
    salahCountdown = countdown['salah']
except:
    pass
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
sTimes = salahInfo.startTimes
timeChanges = salahInfo.tmrroStartTimes()
salahContinerframe =Frame(root,bg=background,height=root.winfo_screenheight()-150,width=root.winfo_screenwidth())
fajr = SalahContainer(salahContinerframe,"Fajr",salahInfo.get(0),sTimes[0],xpos=(x+0.1)-x2,ypos=y+0.70)
zuhr = SalahContainer(salahContinerframe,"Zuhr",salahInfo.get(1),sTimes[1],xpos=x+0.35-x1,ypos=y+0.5+y1)
asr = SalahContainer(salahContinerframe,"Asr",salahInfo.get(2),sTimes[2],xpos=x+0.5,ypos=y+0.25)
maghrib = SalahContainer(salahContinerframe,"Maghrib",salahInfo.get(3),sTimes[3],xpos=x+0.65+x1,ypos=y+0.5+y1)
isha = SalahContainer(salahContinerframe,"Isha",salahInfo.get(4),sTimes[4],xpos=(x+0.9)+x2,ypos=y+0.70)
salahLabels = [fajr,zuhr,asr,maghrib,isha]
Label(salahContinerframe,text="Jummah",font=(fontStyle,salahTitles),bg=background,fg=foreground).place(relx=jummahTitleXpos,rely=jummahTitleYpos,anchor='center')
Label(salahContinerframe,text=JummahTimes,font=(fontStyle,salahContainerFont),bg=background,fg=foreground).place(relx=jummahXpos,rely=jummahYpos,anchor='center')
baitulMamurLogo = Image.open("logo.png")
logo_pic = baitulMamurLogo.resize((BMA_logoWidth,BMA_logoLength),Image.Resampling.LANCZOS)
new_logo = ImageTk.PhotoImage(logo_pic)
Label(salahContinerframe,image=new_logo).place(relx=BMA_logoPositioningRelx,rely=BMA_logoPositioningRely,anchor='center')

s1 = Slide(root,
content="",
frame=salahContinerframe,
time=10
)

spaces = "    "
qrCode = ImageTk.PhotoImage(Image.open("images/BMA donate qr code.png").resize((890,890),Image.Resampling.LANCZOS))
s2 = Slide(root,
title="",
content=spaces+"Please Donate by\n"+spaces+"following the QR code\n\n\n"+spaces+"Or donate via the\n"+spaces+"charity box/card machine \n"+spaces+"at the entrance/exit",
contentFont=60,
image=qrCode
)
# s2 = Slide(root,
# title="Donations",
# content="Please donate to the masjid using the charity box or card machine near the entrance/exit\nor\nBy using online transfer\nOrganisation name: Baitul Mamur Academy\nAcc no. 31643290\nSort code: 40-01-18",
# contentFont=60
# )

hijri = Gregorian(int(datetime.now().year), datetime.now().month, datetime.now().day).to_hijri()

if hijri.month_name() =="Dhu al-Hijjah":
    if hijri.day <10 and hijri.day>3:
        eidJamaahSlide = Slide(root,title="EID JAMA'AH",content="1st Jama'ah: 7:00 AM\n\n2nd Jama'ah: 8:30 AM\n\n3rd Jama'ah: 10:00 AM",contentFont=100,bg='black')
if hijri.month_name() =="Ramadhan":
    ramadanDay = hijri.day
    ramadanDaySlide = Slide(root,title="Ramadan Day",content=ramadanDay,contentFont=450,titleFont=100)
    if ramadanDay >25:
        eidJamaahSlide = Slide(root,title="EID JAMA'AH",content="1st Jama'ah: 7:00 AM\n\n2nd Jama'ah: 8:30 AM\n\n3rd Jama'ah: 9:30 AM",contentFont=100,bg='black')
    if ramadanDay <= 12 and hijri.year == 1444:
        gatheringSlide = Slide(root, title="Iftaar gathering this monday",titleFont=100,content="On monday 3rd of April (12th Ramadan),\nBaitul Mamur Academy would like to invite you to an iftaar gathering,\nPlease come and bring your friends & family to this barakah filled event\nWe look forward to seeing you all\nInsha'Allah",contentFont=65)
# currentDate = datetime.now()
# d1 = date(currentDate.year,currentDate.month,currentDate.day)
# d2 = date(day=22,month=3,year=2023)
# daysTillRamadan = (d2-d1).days
# ramadanCountDownTitle= "Days until Ramadan"
# ramadanCountDownMsg = str(daysTillRamadan)
# ramadanCountDownContentFont =450
# ramadanCountDownTitleFont =100
# if(daysTillRamadan<1):
#     ramadanCountDownMsg = "Ramadan Mubarak"
#     ramadanCountDownTitle=""
#     ramadanCountDownContentFont =250
#     ramadanCountDownTitleFont =0
# s3 = Slide(root,title=ramadanCountDownTitle,content=ramadanCountDownMsg,contentFont=ramadanCountDownContentFont,titleFont=ramadanCountDownTitleFont,smallContent="Subject to moon sighting",smallContentFont=30)

if (hijri.month_name()=="Shawwal" and hijri.day ==1) or (hijri.month_name()=="Dhu al-Hijjah" and hijri.day==10):
    eidMubarakSlide = Slide(root,title="",content="Eid Mubarak",contentFont=250,smallContent="TaqabbalAllahu Minna Wa Minkum",smallContentFont=50)

# s3 = Slide(root,
# title="",
# content="",
# contentFont=60
# )
# s4 = Slide(root,
# title="",
# content="",
# contentFont=60
# )

# a = EidAdha(root,slideshow)
# p = PostRamadan(root,slideshow)
# if isRamadan:
r = Ramadan(slideshow,root)
# s3 = Slide(root,
# title="'Virtues Of Dhul-Hijjah'",
# content="""There are no days in the year more beloved to Allah swt than the first ten days of Dhul-Hijjah and the last ten nights of Ramadan, as they combine acts of worship in a way unlike any other time. The Prophet Pbuh said, 'There is no deed that is better in the sight of Allah or more greatly rewarded than a good deed done in the (first) ten days of Al-Adha'. It was asked, 'Not even Jihad for the sake of Allah?' The Prophet Pbuh replied, 'Not even Jihad for the sake of Allah, unless a man goes out himself for Jihad taking his wealth with him and does not come back with anything.' 
# [Al Bukhari]""",
# contentFont=46,
# time=15,
# bg="white",
# fg=background    
# )
# s4 = Slide(root,
# title="'Maximising Your Rewards'",  
# content="""The first ten days of Dhul Hijjah are almost upon us and we don’t want to miss out on a single blessing. Even if you are not going on Hajj, there’s plenty you can do to make the most of Dhul Hijjah at home.
# - Perform Dhikr & Takbeer 
# - Standing In Night Prayer
# - Fasting all 9 days especially Day Of Arafah
# - Make Sincere Repentance
# - Perform The Hajj Pilgrimage
# - Give A Prophetic Qurbani
# - Return to Book of Allah (Quran)
# - Give Sadaqah & Charity""",
# contentFont=43,
# wraplength=root.winfo_screenwidth()-100,
# time=15,
# bg="white",
# fg=background
# )

# s5 = Slide(root,
# title="EID JAMA'AH",
# content="1st Jama'ah: 7:00 AM\n\n2nd Jama'ah: 8:30 AM\n\n3rd Jama'ah: 9:30 AM",
# contentFont=100,
# bg='black',
# time=10
# )

s1.packSlide()
slideshow.addAll([s1])
normalSlides = []
imageSlides = []

try:
    slides = data['slides']
    basicSlides = slides['basic']
    nSlides = basicSlides['normalSlide']
    iSlides = basicSlides['imageSlide']
    if(not (isinstance(nSlides,str))):
        for i in range(len(nSlides)):
            normalSlides.append([Slide(root,
        title=nSlides[i]['title'],
        titleFont=45+(nSlides[i]['font']['textFactor']*5),
        content=nSlides[i]['text'],
        contentFont=35+(nSlides[i]['font']['textFactor']*5),
        bg=nSlides[i]['colour']['slide'],
        time=nSlides[i]['displayTime'],
        fg=nSlides[i]['colour']['text'],
        titleFg=nSlides[i]['colour']['title'],
        ),nSlides[i]['order']])
    if(not (isinstance(iSlides,str))):
        for i in range(len(iSlides)):
            maxImgWidth=1900
            maxImgHeight=870
            if iSlides[i]['title'] !="":
                maxImgHeight=780
            try:
                openedImage = Image.open("images/downloadedImages/"+iSlides[i]['imageName'])
            except:
                openedImage = Image.open("images/noImgFound.png")
            width, height = openedImage.size
            imgWidth = round((width/height)*maxImgHeight)
            imgHeight = maxImgHeight
            if imgWidth>maxImgWidth:
                imgWidth=maxImgWidth
                imgHeight=round((height/width)*maxImgWidth)
            image = ImageTk.PhotoImage(openedImage.resize((imgWidth,imgHeight),Image.Resampling.LANCZOS))
            imageSlides.append([Slide(root,None,
        image=image,
        title=iSlides[i]['title'],
        bg=iSlides[i]['colour']['slide'],
        time=iSlides[i]['displayTime'],
        titleFont=45+(iSlides[i]['font']['titleFactor']*5),
        titleFg=iSlides[i]['colour']['title']),
        iSlides[i]['order']])
except Exception as e:
    print("error",e)
    pass
allSlides = [None for _ in range(len(normalSlides)+len(imageSlides))]
for i in range(len(normalSlides)):
    allSlides[normalSlides[i][1]] = normalSlides[i][0]
for i in range(len(imageSlides)):
    allSlides[imageSlides[i][1]] = imageSlides[i][0]
slideshow.addAll(allSlides)
try:
    slideshow.add(gatheringSlide)
except:
    pass
try:
    slideshow.add(ramadanDaySlide)
except:
    pass
try:
    slideshow.add(eidJamaahSlide)
except:
    pass
try:
    slideshow.add(eidMubarakSlide)
except:
    pass
try:
    t = Timer(root,salahInfo.salahTimesObj,[f,slideshow],changes,announcements,timeChanges,salahLabels,r)
except:
    t = Timer(root,salahInfo.salahTimesObj,[f,slideshow],changes,announcements,timeChanges,salahLabels,None)
slideshow.redoTimes()
root.config(bg=background)
root.attributes('-fullscreen',True)
root.mainloop()
