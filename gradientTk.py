import math
import time
from tkinter import Canvas
from typing import Literal
from gradify import Gradient , angleToPoint ,pointToAngle , AllColors , Coordinates,GradientCanvasObject
from tkinter import *

class GradientLine(Gradient):
    def __init__(self, canvas:Canvas,coords:tuple, colors=...,width=3, mode: Literal['rgb'] | Literal['hex'] = None,xwidth = 3) -> None:
        super().__init__(colors, mode)
        self.canvas = canvas
        self.dotlines = []
        self.dotlinescolors = []
        self.dotLineCoords = []
        self.dLIcoords = Coordinates(coords)
        self.coords = coords
        self.x1 = coords[0]
        self.y1 = coords[1]
        self.x2 = coords[2]
        self.y2 = coords[3]
        self.length = self.dLIcoords.__len__()
        self.width = width
        self.xwidth = xwidth
        self._createDotLinesCoords()
        self.dotlinescolors = self.MindMultiGradient(self.length)

    def __call__(self, coords:tuple = [], colors=[],width=3, mode: Literal['rgb'] | Literal['hex'] = None,xwidth = 3) -> None:
        if colors.__len__() >1:
            self.colors = colors
        if coords.__len__() >3:
            self.coords = coords
            self.dLIcoords = Coordinates(coords)
            self.length = self.dLIcoords.__len__()
            self.x1 = coords[0]
            self.y1 = coords[1]
            self.x2 = coords[2]
            self.y2 = coords[3]
        if width != 3:
            self.width = width
        if xwidth != 3:
            self.xwidth = xwidth
        super().__call__(self.colors, mode)
        self.delete()
        self.dotlines = []
        self.dotlinescolors = []
        self.dotLineCoords = []
        self._createDotLinesCoords()
        self.dotlinescolors = self.MindMultiGradient(self.length)


    
    def _createDotLinesCoords(self):
        for x1 , y1 in self.dLIcoords: 
            coord1 = list(angleToPoint(pointToAngle(self.x1,self.y1,self.x2,self.y2)+95,(x1,y1),self.width))
            # print((x1,y1,x2,y2),end='  -c-  ')
            self.dotLineCoords.append(coord1)


    def create(self):
        self.delete()
        for n,i in enumerate(self.dotLineCoords):
            self.dotlines.append(self.canvas.create_line(*i,fill=self.dotlinescolors[n],width=self.xwidth))
        ...
    def delete(self):
        if self.dotlines.__len__() > 1:
            for i in self.dotlines:
                self.canvas.delete(i)
        self.dotlines.clear()


class GradientCircle(GradientCanvasObject):
    def __init__(self, canvas: Canvas, coords: tuple[int, int], radius:int = 40, border: int = 10, colors: list[str] = ..., gradientMethod: Literal['MMG'] | Literal['DRMMG'] = 'MMG') -> None:
        self.radius = radius
        self.ccoords = coords
        super().__init__(canvas,[coords[0]-radius,coords[1]-radius,coords[0]+radius,coords[1]+radius], border, colors, gradientMethod, objectTag = 'circle')

    def __call__(self, coords: list = None,radius:int = None, border: int = None, colors: list = None):
        if radius:
            self.radius = radius
        if coords:
            self.ccoords = coords
        self.ccoords = [self.ccoords[0]-self.radius,self.ccoords[1]-self.radius,self.ccoords[0]+self.radius,self.ccoords[1]+self.radius]

        return super().__call__(self.ccoords, border, colors)
        
class GradientRec(GradientCanvasObject):
    def __init__(self, canvas: Canvas, coords: tuple[int, int, int, int], border: int, colors: list[str] = ..., gradientMethod: Literal['MMG'] | Literal['DRMMG'] = 'MMG') -> None:
        super().__init__(canvas, coords, border, colors, gradientMethod, objectTag = 'rectangle')

    def __call__(self, coords: list = None, border: int = None, colors: list = None):
        return super().__call__(coords, border, colors)

def main():
    root = Tk()
    
    canvas = Canvas(root,width=500,height=500,bg='black')
    canvas.pack(expand=True,fill='both')
    line1 = GradientLine(canvas,(-30,-30,500,500),colors=('black','cyan'),width=10)
    line1.create()
    space = 40
    line2 = GradientLine(canvas,(100,100,400,800),colors=('black','blue'),width=10)
    line2.create()
    circle = GradientCircle(canvas,(0,0),40,border=20,colors=['cyan','black'])
    # root.resizable(False,False)
    i = 90
    while True:
        time.sleep(0.01)
        pos = root.winfo_pointerxy()
        lx = (pos[0]-root.winfo_rootx())
        ly = (pos[1]-root.winfo_rooty())
        length = 200
        line1([int(v) for v in angleToPoint(i,(lx,ly),int(length/1.5))])
        line2([int(v) for v in angleToPoint(i*2,(lx,ly),length)])
        circle((lx,ly),radius=length)
        circle.create()
        i +=5
        if i >= 360:
            i = 0
        # print(i)
        line1.create()
        line2.create()
        root.update()
    root.mainloop()




if __name__ == '__main__':
    main()