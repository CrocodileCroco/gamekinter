from tkinter import * 
import time
from threading import Thread

#La hauteur et la largeur auront -1 en résultat donc faites attention a ce que vous faites
#The width and heigth (pixel size) will have their size - 1, so be careful of what you're doing
pixelgh = 64
pixelgl = 64
#(OBSOLETE)pixelghd = pixelgh - 1
#(OBSOLETE)pixelgld = pixelgl - 1
drawh = 0
drawl = 0

wdws = Tk()



#def initg():
#    global pixelgh
#    global pixelgl
#    global pixelghd
#    global pixelgld
#    global drawh
#    global drawl
#    while pixelghd > drawh:
#        while pixelgld > drawl:
#            currentone = str(drawh) + "h" + str(drawl) + "l"
#            print(currentone)
#            exec('pixel_%s = Canvas(wdws, width=30, height=30, background="white")' % currentone)
#            #pixel[drawh + "h" + drawl + "l"] = Canvas(wdws, width=5, height=5, background='white')
#            exec('pixel_%s.grid(row=drawh, column=drawl)' % currentone)
#            print('pixel_%s' % currentone)
#            #pixel[drawh + "h" + drawl + "l"].grid(row=drawh, column=drawl)
#            drawl = drawl + 1
#        drawl = 0
#        drawh = drawh + 1

            
def updatepix(upd, lfr, whiteorblack):
    if whiteorblack == "b":
        currentupd = str(upd) + "h" + str(lfr) + "l"
        exec('pixel_%s["background"] = "black"' % currentupd)
    if whiteorblack == "w":
        currentupd = str(upd) + "h" + str(lfr) + "l"
        exec('pixel_%s["background"] = "white"' % currentupd)

def clearpix(whiteorblack2):
    pixelglc = 0
    pixelghc = 0
    if whiteorblack2 == "b":
        while pixelghc != pixelgh:
            while pixelglc != pixelgl:
                currentupdc = str(pixelghc) + "h" + str(pixelglc) + "l"
                try:
                    exec('pixel_%s["background"] = "black"' % currentupdc)
                except:
                    pass
                pixelglc = pixelglc + 1
            pixelglc = 0
            pixelghc = pixelghc + 1
    if whiteorblack2 == "w":
        while pixelghc != pixelgh:
            while pixelglc != pixelgl:
                currentupdc = str(pixelghc) + "h" + str(pixelglc) + "l"
                try:
                    exec('pixel_%s["background"] = "white"' % currentupdc)
                except:
                    pass
                pixelglc = pixelglc + 1
            pixelglc = 0
            pixelghc = pixelghc + 1
        



#INITIALIZATION OF THE PROGRAM DO NOT TOUCH
#------------------------------------------
pixdict = {}
while drawh != pixelgh:
        while drawl != pixelgl:
            currentone = str(drawh) + "h" + str(drawl) + "l"
            print(currentone)
            exec('pixel_%s = Canvas(wdws, width=6, height=6, highlightthickness=0, background="white")' % currentone)
            #pixel[drawh + "h" + drawl + "l"] = Canvas(wdws, width=5, height=5, background='white')
            exec('pixel_%s.grid(row=drawh, column=drawl)' % currentone)
            print('pixel_%s' % currentone)
            #pixel[drawh + "h" + drawl + "l"].grid(row=drawh, column=drawl)
            drawl = drawl + 1
        drawl = 0
        drawh = drawh + 1
#------------------------------------------ END OF INITIALIZATION, YOU CAN TOUCH EVERYTHING AFTER THIS LINE

#Just to test it

def loadgame():

    time.sleep(1)
    
    updatepix(0, 0, "b")
    
    time.sleep(1)
    
    updatepix(0, 1, "b")
        
    time.sleep(1)    

    updatepix(0, 3, "b")

gamethread = Thread(target=loadgame)
loadbutton = Button(wdws, text="Start Game", command=gamethread.start)
ldbtrow = pixelgh + 2
ldbtcolmn = pixelgl + 2
loadbutton.grid(row=ldbtrow, column=ldbtcolmn)


wdws.mainloop()