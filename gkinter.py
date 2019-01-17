from tkinter import * 
import time

#La hauteur et la largeur auront -1 en résultat donc faites attention a ce que vous faites
#The width and heigth (pixel size) will have their size - 1, so be careful of what you're doing
pixelgh = 8
pixelgl = 6
pixelghd = pixelgh - 1
pixelgld = pixelgl - 1
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


#INITIALIZATION OF THE PROGRAM DO NOT TOUCH
#------------------------------------------
while pixelghd > drawh:
        while pixelgld > drawl:
            currentone = str(drawh) + "h" + str(drawl) + "l"
            print(currentone)
            exec('pixel_%s = Canvas(wdws, width=10, height=10, highlightthickness=0, background="white")' % currentone)
            #pixel[drawh + "h" + drawl + "l"] = Canvas(wdws, width=5, height=5, background='white')
            exec('pixel_%s.grid(row=drawh, column=drawl)' % currentone)
            print('pixel_%s' % currentone)
            #pixel[drawh + "h" + drawl + "l"].grid(row=drawh, column=drawl)
            drawl = drawl + 1
        drawl = 0
        drawh = drawh + 1
#------------------------------------------ END OF INITIALIZATION, YOU CAN TOUCH EVERYTHING AFTER THIS LINE

#Just to test it

updatepix(0, 0, "b")
updatepix(0, 1, "b")
        


wdws.mainloop()