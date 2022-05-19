from datetime import timedelta,datetime,date
from tkinter import Label
import schedule
from Settings import background,foreground,fontStyle,salahIn2Font,salahIn2PaddingTop,salahIn2SpaceBetween,announcementContentFont,salahIn2Bg,phonSwitchFont,minsBeforeSalah
from Slide import Slide
from audioplayer import AudioPlayer

def toStrp(st):
    return datetime.strptime(st,"%I:%M:%S %p")

class Timer:
    def __init__(self,root,salahObj,Frames,changes,announcements,salahLabels,ramadan) -> None:
        self.root = root
        self.salahObj= salahObj
        self.nextSalah = None
        self.getNextSalah()
        self.countdown = Label(root,font=(fontStyle,salahIn2Font,"bold"),bg=salahIn2Bg,fg=foreground)
        self.counting = True
        self.phoneSwitch=Label(root,font=(fontStyle,phonSwitchFont,"bold"),text=salahIn2SpaceBetween+"Please switch off your mobile phones",bg=salahIn2Bg,fg=foreground)
        self.otherFrame = Frames
        self.changes = changes
        self.ramadan = ramadan
        self.announcements = announcements
        self.salahLabels = salahLabels
        self.timesChanged = False
        if announcements !=[]:
            self.sa = Slide(self.root,title="Announcements",content="",contentFont=announcementContentFont,fg="white",bg="red",paddingCtop=0,announce=True)
            self.otherFrame[1].add(self.sa)
        self.setAnnouncements()
        schedule.every(0.2).seconds.do(self.countingDown)
    def getNextSalah(self):
        arr = self.salahObj
        currentTime = toStrp(datetime.now().strftime("%I:%M:%S %p"))
        nextSalah = ""
        for j in range(len(arr)):
            if currentTime<arr[j][1]:
                if datetime.now().strftime("%A") == "Friday" and arr[j][0] == "Zuhr":
                    continue
                nextSalah=arr[j]
                break
        if not nextSalah:
            nextSalah=["Waiting to reboot\n\n\n\n\n\n\n\n\n",toStrp("11:59:00 PM")]
        self.nextSalah=nextSalah
    def countingDown(self):
        currentTime = datetime.now().strftime("%I:%M:%S %p")
        if self.nextSalah[1] <=toStrp(currentTime) and toStrp(currentTime)<=(self.nextSalah[1]+timedelta(minutes=minsBeforeSalah)):
            self.otherFrame[0].unpackFooter()
            self.otherFrame[1].setTimerOn(True)
            self.countdown.pack(ipady=salahIn2PaddingTop)
            self.root.config(bg=salahIn2Bg)
            self.phoneSwitch.pack()
            cDown = datetime.combine(date.min, (self.nextSalah[1]+timedelta(minutes=minsBeforeSalah)).time()) - datetime.combine(date.min, toStrp(currentTime).time())
            cDownVar = str(cDown).replace("0:0","")
            cDownVar = str(cDownVar).replace("0:","")
            if self.counting:
                self.countdown.config(text=self.nextSalah[0]+" salah in\n"+cDownVar)
                if cDownVar == "0":
                    self.phoneSwitch.pack_forget()
                    self.countdown.config(text="Please straighten the lines\nand\nfill in the gaps")
                    self.countdown.pack(ipady=500)
                    AudioPlayer("sounds/plane.mp3").play(block=True)
                    self.nextSalah[1] += timedelta(minutes=4)
                    self.counting =False
        elif toStrp(currentTime)>(self.nextSalah[1]+timedelta(minutes=minsBeforeSalah)):
            self.getNextSalah()
            self.phoneSwitch.pack_forget()
            self.countdown.pack_forget()
            self.otherFrame[0].packFooter()
            self.otherFrame[1].setTimerOn(False)
            self.counting=True
            self.timesChanged=False
            self.root.config(bg=background)
        else:
            self.phoneSwitch.pack_forget()
            if not self.timesChanged:
                for i in range(len(self.changes)):
                    if toStrp(currentTime) > self.changes[i][0]:
                        self.salahLabels[self.changes[i][2]].label.config(text=self.changes[i][1])
                        # if self.changes[i][2] == 0: 
                            #if self.ramadan.isRamadan():
                             #   self.ramadan.setSuhoor()
                              #  continue
                        if self.changes[i][2] == 3:
                            #if self.ramadan.isRamadan():
                            #    self.ramadan.setIftaar()
                            #    self.ramadan.changeDailyMessage()
                            continue
                        self.setAnnouncements(self.changes[i][2])
                self.timesChanged= True
    def setAnnouncements(self,whichSalah=-1):
        salahNames = ["Fajr","Zuhr","Asr","Maghrib","Isha"]
        if self.announcements != []:
            announcementscontent = "Insha'Allah\n"
            for i in range(len(self.announcements)):
                if self.announcements[i][0] <= whichSalah:
                    announcementscontent+=salahNames[self.announcements[i][0]]+" is now at "+self.announcements[i][1]+"\n"
                else:
                    announcementscontent+=salahNames[self.announcements[i][0]]+" salah will be changing to "+self.announcements[i][1]+" tommorow\n"
            self.sa.content.config(text=announcementscontent)
