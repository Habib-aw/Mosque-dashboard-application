from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class Bot:
	def __init__(self):
		self.lastDayOfYear = "31-Dec-"+str(datetime.now().year)[2:]
	def receiveTime(self):
		checking = self.checkTime()
		if not checking[0]:
			PATH = "chromedriver.exe"
			driver = webdriver.Chrome(PATH)
			wait = WebDriverWait(driver, 5)
			visible = EC.visibility_of_element_located
			driver.get("https://www.towerhamletsmosques.co.uk/baitulmamur/")	
			date = driver.find_element_by_xpath("//label[@id='selected']").get_attribute('innerHTML')
			if checking[1] == "":
				open("times.txt", "a").truncate(0)
			else:
				while date != checking[1]:
					print(date,checking[1])
					search = driver.find_element_by_id('next3')
					search.send_keys(Keys.RETURN)
					wait.until(visible((By.XPATH,"//label[@id='selected']")))
					date = driver.find_element_by_xpath("//label[@id='selected']").get_attribute('innerHTML')
				search = driver.find_element_by_id('next3')
				search.send_keys(Keys.RETURN)
			while date != self.lastDayOfYear:
				wait.until(visible((By.XPATH,"//tr[@id='fajr']//td[@class='prayer-jamaah']//span")))
				date = driver.find_element_by_xpath("//label[@id='selected']").get_attribute('innerHTML')
				if date[1:2] == "-":
					date = "0"+date
				fajr_time= driver.find_element_by_xpath("//tr[@id='fajr']//td[@class='prayer-jamaah']//span").get_attribute('innerHTML')
				zuhr_time=driver.find_element_by_xpath("//tr[@id='zuhr']//td[@class='prayer-jamaah']//span").get_attribute('innerHTML')
				asr_time=driver.find_element_by_xpath("//tr[@id='asr']//td[@class='prayer-jamaah']//span").get_attribute('innerHTML')
				maghrib_time=driver.find_element_by_xpath("//tr[@id='maghrib']//td[@class='prayer-jamaah']//span").get_attribute('innerHTML')
				isha_time=driver.find_element_by_xpath("//tr[@id='isha']//td[@class='prayer-jamaah']//span").get_attribute('innerHTML')
				with open("times.txt", "a+") as file:
						file.seek(0)
						data = file.read(100)
						if len(data) > 0:
							file.write("\n")
						file.write(date+","+"Fajr "+fajr_time+","+"Zuhr "+zuhr_time+","+"Asr "+asr_time+","+"Maghrib "+maghrib_time+","+"Isha "+isha_time)
						file.close()
				search = driver.find_element_by_id('next3')
				search.send_keys(Keys.RETURN)
			driver.quit()
			self.receiveTime()
		print("Times are upto date")


	def checkTime(self):
		day = timedelta(days=1)
		date = datetime.now()
		try:
			lines= open("times.txt", "r").readlines() # Possible problems -- times.txt may not exist
		except:
			return (False,"")
		if len(lines) == 0:
			return (False,"")
		for i in range(len(lines)):
			lookingAt = date.strftime("%d-%b-%y")
			if lookingAt == self.lastDayOfYear:
				return (True,"")
			if i == len(lines)-1 and lookingAt != self.lastDayOfYear: # checks that the last line of file is last day of year
				return (False,lookingAt)
			if lines[i][:9] != lookingAt: # checks that no days have been skipped
				return (False,lookingAt)
			date+=day
		return (True,"")
