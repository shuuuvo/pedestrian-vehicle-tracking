#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="black")

def function1():
    os.system("python pedestrian.py --conf config/config.json --input videos/example_01.mp4 --output output/persons01.avi")
    
def function2():
    os.system("python vehicle.py --conf config/config.json --input sample_data/cars.mp4 --output output/cars01.avi")
 
def function6():
	root.destroy()

#stting title for the window
root.title("Pedestrian Detection & Vehicle Speed Estimation")

#creating a text label
Label(root, text="Pedestrian Detection & Vehicle Speed Estimation \nUsing Deep Learning.",font=("times new roman",14),
	fg="white",bg="black",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Pedestrian Detection",font=("times new roman",11),
	bg="#2B2828",fg='green',command=function1).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Vehicle Speed Estimation",font=("times new roman",11),
	bg="#2B2828",fg='green',command=function2).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',11),
	bg="#2B2828",fg="red",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()