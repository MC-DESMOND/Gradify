import time
from tkinter import Canvas
from typing import Literal
from gradify import (
        Gradient,
        angleToPoint,
        pointToAngle,
        RangeCoordinates,
    )
from tkinter import *


class GradientCanvasObject(Gradient):
    
    def __init__(self,
                 canvas : Canvas
                 ,coords: tuple[int , int,int,int],
                 spread : int,
                 colors : list[str] = ['cyan','black'],
                 gradientMethod : Literal['MMG','DRM'] = 'MMG',
                 objectTag: Literal['circle','rectangle','polygon','line'] = 'circle') -> None:
        """ 
        
This should used in tkinter Canvas to create Gradient lines and shapes
>>> grObj = GradientCanvasObject(coords=(100,100,100,200,400) # Origin coordinates
            ,spread=500, # Amount of gradient shape
            canvas=canvas, # Canvas 
            gradientMethod='MMG', # gradient method, i picked MMG ( MindMultiGradient )
            objectTag='c'
                        )

To create the gradient shapes
----------------------
>>> grObj(colors=('cyan','blue','green'))
>>> grObj.create()
To reconfigure the coordinates
----------------------
>>> grObj(coords=(x1,y1,x2,y2),colors=('cyan','blue','green'))
>>> grObj.create()
To delete the gradient
------------------
>>> grObj.delete()

        """
        super().__init__()
        self.__colorList = []
        self.__objectList = []
        self.__spread = spread
        self.__colors = colors
        self.__objectTag = objectTag.lower()
        self.__coords = coords
        self.__canvas = canvas
        
        self.variables = {}
        self.__objectDictCreate = {
            'line':self.__canvas.create_line,
            'l':self.__canvas.create_line,
            'circle':self.__canvas.create_oval,
            'c':self.__canvas.create_oval,
            'rectangle':self.__canvas.create_rectangle,
            'rec':self.__canvas.create_rectangle,
            'r':self.__canvas.create_rectangle,
            'polygon':self.__canvas.create_polygon,
            'poly':self.__canvas.create_polygon,
            'poygon':self.__canvas.create_polygon,
            'p':self.__canvas.create_polygon,
        }
        self.__gradientMethods = {
            'MMG': self.MindMultiGradient,
            'DRM': self.DoubleReveredMergedMindMultiGradient
        }
        self.__gradientMethod = self.__gradientMethods[gradientMethod]

    def __call__(self,coords:list = None,
                  spread : int = None ,
                  colors:list = None,
                  objectTag: Literal['circle','rectangle','polygon','line'] = None,
                  gradientMethod : Literal['MMG','DRM'] = None ):
        ''' reconfigue the object
        >>> grObj(coords=(x1,y1,x2,y2),colors=('cyan','blue','green'))
        >>> grObj.colors
        >>> ('cyan','blue','green')
        '''
        self.delete()
        if spread:
            self.__spread = spread
        if colors:
            self.__colors = colors
        if objectTag:
            self.__objectTag = objectTag.lower()
        if coords:
            self.__coords = coords
        if gradientMethod:
            self.__gradientMethod = gradientMethod
        pass

    def delete(self):
        """ 
To delete the gradient
------------------
>>> grObj.delete()

        """
        if self.__objectList.__len__() > 1:
            for i in self.__objectList:
                self.__canvas.delete(i)
            self.__objectList.clear()
            self.__colorList.clear()



    def create(self):
        """ 
        
To create the gradient shapes
----------------------
>>> grObj(colors=('cyan','blue','green'))
>>> grObj.create()
To reconfigure the coordinates
----------------------
>>> grObj(coords=(x1,y1,x2,y2),colors=('cyan','blue','green'))
>>> grObj.create()

        """
        
        self.delete()

        objectCreator = self.__objectDictCreate[self.__objectTag]
        self.__colorList = self.__gradientMethod(self.__spread,self.__colors)
        self.__coords = list(self.__coords)
        if self.__objectTag in 'polygon' and self.__objectTag not in 'line' :
            r = True
            for s in range(0,self.__coords.__len__()-1, 2):
                    if r:
                        self.__coords[s-1] -=self.__spread
                        self.__coords[s] +=self.__spread
                    else:
                        self.__coords[s-1] +=self.__spread
                        self.__coords[s] -=self.__spread
                    r = not r
            for i,o in enumerate(self.__colorList):
                r = True
                for s in range(0,self.__coords.__len__()-1, 2):
                        if r:
                            self.__coords[s-1] +=1
                            self.__coords[s] -=1
                        else:
                            self.__coords[s-1] -=1
                            self.__coords[s] +=1
                        r = not r
                self.__objectList.append(
                    objectCreator(*self.__coords,outline = o,fill = None,width =2,)
                )
        else:
            for i,o in enumerate(self.__colorList):
                if self.__objectTag in 'line':
                    self.__coords[2] = self.__coords[2]+1
                    self.__coords[0] = self.__coords[0]+1
                    self.__objectList.append(
                        objectCreator(*self.__coords,fill = o)
                    )
                else:
                    
                    r = True
                    Dict = {}
                    for s in range(0,self.__coords.__len__()-1, 2):
                        if r:
                            self.__coords[s-1] +=1
                            self.__coords[s] -=1
                        else:
                            self.__coords[s-1] -=1
                            self.__coords[s] +=1
                        r = not r
                    
                    else:
                        self.__objectList.append(
                            objectCreator(*self.__coords,outline = o,width =2)
                        )



class GradientLine(Gradient):
    def __init__(self, canvas:Canvas,coords:tuple, colors=...,width=3, mode: Literal['rgb'] | Literal['hex'] = None,xwidth = 3) -> None:
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
        self.width = width
        self.xwidth = xwidth
        self._createDotLinesCoords()
        self.length = self.dLIcoords.__len__()

        self.dotlinescolors = self.MindMultiGradient(self.length)

    def __call__(self, coords:tuple = [], colors=[],width=3, mode: Literal['rgb'] | Literal['hex'] = None,xwidth = 3) -> None:
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
        if xwidth != 3:
            self.xwidth = xwidth
        super().__call__(self.colors, mode)
        self.delete()
        self.dotlines = []
        self.dotlinescolors = []
        self.dotLineCoords = []
        self._createDotLinesCoords()
        self.length = self.dLIcoords.__len__()
        self.dotlinescolors = self.MindMultiGradient(self.length)


    
    def _createDotLinesCoords(self):
        self.dLIcoords = RangeCoordinates(self.coords)
        for x1 , y1 in self.dLIcoords:
            w2 = int (self.width/2) 
            coord1 = list(angleToPoint(pointToAngle(self.x1,self.y1,self.x2,self.y2)+95,(x1,y1),w2))
            minus = lambda num1,num2 : int (num2-num1)
            coord1[0] = coord1[0]-minus(coord1[0],coord1[2])
            coord1[1] = coord1[1]-minus(coord1[1],coord1[3])
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
    '''
    
    '''
    def __init__(self, canvas: Canvas, coords: tuple[int, int], radius:int = 40, border: int = 10, colors: list[str] = ..., gradientMethod: Literal['MMG'] | Literal['DRM'] = 'MMG') -> None:
        self.radius = radius
        self.ccoords = coords
        super().__init__(canvas,[coords[0]-radius,coords[1]-radius,coords[0]+radius,coords[1]+radius], border, colors, gradientMethod, objectTag = 'circle')

    def __call__(self, coords: list = None,radius:int = None, border: int = None, colors: list = None,gradientMethod: Literal['MMG'] | Literal['DRM'] = None):
        if radius:
            self.radius = radius
        if coords:
            self.ccoords = coords
        self.ccoords = [self.ccoords[0]-self.radius,self.ccoords[1]-self.radius,self.ccoords[0]+self.radius,self.ccoords[1]+self.radius]

        return super().__call__(self.ccoords, border, colors,gradientMethod=gradientMethod)
        
class GradientRectangle(GradientCanvasObject):
    def __init__(self, canvas: Canvas, coords: tuple[int, int, int, int], border: int = 30, colors: list[str] = ..., gradientMethod: Literal['MMG'] | Literal['DRM'] = 'MMG') -> None:
        super().__init__(canvas, coords, border, colors, gradientMethod, objectTag = 'rectangle')

    def __call__(self, coords: list = None, border: int = None, colors: list = None,gradientMethod: Literal['MMG'] | Literal['DRM'] = None):
        return super().__call__(coords, border, colors,gradientMethod=gradientMethod)

def Example():
    root = Tk()
    canvas = Canvas(root,width=500,height=500,bg='black',highlightthickness=0)
    root.geometry(f'{int(canvas["width"])}x{canvas["height"]}')
    canvas.pack(expand=True,fill='both')
    sec = GradientLine(canvas,(-30,-30,500,500),colors=('black','cyan'),width=10)
    minute = GradientLine(canvas,(100,100,400,800),colors=('black','#00dddd'),width=10)
    hour = GradientLine(canvas,(100,100,400,800),colors=('black','#004C4c'),width=10)
    circle = GradientCircle(canvas,(0,0),40,border=30,gradientMethod='DRM',colors=['cyan','#004848','black'])
    # root.resizable(False,False)
    
    def loop():
        time.sleep(0.01)
        pos = root.winfo_pointerxy()
        canvas.config(width=int(root.winfo_width()),height=int(root.winfo_height()))
        lx = int(int(canvas['width'])/2)
        ly = int(int(canvas['height'])/2)
        # lx = (pos[0]-root.winfo_rootx())
        # ly = (pos[1]-root.winfo_rooty())
        length = 200
        seci = ((int(time.strftime('%S'))/60)*360)-90
        mini = ((int(time.strftime('%M'))/60)*360)-90
        hri = ((int(time.strftime('%H'))/12)*360)-90
        sec([int(v) for v in angleToPoint(seci,(lx,ly),length)])
        minute([int(v) for v in angleToPoint(mini,(lx,ly),length-20)])
        hour([int(v) for v in angleToPoint(hri,(lx,ly),int(length/1.5))])
        circle((lx,ly),radius=length,border=int(int(canvas['width'])/2))
        circle.create()
        sec.create()
        minute.create()
        hour.create()
        root.update()
        root.after(1,loop)
    loop()
    root.mainloop()




if __name__ == '__main__':
    Example()