
"""
DESDROID Inc. - Gradient Color Generation Module

This module provides functions for generating color gradients in Python.

**Features:**

* Create gradients between multiple colors.
* Specify colors in various formats (e.g., RGB, HEX, color names).
* Generate gradients with a specified amount of colors.

**Usage:**

```python
from gradify import Gradient

# Generate a linear gradient from cyan to blue to yellow with only an amount of 50 colors
length_of_gradient = 50
gradient_object:list = Gradient('cyan','blue','yellow')
gradient_colors = gradient_object.MindMultiGradient(
                        length_of_gradient
                        )
print(gradient_colors)

# there are still more, Explore
# Use the generated colors in your application...
#
#
#
```
"""



from tkinter import Canvas,Tk,BOTH # For the `GradientCanvasObject`
import math
from random import sample,choice
from typing import Literal
import numpy as np


AllColors = {'aliceblue': [240, 248, 255],
 'alienarmpit': [132, 222, 2],
 'alloyorange': [196, 98, 16],
 'amethyst': [100, 96, 154],
 'antiqueruby': [131, 34, 50],
 'antiquewhite': [250, 235, 215],
 'aqua': [0, 255, 255],
 'aquamarine': [127, 255, 212],
 'argentina': [116, 172, 223],
 'atomictangerine': [255, 153, 102],
 'aztecgold': [195, 153, 83],
 'azure': [240, 255, 255],
 "b'dazzledblue": [46, 88, 148],
 'babypowder': [254, 254, 250],
 'bahamas': [0, 119, 139],
 'banana': [255, 209, 42],
 'beige': [245, 245, 220],
 'belgium': [250, 224, 66],
 "bigdipo'ruby": [156, 37, 66],
 'bigfootfeet': [232, 142, 90],
 'bisque': [255, 228, 196],
 'bittersweetshimmer': [191, 79, 81],
 'black': [0, 0, 0],
 'blackshadows': [191, 175, 178],
 'blanchedalmond': [255, 235, 205],
 'blastoffbronze': [165, 113, 100],
 'blizzardblue': [80, 191, 230],
 'blue': [0, 0, 255],
 'blueberry': [79, 134, 247],
 'bluejeans': [93, 173, 236],
 'blueviolet': [138, 43, 226],
 'boogerbuster': [221, 226, 106],
 'brazil': [0, 155, 58],
 'brightyellow': [255, 170, 29],
 'brown': [165, 42, 42],
 'brownsugar': [175, 110, 77],
 'bubblegum': [255, 211, 248],
 'burlywood': [222, 184, 135],
 'burnishedbrown': [161, 122, 116],
 'cadetblue': [95, 158, 160],
 'cedarchest': [201, 90, 73],
 'ceruleanfrost': [109, 155, 195],
 'chartreuse': [127, 255, 0],
 'cherry': [218, 38, 71],
 'china': [222, 41, 16],
 'chocolate': [210, 105, 30],
 'cinnamonsatin': [205, 96, 126],
 'citrine': [147, 55, 9],
 'coconut': [254, 254, 254],
 'colombia': [252, 209, 22],
 'copper': [206, 137, 100],
 'copperpenny': [173, 111, 105],
 'coral': [255, 127, 80],
 'cornflowerblue': [100, 149, 237],
 'cornsilk': [255, 248, 220],
 'cosmiccobalt': [46, 45, 136],
 'crimson': [220, 20, 60],
 'cyan': [0, 255, 255],
 'cybergrape': [88, 66, 124],
 'daffodil': [255, 255, 49],
 'darkblue': [0, 0, 139],
 'darkcyan': [0, 139, 139],
 'darkgoldenrod': [184, 134, 11],
 'darkgray': [169, 169, 169],
 'darkgreen': [0, 100, 0],
 'darkgrey': [169, 169, 169],
 'darkkhaki': [189, 183, 107],
 'darkmagenta': [139, 0, 139],
 'darkolivegreen': [85, 107, 47],
 'darkorange': [255, 140, 0],
 'darkorchid': [153, 50, 204],
 'darkred': [139, 0, 0],
 'darksalmon': [233, 150, 122],
 'darkseagreen': [143, 188, 143],
 'darkslateblue': [72, 61, 139],
 'darkslategray': [47, 79, 79],
 'darkslategrey': [47, 79, 79],
 'darkturquoise': [0, 206, 209],
 'darkviolet': [148, 0, 211],
 'deeppink': [255, 20, 147],
 'deepskyblue': [0, 191, 255],
 'deepspacesparkle': [74, 100, 108],
 'denimblue': [34, 67, 182],
 'dimgray': [105, 105, 105],
 'dimgrey': [105, 105, 105],
 'dingydungeon': [197, 49, 81],
 'dirt': [183, 101, 3],
 'dodgerblue': [30, 144, 255],
 'eaglegreen': [25, 83, 95],
 'eerieblack': [27, 27, 27],
 'electriclime': [204, 255, 0],
 'emerald': [20, 169, 137],
 'eucalyptus': [68, 215, 168],
 'firebrick': [178, 34, 34],
 'floralwhite': [255, 250, 240],
 'forestgreen': [34, 139, 34],
 'freshair': [166, 231, 255],
 'fuchsia': [255, 0, 255],
 'gainsboro': [220, 220, 220],
 'gargoylegas': [255, 223, 70],
 'ghostwhite': [248, 248, 255],
 "giant'sclub": [176, 92, 82],
 'glossygrape': [171, 146, 179],
 'gold': [255, 215, 0],
 'goldenrod': [218, 165, 32],
 'goldfusion': [133, 117, 78],
 'granitegray': [103, 103, 103],
 'grape': [111, 45, 168],
 'gray': [128, 128, 128],
 'green': [0, 128, 0],
 'greenlizard': [167, 244, 50],
 'greensheen': [110, 174, 161],
 'greenyellow': [173, 255, 47],
 'grey': [128, 128, 128],
 'honeydew': [240, 255, 240],
 'hotmagenta': [255, 0, 204],
 'hotpink': [255, 105, 180],
 'illuminatingemerald': [49, 145, 119],
 'india': [255, 154, 48],
 'indianred': [205, 92, 92],
 'indigo': [75, 0, 130],
 'ireland': [255, 136, 62],
 'iris': [69, 74, 222],
 'ivory': [255, 255, 240],
 'jade': [70, 154, 132],
 'jasper': [208, 83, 64],
 'jellybean': [218, 97, 78],
 'keylime': [234, 242, 124],
 'khaki': [240, 230, 140],
 'lapislazuli': [67, 108, 185],
 'laserlemon': [255, 255, 102],
 'latvia': [158, 48, 57],
 'lavender': [230, 230, 250],
 'lavenderblush': [255, 240, 245],
 'lawngreen': [124, 252, 0],
 'leatherjacket': [37, 53, 41],
 'lemon': [255, 255, 56],
 'lemonchiffon': [255, 250, 205],
 'lichen': [113, 180, 141],
 'licorice': [26, 17, 16],
 'lightblue': [173, 216, 230],
 'lightcoral': [240, 128, 128],
 'lightcyan': [224, 255, 255],
 'lightgoldenrodyellow': [250, 250, 210],
 'lightgray': [211, 211, 211],
 'lightgreen': [144, 238, 144],
 'lightgrey': [211, 211, 211],
 'lightpink': [255, 182, 193],
 'lightsalmon': [255, 160, 122],
 'lightseagreen': [32, 178, 170],
 'lightskyblue': [135, 206, 250],
 'lightslategray': [119, 136, 153],
 'lightslategrey': [119, 136, 153],
 'lightsteelblue': [176, 196, 222],
 'lightyellow': [255, 255, 224],
 'lilac': [219, 145, 239],
 'lilacluster': [174, 152, 170],
 'lime': [0, 255, 0],
 'limegreen': [50, 205, 50],
 'linen': [250, 240, 230],
 'lumber': [255, 228, 205],
 'macau': [15, 117, 98],
 'madagascar': [252, 61, 50],
 'magenta': [255, 0, 255],
 'magicmint': [170, 240, 209],
 'magicpotion': [255, 68, 102],
 'malachite': [70, 148, 150],
 'maroon': [128, 0, 0],
 'mediumaquamarine': [102, 205, 170],
 'mediumblue': [0, 0, 205],
 'mediumorchid': [186, 85, 211],
 'mediumpurple': [147, 112, 219],
 'mediumseagreen': [60, 179, 113],
 'mediumslateblue': [123, 104, 238],
 'mediumspringgreen': [0, 250, 154],
 'mediumturquoise': [72, 209, 204],
 'mediumvioletred': [199, 21, 133],
 'metallicseaweed': [10, 126, 140],
 'metallicsunburst': [156, 124, 56],
 'midnightblue': [25, 25, 112],
 'mintcream': [245, 255, 250],
 'mistymoss': [187, 180, 119],
 'mistyrose': [255, 228, 225],
 'moccasin': [255, 228, 181],
 'moonstone': [58, 168, 193],
 "mummy'stomb": [130, 142, 132],
 'mysticmaroon': [173, 67, 121],
 'navajowhite': [255, 222, 173],
 'navy': [0, 0, 128],
 'neoncarrot': [255, 153, 51],
 'newcar': [33, 79, 198],
 'night': [11, 0, 51],
 'ogreodor': [253, 82, 64],
 'oldlace': [253, 245, 230],
 'olive': [128, 128, 0],
 'olivedrab': [107, 142, 35],
 'onyx': [53, 56, 57],
 'orange': [255, 165, 0],
 'orangered': [255, 69, 0],
 'orangesoda': [250, 91, 61],
 'orchid': [218, 112, 214],
 'outrageousorange': [255, 96, 55],
 'palau': [0, 153, 255],
 'palegoldenrod': [238, 232, 170],
 'palegreen': [152, 251, 152],
 'paleturquoise': [175, 238, 238],
 'palevioletred': [219, 112, 147],
 'panama': [218, 18, 26],
 'papayawhip': [255, 239, 213],
 'peach': [255, 208, 185],
 'peachpuff': [255, 218, 185],
 'pearlypurple': [183, 104, 162],
 'peridot': [171, 173, 72],
 'peru': [205, 133, 63],
 'pewterblue': [139, 168, 183],
 'pine': [69, 162, 125],
 'pink': [255, 192, 203],
 'pinkpearl': [176, 112, 128],
 'pixiepowder': [57, 18, 133],
 'plum': [221, 160, 221],
 'plumppurple': [89, 70, 178],
 'poison': [55, 0, 49],
 'polishedpine': [93, 164, 147],
 'powderblue': [176, 224, 230],
 'princessperfume': [255, 133, 207],
 'purple': [128, 0, 128],
 'purpleplum': [156, 81, 182],
 'quicksilver': [166, 166, 166],
 'radicalred': [255, 53, 94],
 'razzledazzlerose': [238, 52, 210],
 'razzmicberry': [141, 78, 133],
 'rebeccapurple': [102, 51, 153],
 'red': [255, 0, 0],
 'redsalsa': [253, 58, 74],
 'rose': [255, 80, 80],
 'rosedust': [158, 94, 111],
 'rosequartz': [189, 85, 156],
 'rosybrown': [188, 143, 143],
 'royalblue': [65, 105, 225],
 'ruby': [170, 64, 105],
 'rustyred': [218, 44, 67],
 'saddlebrown': [139, 69, 19],
 'salmon': [250, 128, 114],
 'sandybrown': [244, 164, 96],
 'sapphire': [45, 93, 161],
 'sasquatchsocks': [255, 70, 129],
 "screamin'green": [102, 255, 102],
 'seagreen': [46, 139, 87],
 'seaserpent': [75, 199, 207],
 'seashell': [255, 245, 238],
 'seychelles': [252, 216, 86],
 'shadowblue': [119, 139, 165],
 'shampoo': [255, 207, 241],
 'sheengreen': [143, 212, 0],
 'shimmeringblush': [217, 134, 149],
 'shinyshamrock': [95, 167, 120],
 'shockingpink': [255, 110, 255],
 'sienna': [160, 82, 45],
 'silver': [192, 192, 192],
 'sizzlingred': [255, 56, 85],
 'skyblue': [135, 206, 235],
 'slateblue': [106, 90, 205],
 'slategray': [112, 128, 144],
 'slategrey': [112, 128, 144],
 'slimygreen': [41, 150, 23],
 'smashedpumpkin': [255, 109, 58],
 'smoke': [115, 130, 118],
 'smokeytopaz': [131, 42, 13],
 'snow': [255, 250, 250],
 'soap': [206, 200, 239],
 'solomon': [33, 91, 51],
 'sonicsilver': [117, 117, 117],
 'southafrica': [0, 119, 73],
 'springgreen': [0, 255, 127],
 'steelblue': [70, 130, 180],
 'steelteal': [95, 138, 139],
 'strawberry': [252, 90, 141],
 'sugarplum': [145, 78, 117],
 'sunburntcyclops': [255, 64, 76],
 'sunglow': [255, 204, 51],
 'sweetbrown': [168, 55, 49],
 'tan': [210, 180, 140],
 'tartorange': [251, 77, 70],
 'teal': [0, 128, 128],
 'thistle': [216, 191, 216],
 "tiger'seye": [181, 105, 23],
 'tomato': [255, 99, 71],
 'tulip': [255, 135, 141],
 'turquoise': [64, 224, 208],
 'twilightlavender': [138, 73, 107],
 'usa': [60, 59, 110],
 'vanuatu': [210, 16, 52],
 'violet': [238, 130, 238],
 'wheat': [245, 222, 179],
 'white': [255, 255, 255],
 'whitesmoke': [245, 245, 245],
 'wildwatermelon': [253, 91, 120],
 'wintergreendream': [86, 136, 125],
 'winterwizard': [160, 230, 255],
 'yellow': [255, 255, 0],
 'yellowgreen': [154, 205, 50],
 'yellowsunshine': [255, 247, 0]}




def Coordinates(coords):
  
    """
    This function generates a list of coordinates representing a line segment
    from a starting point (start_x, start_y) to an ending point (end_x, end_y).

    Args:
        start_x: X-coordinate of the starting point.
        start_y: Y-coordinate of the starting point.
        end_x: X-coordinate of the ending point.
        end_y: Y-coordinate of the ending point.

    Returns:
        A list of tuples representing the (x, y) coordinates of the line segment.
    """
    start_x, start_y, end_x, end_y = coords
    # Calculate the change in x and y
    delta_x = end_x - start_x
    delta_y = end_y - start_y

    # Handle potential division by zero (straight line)
    if delta_x == 0:
        # Create a list of points with the same x-coordinate
        return [(start_x, y) for y in range(start_y, end_y + 1)]
    elif delta_y == 0:
        # Create a list of points with the same y-coordinate
        return [(x, start_y) for x in range(start_x, end_x + 1)]

    # Calculate the slope
    slope = delta_y / delta_x

    # Generate a list of x values from start_x to end_x
    x_vals = np.linspace(start_x, end_x, num=max(abs(delta_x), abs(delta_y)) + 1, dtype=int)

    # Calculate the corresponding y values using the slope
    y_vals = slope * (x_vals - start_x) + start_y

    # Combine x and y values into a list of coordinates
    coordinates = list(zip(x_vals, y_vals))

    return coordinates


def rgb2hex(rgb):
    """ 
Convert rgb values to hex.
>>> rgb2hex((234,123,150))
'#ea7b96'
    """
    hx = ''.join(["%02x" % int(c )
                for c in rgb])
    return f'#{hx}'

getRGBof = lambda name : AllColors.get(name.lower())
getHEXof = lambda name : rgb2hex(AllColors.get(name.lower()))





def hex2rgb(str_rgb):
    """
Convert hex or color names to rgb
>>> hex2rgb('#ea7b96')
(234, 123, 150)

Using color names
-----------------
>>> hex2rgb('navy')    
(0, 0, 128)

>>> hex2rgb('white') 
(255, 255, 255)

>>> hex2rgb('gold')  
(255, 215, 0)

>>> hex2rgb('purple') 
(128, 0, 128)

>>> hex2rgb('violet') 
(238, 130, 238)

    """

    if str_rgb.lower() in AllColors.keys():
        str_rgb = getHEXof(str_rgb)
    try:
        rgb = str_rgb[1:]
        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError("Invalid value %r provided for rgb color."
                        % str_rgb)
    return tuple([int(int(v, 16)) for v in (r, g, b)])



def pointToAngle(x1,y1,x2, y2):
    # Calculate the change in x and y
    dx = x2 - x1
    dy = y2 - y1

    # Use math.atan2 for accurate angle calculation (handles quadrants)
    radians = math.atan2(dy, dx)

    # Convert radians to degrees
    degrees = math.degrees(radians)

    # Handle negative angles (optional)
    if degrees < 0:
        degrees += 360  # Convert to positive angle between 0 and 360

    return degrees


def angleToPoint(angle, OriginPoint, length):
  """
Generate coordinates of a line using an `angle` `OriginPoint` and `length` 

>>> angleToPoint(60,(20,30),50)
(20, 30, -23.30127018922194, 50)

  """
  
  # Convert angle to radians
  angle = angle
  angle_radians = math.radians(angle)
  # Get original Point coordinates
  x1, y1 = OriginPoint
  # Calculate offsets based on angle and length
  x_offset = length * math.cos(angle_radians)
  y_offset = length * math.sin(angle_radians)
  # Calculate second point coordinates
  x2 = x1 + x_offset
  y2 = y1 + y_offset

  return (x1,y1,x2, y2)




class Gradient:

    def __init__(self,colors=[],mode:Literal['rgb','hex']=None) -> None:
        """ 
Generate a list of colors of either rgb or hex 
>>> gradient = Gradient()
>>> gradient.MindMultiGradient(20,'cyan','blue')
['#00f1ff', '#00e1ff', '#00d1ff', '#00c1ff', '#00b1ff', '#00a1ff', '#0091ff', '#0081ff', '#0071ff', '#0061ff', '#0051ff', '#0041ff', '#0031ff', '#0029ff', '#0021ff', '#0019ff', '#0011ff', '#0009ff', '#0001ff', '#0000ff']
>>> gradient.MindMultiGradient(50)               
['#00f9ff', '#00f1ff', '#00e9ff', '#00e1ff', '#00d9ff', '#00d1ff', '#00c9ff', '#00c1ff', '#00b9ff', '#00b1ff', '#00a9ff', '#00a1ff', '#0099ff', '#0091ff', '#0089ff', '#0085ff', '#0081ff', '#007dff', '#0079ff', '#0075ff', '#0071ff', '#006dff', '#0069ff', '#0065ff', '#0061ff', '#005dff', '#0059ff', '#0055ff', '#0051ff', '#004dff', '#0049ff', '#0045ff', '#0041ff', '#003dff', '#0039ff', '#0035ff', '#0031ff', '#002dff', '#0029ff', '#0025ff', '#0021ff', '#001dff', '#0019ff', '#0015ff', '#0011ff', '#000dff', '#0009ff', '#0005ff', '#0001ff', '#0000ff']
>>> gradient.colors
('cyan', 'blue')
>>> gradient.mode
hex
Fading from blue to cyan to blue
------------------
>>> colorlist = gradient.DoubleReveredMergedMindMultiGradient(40) 
>>> colorlist
['#0000ff', '#0001ff', '#0009ff', '#0011ff', '#0019ff', '#0021ff', '#0029ff', '#0031ff', '#0041ff', '#0051ff', '#0061ff', '#0071ff', '#0081ff', '#0091ff', '#00a1ff', '#00b1ff', '#00c1ff', '#00d1ff', '#00e1ff', '#00f1ff', '#00f1ff', '#00e1ff', '#00d1ff', '#00c1ff', '#00b1ff', '#00a1ff', '#0091ff', '#0081ff', '#0071ff', '#0061ff', '#0051ff', '#0041ff', '#0031ff', '#0029ff', '#0021ff', '#0019ff', '#0011ff', '#0009ff', '#0001ff', '#0000ff']

convert hex list to rgb list
----------------------------
>>> gradient.rgbFIYhexList(colorlist) 
[(0, 0, 255), (0, 1, 255), (0, 9, 255), (0, 17, 255), (0, 25, 255), (0, 33, 255), (0, 41, 255), (0, 49, 255), (0, 57, 255), (0, 65, 255), (0, 73, 255), (0, 81, 255), (0, 89, 255), (0, 97, 255), (0, 105, 255), (0, 113, 255), (0, 121, 255), (0, 129, 255), (0, 145, 255), (0, 161, 255), (0, 177, 255), (0, 193, 255), (0, 209, 255), (0, 225, 255), (0, 241, 255), (0, 241, 255), (0, 225, 255), (0, 209, 255), (0, 193, 255), (0, 177, 255), (0, 161, 255), (0, 145, 255), (0, 129, 255), (0, 121, 255), (0, 113, 255), (0, 105, 255), (0, 97, 255), (0, 89, 255), (0, 81, 255), (0, 73, 255), (0, 65, 255), (0, 57, 255), (0, 49, 255), (0, 41, 255), (0, 33, 255), (0, 25, 255), (0, 17, 255), (0, 9, 255), (0, 1, 255), (0, 0, 255)]    

        """
        self.colors = colors
        self.ColorlList =[]
        try:
            if not mode:
                match colors[0]:
                    case str():
                        self.mode = 'hex'
                    case _:
                        self.mode = 'rgb'
        except IndexError:
            self.mode = 'hex'
        
        self.MaxPower = 255
        self.FLOAT_ERROR = 0.0000005




    def __call__(self,colors,mode:Literal['rgb','hex']=None) -> None:
        """ Reconfigure colors and mode (rgb or hex)"""
        self.colors = colors
        self.ColorlList =[]
        try:
            if not mode:
                match colors[0]:
                    case str():
                        self.mode = 'hex'
                    case _:
                        self.mode = 'rgb'
        except IndexError:
            pass



    def _gradient( self, color1,color2)-> list:
        self.MaxPower = 255
        if self.mode.upper() == 'HEX':

            rcolor1 = [i for i in hex2rgb(color1)]
            rcolor2 = [i for i in hex2rgb(color2)]
        else:
            rcolor1 = [i for i in color1]
            rcolor2 = [i for i in color2]

        rgblist = []
        if self.mode.upper() == 'HEX':
            rgblist.append(rgb2hex([i for i in rcolor1]))
        else:
            rgblist.append([i for i in rcolor1])
        while rcolor1 != rcolor2:
            for i,o in enumerate(rcolor1):
                if rcolor1[i] < rcolor2[i]:
                    rcolor1[i] = rcolor1[i]+1
                elif rcolor1[i] > rcolor2[i]:
                    rcolor1[i] = rcolor1[i]-1
            if self.mode.upper() == 'HEX':
                rgblist.append(rgb2hex([i for i in rcolor1]))
            else:
                rgblist.append([i for i in rcolor1])
        return rgblist
    


    def _MultiGradient(self,COLORS = [])-> list:

        COLORS = self.colors if COLORS.__len__() < 1 else COLORS
        fade = []
        match COLORS[0]:
            case str():
                self.mode = 'hex'
                fade.append(rgb2hex(hex2rgb(COLORS[0])))
            case _:
                self.mode = 'rgb'
                fade.append(COLORS[0])
        
        for i in range(COLORS.__len__()):
            if i !=0:
                fade.extend(self._gradient(fade[fade.__len__()-1],COLORS[i]))
        self.colors = COLORS
        return fade



    def MindMultiGradient(self,lengthOfList:int = 0,COLORS = [])-> list:
        """ 
Generate a list of `lengthOfList` colors
>>> gradient.MindMultiGradient(20,'cyan','blue')
['#00f1ff', '#00e1ff', '#00d1ff', '#00c1ff', '#00b1ff', '#00a1ff', '#0091ff', '#0081ff', '#0071ff', '#0061ff', '#0051ff', '#0041ff', '#0031ff', '#0029ff', '#0021ff', '#0019ff', '#0011ff', '#0009ff', '#0001ff', '#0000ff']
>>> gradient.MindMultiGradient(50)               
['#00f9ff', '#00f1ff', '#00e9ff', '#00e1ff', '#00d9ff', '#00d1ff', '#00c9ff', '#00c1ff', '#00b9ff', '#00b1ff', '#00a9ff', '#00a1ff', '#0099ff', '#0091ff', '#0089ff', '#0085ff', '#0081ff', '#007dff', '#0079ff', '#0075ff', '#0071ff', '#006dff', '#0069ff', '#0065ff', '#0061ff', '#005dff', '#0059ff', '#0055ff', '#0051ff', '#004dff', '#0049ff', '#0045ff', '#0041ff', '#003dff', '#0039ff', '#0035ff', '#0031ff', '#002dff', '#0029ff', '#0025ff', '#0021ff', '#001dff', '#0019ff', '#0015ff', '#0011ff', '#000dff', '#0009ff', '#0005ff', '#0001ff', '#0000ff']

        """
        COLORS = self.colors if COLORS.__len__() < 1 else COLORS
        match COLORS[0]:
            case str():
                self.mode = 'hex'
            case _:
                self.mode = 'rgb'
        """ lengthOfList: numbers of colors in that list"""
        grad = [i for i in self._MultiGradient(COLORS)]
        length = grad.__len__()
        fil = []
        if lengthOfList !=0:
            if lengthOfList < 0:
                lengthOfList = 0
            f = True
            while grad.__len__() != lengthOfList:
                if lengthOfList > grad.__len__():
                    for i in range(0,(grad.__len__())*2,2):
                        grad.insert(i,grad[i])
                else:
                    fw = 0
                    bw = 0
                    r = 0
                    while lengthOfList < grad.__len__():
                                    
                        if r >= grad.__len__()-1:
                            r = 0
                        if f:
                            grad.remove(grad[int(fw-r)])
                            f = False
                        else:
                            grad.remove(grad[int(bw+r)])
                            f = True
                        r = r+1



        self.colors = COLORS
        
        return grad



    def DoubleReveredMergedMindMultiGradient(self,lengthOfList ,COLORS) -> list:
        """ 
Fading from blue to cyan to blue.
It runs the `MindMultiGradient` with half of `lengthOfList`.
The returned list is extended with a revered version of it self

>>> gradient.DoubleReveredMergedMindMultiGradient(40,'cyan','blue') 
['#0000ff', '#0001ff', '#0009ff', '#0011ff', '#0019ff', '#0021ff', '#0029ff', '#0031ff', '#0041ff', '#0051ff', '#0061ff', '#0071ff', '#0081ff', '#0091ff', '#00a1ff', '#00b1ff', '#00c1ff', '#00d1ff', '#00e1ff', '#00f1ff', '#00f1ff', '#00e1ff', '#00d1ff', '#00c1ff', '#00b1ff', '#00a1ff', '#0091ff', '#0081ff', '#0071ff', '#0061ff', '#0051ff', '#0041ff', '#0031ff', '#0029ff', '#0021ff', '#0019ff', '#0011ff', '#0009ff', '#0001ff', '#0000ff']

        """
        COLORS = self.colors if COLORS.__len__() < 1 else COLORS
        match COLORS[0]:
            case str():
                self.mode = 'hex'
            case _:
                self.mode = 'rgb'
        spread = self.MindMultiGradient(int(lengthOfList/2),COLORS)[::-1]
        spread.extend(spread[::-1])
        self.colors = COLORS
        return spread
    


    def rgbFIYhexList(self ,HEXlist)-> list[tuple]:
        """ Convert a hex list to an rgb list"""
        try:
            fil = [hex2rgb(i) for i in HEXlist]
        except:
            fil = HEXlist
        return fil
    

    
    def hexFIYrgbList(self ,RGBlist) -> list[str]:
        """ Convert a rgb list to a hex list"""
        try:
            fil = [rgb2hex(i) for i in fil]
        except:
            fil = RGBlist
        return fil


class GradientCanvasObject:
    
    def __init__(self,
                 canvas : Canvas
                 ,coords: tuple[int , int,int,int],
                 spread : int,
                 colors : list[str] = ['cyan','black'],
                 gradientMethod : Literal['MMG','DRMMG'] = 'MMG',
                 objectTag: Literal['circle','rectangle','polygon','line'] = 'circle') -> None:
        """ 
        
This is used in tkinter Canvas to create Gradient lines and shapes
>>> grObj = GradientCanvasObject(coords=(100,100,100,200,400) # Origin coordinates
            ,spread=500, # Amount of gradient shape
            canvas=canvas, # Canvas 
            gradientMethod='MMG', # gradient method, i picked MMG ( MindMultiGradient )
            objectTag='c'
                        )

To create the gradient shapes
----------------------
>>> grObj.create(colors=('cyan','blue','green'))

To reconfigure the coordinates
----------------------
>>> grObj.create(coords=(x1,y1,x2,y2),colors=('cyan','blue','green'))

To delete the gradient
------------------
>>> grObj.delete()

        """
        self.__colorList = []
        self.__objectList = []
        self.__spread = spread
        self.__colors = colors
        self.__objectTag = objectTag.lower()
        self.__coords = coords
        self.__canvas = canvas
        self.__gradient = Gradient()
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
            'MMG': self.__gradient.MindMultiGradient,
            'DRMMG': self.__gradient.DoubleReveredMergedMindMultiGradient
        }
        self.__gradientMethod = self.__gradientMethods[gradientMethod]

    def __call__(self,coords:list = None, spread : int = None ,colors:list = None,objectTag: Literal['circle','rectangle','polygon','line'] = None ):
        self.delete()
        if spread:
            self.__spread = spread
        if colors:
            self.__colors = colors
        if objectTag:
            self.__objectTag = objectTag.lower()
        if coords:
            self.__coords = coords
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



    def create(self,colors: list[str] = None,
                 coords: tuple[int , int,int,int] = None,
                 spread : int = None,
                 gradientMethod : str = None,
                 objectTag: Literal['circle','rectangle','polygon','line'] = None
                 ):
        """ 
        
To create the gradient shapes
----------------------
>>> grObj.create(colors=('cyan','blue','green'))

To reconfigure the coordinates
----------------------
>>> grObj.create(coords=(x1,y1,x2,y2),colors=('cyan','blue','green'))


        """
        gradientMethod = self.__gradientMethods[gradientMethod] if gradientMethod else self.__gradientMethod
        objectTag = objectTag if objectTag else self.__objectTag
        colors = colors if colors else self.__colors
        coords = coords if coords else self.__coords
        spread = spread if spread else self.__spread
        self.__objectTag = objectTag.lower()
        self.__coords = coords
        self.__spread = spread
        self.__colors = colors
        self.__gradientMethod = gradientMethod
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



def Example():  
    grad = Gradient() 
    root = Tk(screenName='GRADIENT')
    root.geometry('700x300')
    root.update()
    root.title('Gradient Tk')
    # root.attributes('-alpha',0.3)
    # 
    root.attributes('-topmost',1)
    geo = lambda : (int(root.winfo_width()),int(root.winfo_height()))
    canvas = Canvas(root,width=geo()[0],height=geo()[1],bg='#021316',highlightthickness=0)
    canvas.pack(expand=True,fill=BOTH)
    # root.attributes('-transparentcolor',canvas['bg'])
    grad(('black','cyan','blue','black'))
    print(canvas['width'])
    print(canvas['height'])
    ackeys = list(AllColors.keys())
    ackeys.remove('black')
    

    gr = GradientCanvasObject(coords=(100,100,100,200,400)
                              ,spread=200,
                              canvas=canvas,
                              gradientMethod='DRMMG',
                              objectTag='c'
                        )
    lines = GradientCanvasObject(coords=(0,0,0,0),
                                 spread=200,
                                 canvas=canvas,
                                 objectTag='line')
    while True:
        
        ichoice = choice(range(ackeys.__len__()))
        inc = 3
        colorChoice = canvas['bg'],*ackeys[ichoice:ichoice+inc if ichoice < ackeys.__len__()-(inc+1) else ichoice-(inc+1)],canvas['bg']
        grad(colorChoice)
        colorsp = grad.MindMultiGradient(500)
        root.update()
        for i in colorsp:
            pos = root.winfo_pointerxy()
            
            color = i,canvas['bg']
            # root.attributes('-transparentcolor',color[0])
            # color =  rgb2hex(pixel(pos[0],pos[1])),canvas['bg']
            canvas.config(width=geo()[0],height=geo()[1])
            lx = (pos[0]-root.winfo_rootx())
            ly = (pos[1]-root.winfo_rooty())
            # gr.create(coords=(int(int(canvas['width'])/2),int(int(canvas['height'])/2),int(int(canvas['width'])/2),int(int(canvas['height'])/2)),colors=color)
            gr.create(coords=(lx,ly,lx,ly),colors=color)
            # lines.create(coords=(0,0,0,int(canvas['height'])),spread=lx,colors=[canvas['bg'],'#ff0000','#00ff00','#0000ff',canvas['bg']])
            root.update()
        


if __name__ == '__main__':
    # try:
        Example()
    # except tkinter.TclError:pass