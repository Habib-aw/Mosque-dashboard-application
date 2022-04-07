from tkinter import Frame, Label, Canvas
from Settings import background,foreground,salahContainerFont,fontStyle,salahTitles,salahContainerFrameW,salahContainerFrameH,salahContainerCanvasH,salahContainerCanvasW,salahTitlesXpos,salahTitlesYpos,canvasXpos,canvasYpos,salahTimeXpos,salahTimeYpos,circleXpos,circleYpos,salahContainerCircleRadius


class SalahContainer:
	def __init__(self,frame,salahName, salahTime,xpos=0.5,ypos=0.5):
		self.salahName = salahName
		self.salahTime = salahTime
		self.frame = Frame(frame,width=salahContainerFrameW, height=salahContainerFrameH,bg=background)
		self.canvas = Canvas(self.frame, width=salahContainerCanvasW, height=salahContainerCanvasH, background=background,highlightthickness=0)
		Label(self.frame,text=self.salahName,bg=background,font=(fontStyle,salahTitles),fg=foreground).place(relx=salahTitlesXpos,rely=salahTitlesYpos,anchor='center')
		self.canvas.place(relx=canvasXpos,rely=canvasYpos,anchor='center')
		self.label = Label(self.canvas,text=self.salahTime,bg=foreground,font=(fontStyle,salahContainerFont),fg=background)
		self.label.place(relx=salahTimeXpos,rely=salahTimeYpos,anchor='center')
		create_circle(circleXpos,circleYpos,salahContainerCircleRadius,self.canvas)
		self.display(xpos=xpos,ypos=ypos)
	
	def display(self,xpos=0.5,ypos=0.5):
		self.frame.place(relx=xpos,rely=ypos)
	def changeBgColour(self):
		pass

	def updateSalahTimes(self):
		pass

	def salahChangeOccured(self):
		pass
def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=foreground,outline=foreground,width=2)