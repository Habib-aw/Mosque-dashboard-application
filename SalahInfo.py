from datetime import datetime,timedelta
import re
from Settings import minsBeforeSalah
def toStrpDate(st):
    return datetime.strptime(st,"%d-%b-%y")
class SalahInfo:
	def __init__(self):
		self.lines = open("times.txt", "r").readlines()
		self.updateFile()
		self.salahTimes = None
		self.salahTimesObj = None
		self.getSalahs()
	def updateFile(self):
		if len(self.lines) != 0:
			while self.lines[0][:9] != datetime.now().strftime("%d-%b-%y"):
				open('times.txt', 'w').writelines(self.lines[1:])
				self.lines= open("times.txt", "r").readlines()
	def getSalahs(self):
		salahNames = ["Fajr","Zuhr","Asr","Maghrib","Isha"]
		if len(self.lines) != 0:
			self.salahTimes = re.findall("\d+:[0-9][0-9]", self.lines[0])
			self.salahTimesObj = objTime(self.salahTimes,subtractMin=minsBeforeSalah)
			for i in range(len(self.salahTimes)):
				self.salahTimes[i] = [salahNames[i],self.salahTimes[i]]
				self.salahTimesObj[i] = [salahNames[i],self.salahTimesObj[i]]
	def getO(self,i):
		return self.salahTimesObj[i][1].strftime("%I:%M:%S %p")
	def get(self,i):
		return self.salahTimes[i][1]
	def checkAnnouncemennts(self):
		announcements = []
		changes = []
		if len(self.lines)>=2:
			tmrroSalahs = re.findall("\d+:[0-9][0-9]", self.lines[1])
			for i in range(5):
				if self.salahTimes[i][1] !=tmrroSalahs[i]:
					changes.append([self.salahTimesObj[i][1],tmrroSalahs[i],i])
				if i == 0 and checkRamadan():
					continue
				if  i!=3:
					if self.salahTimes[i][1] !=tmrroSalahs[i]:
						announcements.append([i,tmrroSalahs[i]])
		return [announcements,changes]
def checkRamadan():
	rmd = open("ramadan.txt", "r").readlines()
	if rmd !=[]:
		RamadanTimes = [rmd[0].replace("\n","").split("|")]
		if toStrpDate(RamadanTimes[0][0])  <= toStrpDate(datetime.now().strftime("%d-%b-%y")) and toStrpDate(RamadanTimes[len(RamadanTimes)-1][0])>=toStrpDate(datetime.now().strftime("%d-%b-%y")):
			return True
	return False
def objTime(arr,addMin=0,subtractMin=0):
	newArr = arr.copy()
	newArr[0] += " AM"
	for i in range(1,len(arr)):
		newArr[i]+= " PM"
	for i in range(len(newArr)):
		newArr[i] = datetime.strptime(newArr[i],"%I:%M %p")+timedelta(minutes=addMin)-timedelta(minutes=subtractMin)
	return newArr
