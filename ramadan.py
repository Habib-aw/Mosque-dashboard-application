from Slide import Slide
from PIL import ImageTk,Image
from datetime import datetime
from Settings import SuhoorIftaarPaddingTop,SuhoorIftaarSpaceBetween,SuhoorIftaarTimeFont,DailyMessageImgLength,DailyMessageImgWidth

def toStrpDate(st):
    return datetime.strptime(st,"%d-%b-%y")

class Ramadan:
    def __init__(self,slideshow,root) -> None:
        self.filename = "ramadan.txt"
        self.lines = open(self.filename, "r",encoding="utf-8").readlines()
        self.getCorrectDate()
        self.RamadanTimes = [self.lines[i].replace("\n","").split("|") for i in range(len(self.lines))] 
        self.messages=self.RamadanTimes[0][3:]
        self.suhoor = "\nSuhoor Ends: "+self.RamadanTimes[0][1]
        self.iftaar = "Iftaar Starts: "+self.RamadanTimes[0][2]
        self.fastTimes = self.fastTimes = self.suhoor + SuhoorIftaarSpaceBetween + self.iftaar
        self.nextDayFasts = [None for _ in range(len(self.RamadanTimes)-1)];self.setNextDayFasts()
        self.Image= None;self.getDailyRamadanMessage()
        # Holds reference to other objects 
        self.slideshow = slideshow
        self.root = root
        DailyMessageImgWidthLocal=1500
        DailyMessageImgLengthLocal=770
        self.banglaImage = ImageTk.PhotoImage(Image.open("images/bangla.jpeg").resize((DailyMessageImgWidthLocal,DailyMessageImgLengthLocal),Image.ANTIALIAS))
        self.englishImage = ImageTk.PhotoImage(Image.open("images/noImgFound.png").resize((DailyMessageImgWidthLocal,DailyMessageImgLengthLocal),Image.ANTIALIAS))
        self.ramadanMessageE = Slide(self.root,None,image=self.englishImage,title="Daily message English")
        self.ramadanMessageB = Slide(self.root,None,image=self.banglaImage,title="Daily message Bangla")
        self.fastTimesSlide = Slide(self.root,self.fastTimes,contentFont=SuhoorIftaarTimeFont,paddingCtop=SuhoorIftaarPaddingTop)
        self.slideshow.add(self.fastTimesSlide)
        
        if True:
            self.slideshow.addAll([self.ramadanMessageE,self.ramadanMessageB])
    def setFastTimes(self):
        self.fastTimes = self.suhoor + SuhoorIftaarSpaceBetween + self.iftaar
        self.fastTimesSlide.content.config(text=self.fastTimes)
    def getDailyRamadanMessage(self):
        if self.isRamadan():
            if len(self.messages) == 1:
                try:
                    self.Image = ImageTk.PhotoImage(Image.open("images/"+self.messages[0]).resize((DailyMessageImgWidth,DailyMessageImgLength),Image.ANTIALIAS))
                except:
                    self.Image = ImageTk.PhotoImage(Image.open("images/noImgFound.png").resize((DailyMessageImgWidth,DailyMessageImgLength),Image.ANTIALIAS))

    def changeDailyMessage(self):
        try:
            self.newImage = ImageTk.PhotoImage(Image.open("images/"+self.nextDayFasts[2]).resize((DailyMessageImgWidth,DailyMessageImgLength),Image.ANTIALIAS))
            if self.nextDayFasts[2] !=None:
                self.ramadanMessage.imageLabel.config(image=self.newImage)
        except:
            self.newImage = ImageTk.PhotoImage(Image.open("images/noImgFound.png").resize((DailyMessageImgWidth,DailyMessageImgLength),Image.ANTIALIAS))


    def setNextDayFasts(self):
        if len(self.RamadanTimes) > 1:
            self.nextDayFasts = self.RamadanTimes[1][1:]
    def setSuhoor(self):
        if self.nextDayFasts[0] !=None:
            self.suhoor = "\nSuhoor Ends: "+self.nextDayFasts[0] 
            self.setFastTimes()
    def setIftaar(self):
        if self.nextDayFasts[1] !=None:
            self.iftaar = "Iftaar Starts: "+self.nextDayFasts[1] 
            self.setFastTimes()
    def getCorrectDate(self):
        if len(self.lines) != 0:
            while self.lines[0][:9] != datetime.now().strftime("%d-%b-%y"):
                open(self.filename, 'w',encoding="utf-8").writelines(self.lines[1:])
                self.lines= open(self.filename, "r",encoding="utf-8").readlines()
    def isRamadan(self):
        if self.lines == []:
            return False
        return toStrpDate(self.RamadanTimes[0][0])  <= toStrpDate(datetime.now().strftime("%d-%b-%y")) and toStrpDate(self.RamadanTimes[len(self.RamadanTimes)-1][0])>=toStrpDate(datetime.now().strftime("%d-%b-%y"))
class PostRamadan:
    def __init__(self,root,slideshow) -> None:
        multB=1
        multE=0.9
        self.postB = ImageTk.PhotoImage(Image.open("images/post-ramadan-bengali.jpeg").resize((round(1024*multB),round(768*multB)),Image.ANTIALIAS))
        self.postE= ImageTk.PhotoImage(Image.open("images/post-ramadan-english.jpeg").resize((round(1024*multE),round(855*multE)),Image.ANTIALIAS))
        post_R_E = Slide(root,None,title="Ramadan Reflection English",image=self.postE)
        post_R_B=Slide(root,None,title="Ramadan Reflection Bengali",image=self.postB)
        slideshow.addAll([post_R_E,post_R_B])
# # initialy for daily message
# if len(self.messages) == 2:
#     if len(imageIndex) == 2:
#         pass # means there is two images display them side by side with equal width and height
#     elif len(imageIndex) == 1:
#         pass # displays one image with text beside it - one picture on writing
# elif  len(self.messages) == 3:
#     if len(imageIndex) == 3:
#         pass # 3 images 1 on left 2 on right on top need to check for arabic for left side
#     elif len(imageIndex) == 2:
#         pass # 2 pictures one writing
#     elif len(imageIndex) == 1:
#         pass # 1 picture 2 writing
#     elif len(imageIndex) == 0:
#         pass # all writing
