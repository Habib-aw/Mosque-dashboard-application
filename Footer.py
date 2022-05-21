from datetime import datetime
from hijri_converter import Gregorian
from tkinter import Frame,Label
import schedule
from Settings import clockFont,dateFont, fontStyle,background,foreground
import os
class Footer:
    def __init__(self,root,slideshow):
        dates = getDates()
        self.r=root
        self.frame = Frame(root,width=root.winfo_screenwidth(),bg=foreground)
        self.frame1 = Frame(self.frame,width=root.winfo_screenwidth(),bg=foreground)
        self.frame2 = Frame(self.frame,width=root.winfo_screenwidth(),bg=background)
        self.clock = Label(self.frame2,font=(fontStyle,clockFont,"bold"),bg=background,fg=foreground)
        self.time = datetime.now().strftime('%I:%M:%S %p')
        self.gDate = Label(self.frame1,text=dates[0],font=(fontStyle,dateFont,"bold"),bg=foreground,fg=background)
        self.hDate = Label(self.frame1,text=dates[1],font=(fontStyle,dateFont,"bold"),bg=foreground,fg=background)
        self.split = Label(self.frame1,text=" | ",font=(fontStyle,dateFont,"bold"),bg=foreground,fg=background)
        self.packFooter()
        self.repeater()
        self.s=slideshow
        self.check = True
    def repeater(self):
        self.time = datetime.now().strftime('%I:%M:%S %p')
        self.clock.config(text=self.time)
        if self.time == "12:00:00 AM":
            os.system("sudo reboot")
        elif self.time == "12:42:40 PM":
            self.s.timerOn=True
            self.unpackFooter()
            if self.check:
                background1="#019900"
                foreground1="white"
                self.check=False
                self.r.config(bg=background1)
                Label(self.r,bg=background1,fg=foreground1,font=(fontStyle,156,"bold","underline"),text="Monsur Ali's Nikah").pack()
                Label(self.r,bg=background1,fg=foreground1,font=(fontStyle,80,"bold"),text="\nPlease remain patient and respect those who may be still praying.\nJazakumullahu Khairan",wraplength=1600).pack()
                Label(self.r,bg=background1,fg=foreground1,font=(fontStyle,85,"bold"),text="And We created you in pairs. [78:8]").pack(side="bottom")
        schedule.run_pending()
        self.clock.after(200,self.repeater)
    def updateDate(self):
        dates = getDates()
        self.gDate.config(text=dates[0])
        self.hDate.config(text=dates[1])
    def packFooter(self):
        self.frame.pack(side="bottom")
        self.frame1.pack(side="bottom")
        self.frame2.pack(side="top")
        self.frame2.tkraise()
        self.gDate.pack(side="left")
        self.split.pack(side="left")
        self.clock.pack(ipadx=1000)
        self.hDate.pack(side="left")
    def raiseFooter(self):
        self.frame.tkraise()
    def unpackFooter(self):
        self.frame.pack_forget()
def getDates():
    gregorianDate = datetime.now().strftime('%A, %d %B %Y')
    hijri = Gregorian(int(datetime.now().year), datetime.now().month, datetime.now().day).to_hijri()
    hijiriDate = hijri.day,hijri.month_name(),hijri.year,hijri.notation()
    return (gregorianDate,hijiriDate)
