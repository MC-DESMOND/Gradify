import time
from typing import Literal
from gradify import Gradient , angleToPoint ,pointToAngle , AllColors
from tkinter import *

class GradientLine(Gradient):
    def __init__(self, canvas:Canvas,coords:tuple, colors=...,width=3, mode: Literal['rgb'] | Literal['hex'] = None) -> None:
        super().__init__(colors, mode)
        self.canvas = canvas
        self.dotlines = []
        self.dotlinescolors = []
        self.dotLineCoords = []
        self.coords = coords
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.x2 = coords[2]
        self.y2 = coords[3]
        self.length = self.measureLine()
        self.width = width
        self.createDotLinesCoords()
        self.dotlinescolors = self.MindMultiGradient(self.length)

    def __call__(self, coords:tuple = [], colors=[],width=3, mode: Literal['rgb'] | Literal['hex'] = None) -> None:
        if colors.__len__() >1:
            self.colors = colors
        if coords.__len__() >3:
            self.coords = coords
            self.x1 = coords[0]
            self.y1 = coords[1]
            self.x2 = coords[2]
            self.y2 = coords[3]
        if width != 3:
            self.width = width
        super().__call__(self.colors, mode)
        self.delete()
        self.dotlines = []
        self.dotlinescolors = []
        self.dotLineCoords = []
        self.length = self.measureLine()
        self.createDotLinesCoords()
        self.dotlinescolors = self.MindMultiGradient(self.length)

    def measureLine(self):
        x1 = self.coords[0]
        y1 = self.coords[1]
        x2 = self.coords[2]
        y2 = self.coords[3]
        length = 0
        while x1 != x2 or y1 != y2:
            length += 1
            if x1 < x2:
                x1+=1
            elif x1 > x2:
                x1-=1
            if y1 < y2:
                y1+=1
            elif y1 > y2:
                y1-=1
        return length
    
    def createDotLinesCoords(self):
        x1 = self.coords[0]
        y1 = self.coords[1]
        x2 = self.coords[2]
        y2 = self.coords[3]
        length = 0
        while x1 != x2 or y1 != y2:
            
            if x1 < x2:
                x1+=1
            elif x1 > x2:
                x1-=1
            if y1 < y2:
                y1+=1
            elif y1 > y2:
                y1-=1
            
            coord1 = angleToPoint(pointToAngle(self.x1,self.y1,x2,y2)+90,(x1,y1),self.width)
            self.dotLineCoords.append(coord1)
            length += 1

    def create(self):
        self.delete()
        for n,i in enumerate(self.dotLineCoords):
            self.dotlines.append(self.canvas.create_line(*i,fill=self.dotlinescolors[n],width=2))
        ...
    def delete(self):
        if self.dotlines.__len__() > 1:
            for i in self.dotlines:
                self.canvas.delete(i)
        self.dotlines.clear()


def main():
    root = Tk()
    
    canvas = Canvas(root,width=500,height=500,bg='black')
    canvas.pack(expand=True,fill='both')
    line1 = GradientLine(canvas,(-30,-30,500,500),colors=('black','#00ffff'),width=500)
    line1.create()
    space = 40
    line2 = GradientLine(canvas,(500,500,-30,-30),colors=('black','#004848'),width=500)
    line2.create()
    root.resizable(False,False)
    colors = line1.MindMultiGradient(500,('blue','cyan','gold','cyan','blue'))
    c = 0
    while True:
        if c >= colors.__len__()-1:
            c = 0
        c += 1
        color = colors[c] , 'black'
        line1(colors=color)
        line2(colors=color[::-1])
        line2.create()
        line1.create()
        root.update()
        




if __name__ == '__main__':
    main()