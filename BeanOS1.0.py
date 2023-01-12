###########################################################################
#  May God's word guide me and humble me in the creation of these words.  #
###########################################################################

###########################################################################
#                            Rules For Design                             #
# 1st:   Designs must resemble Nature in some noticeable way.             #
# 2nd:   Designs must respect historic designs in some noticeable way.    #
# 3rd:   Designs should not copy other things but rather represent what   #
#        is best or necesary while embracing the uniqueness of the medium #
#        and/or pocess that is being used.                                #
# 4th:   Designs must be consistent in style and price                    #
###########################################################################


from functools import cache
import math

from random import seed
from random import randint

import time
import pygame

DEFINITELYBLACK = (0,0,0)
ROMANRED = (164,14,14)
GREEKWHITE = (215,232,238)
SPANISHSILVER = (81,104,111)
ORIENTALGREEN = (77, 144, 20)
GALLICGOLD = (227, 176, 19)
YOU = (0,0,255)
Height = 1011 #703
Width = 725 #500
AppHeight = int(Height*0.71)
StandardHeight = int(Height*0.29)
AppText = 'To Order Please'
AppTextTwo = 'Download the App:'
AppTextThree = 'Bionic Bean'
StandardText = '1234'
nameText = 'Cicero'
AppTextSize = 100
StandardTextSize = 300
NameTextSize = 100
count = 0
thyme = 0
DisapearX = 0
DisapearY = 0
apearX = 300
MenuLineX = 600
WHITE = (255, 255, 255)
LineSize = 5

SmallCupHeight = 400
SmallCupWidth = int(SmallCupHeight*0.84)
SmallCupX = Width
SmallCupShift = 0

MenuWidth = SmallCupWidth
menuX = Width
menuY = 0

disappearTopY = 0
disappearBottomY = 0
MenuSize = 75
MenuSizeTwo = int(MenuSize*0.8)
MenuSizeThree = int(MenuSize*0.6)
MenuSizeFour = int(MenuSize*0.4)
MenuSizeFive = int(MenuSize*0.2)

MenuSelectionTop = int(Height*0.51)
MenuSelectionBottom = int(Height*0.57)


LargeCupX = Width

SmallCupHeightTwo = int(SmallCupHeight*0.7)
SmallCupWidthTwo = int(SmallCupWidth*0.7)

SmallCupHeightThree = int(SmallCupHeight*0.3)
SmallCupWidthThree = int(SmallCupWidth*0.3)

SizeChange = (MenuSize-MenuSizeTwo)/16
SizeChangeTwo = (MenuSizeTwo-MenuSizeThree)/16
SizeChangeThree = (MenuSizeThree-MenuSizeFour)/16
SizeChangeFour = (MenuSizeFour-MenuSizeFive)/16
SizeChangeFive = MenuSizeFive/16

SmallCupY = 0
FRAUTH = (255,255,255)
SM = (224,224,219)
COFFEE = (190,155,89)
CHOCOLATE = (0,0,0)
ORANGESYRUP = (244,159,0)
sizeChange = 0

def standardTextDisplay(size, text, xLoc, yLoc):
    textFont = pygame.font.Font(None, size)
    titleSurface = textFont.render(text, True, WHITE)
    screen.blit(titleSurface, ((int((Width-textFont.size(text)[0])/2)+xLoc), (int((Height-textFont.size(text)[1])/2)+yLoc)))
def nameTextDisplay(size, text, xLoc, yLoc):
    textFont = pygame.font.Font(None, size)
    titleSurface = textFont.render(text, True, WHITE)
    screen.blit(titleSurface, ((int((Width-textFont.size(text)[0])/2)+xLoc), (int((Height-textFont.size(text)[1])/2)+yLoc)))
#def loadingCircle(size, xLoc, yLoc, width, percentage):
def circle(size, xLoc, yLoc, color, thickness, percentage):
    pi = math.pi
    loadingSurface = pygame.Surface((size, size))
    loadingRectangle = loadingSurface.get_rect(center = (size/2,size/2))
    # if(percentage <= 1):
    pygame.draw.arc(loadingSurface, color, loadingRectangle, -(percentage*2*pi-(pi/2)), pi/2, thickness)
    screen.blit(loadingSurface, ((Width/2)-(size/2)+xLoc,(Height/2)-(size/2)+yLoc))
def loadingCircle(size, xLoc, yLoc, color, thickness, nameText, time):
    percentage = 0.001
    while(percentage < 1):
        percentage += 0.001
        # standardSurfaceDisplay()
        circle(size, xLoc, yLoc, color, thickness, percentage)
        nameTextDisplay(NameTextSize, nameText, apearX, 0)
        pygame.display.update()
        pygame.time.delay((int)(time/1000))

def appTextDisplay(size, text, xLoc, yLoc):
    textFont = pygame.font.Font(None, size)
    titleSurface = textFont.render(text, True, GREEKWHITE)
    screen.blit(titleSurface, ((int((Width-textFont.size(text)[0])/2)+xLoc), (int((Height-textFont.size(text)[1])/5)+yLoc)))
def appTextDisplayTwo(size, text, xLoc, yLoc):
    textFont = pygame.font.Font(None, size)
    titleSurface = textFont.render(text, True, GallicGold)
    screen.blit(titleSurface, ((int((Width-textFont.size(text)[0])/2)+xLoc), (int((Height-textFont.size(text)[1])/5)+yLoc)))
def appSurfaceDisplay():
    appSurface = pygame.Surface((Width,AppHeight))
    appSurface.fill(DEFINITELYBLACK)
    screen.blit(appSurface,(0,0))
def standardSurfaceDisplay():
    standardSurface = pygame.Surface((Width,Height))
    standardSurface.fill(DEFINITELYBLACK)
    screen.blit(standardSurface,(0,0))

class Menu:
    size = 0
    def set(self, X, Y, Size, Text):
        self.size = Size
        self.text = Text
        self.x = X
        self.y = Y
        self.textFont = pygame.font.Font(None, int(self.size))
        titleSurface = textFont.render(self.text, True, GREEKWHITE)
        titleRect = titleSurface.get_rect(center = (self.x,self.y))
        screen.blit(titleSurface, titleRect)
    def set(self, Size, Text):
        self.size = Size
        self.text = Text
        self.textFont = pygame.font.Font(None, int(self.size))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
    def setSize(self, Size):
        self.size = Size
        self.textFont = pygame.font.Font(None, int(self.size))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        #self.titleRect = self.titleSurface.get_rect(center = (self.x,self.y))
        #screen.blit(self.titleSurface, self.titleRect)
    def addSize(self, Size):
        self.size = self.size+Size
        self.textFont = pygame.font.Font(None, int(self.size))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        #self.titleRect = self.titleSurface.get_rect(center = (self.x,self.y))
        #screen.blit(self.titleSurface, self.titleRect)
    def location(self,X,Y):
        self.x = X
        self.y = Y
        self.titleRect = self.titleSurface.get_rect(center = (self.x,self.y))
        screen.blit(self.titleSurface, self.titleRect)
    def addLocation(self,X,Y):
        self.x += X
        self.y += Y
        self.titleRect = self.titleSurface.get_rect(center = (self.x,self.y))
        screen.blit(self.titleSurface, self.titleRect)
    def display():
        screen.blit(self.titleSurface, self.titleRect)

class CoffeeCup:
    x = 500
    y = 0
    size = 0
    text = 0
    textTwo = 0
    syrup = 0
    coffee = 0
    sm = 0
    frauth = 0
    syrupColor = 0
    def set(self,X,Y,Size,Text,TextTwo,Syrup,Coffee,Sm,Frauth,SyrupColor):
        x = X
        y = Y
        size = Size
        syrup = Syrup
        coffee = Coffee
        sm = Sm
        frauth = Frauth
        syrupColor = SyrupColor
        test = int(size*0.2)
        
        CupWidth = int(size*0.84)-test
        fill = int(size-size*0.2)
        test_surfaceX = pygame.image.load('SmallCup.png').convert_alpha()
        test_surface = pygame.transform.scale(test_surfaceX, (CupWidth+test, size))
        syrupHeight = int((fill*syrup)/100)
        syrupSurface = pygame.Surface((CupWidth,syrupHeight))
        syrupSurface.fill(syrupColor)
        coffeeHeight = int((fill*coffee)/100)
        coffeeSurface = pygame.Surface((CupWidth,coffeeHeight))
        coffeeSurface.fill(COFFEE)
        smHeight = int((fill*sm)/100)
        smSurface = pygame.Surface((CupWidth,smHeight))
        smSurface.fill(SM)
        frauthHeight = int((fill*frauth)/100)
        frauthSurface = pygame.Surface((CupWidth,frauthHeight))
        frauthSurface.fill(FRAUTH)
        capHeight = int((size*18)/100)
        textFont = pygame.font.Font(None, int(size*0.2))
        titleSurface = textFont.render(text, True, GREEKWHITE)
        titleRect = titleSurface.get_rect(centerx = x, top = y+size)
        screen.blit(titleSurface, titleRect)
        titleSurfaceTwo = textFont.render(textTwo, True, GREEKWHITE)
        titleRectTwo = titleSurfaceTwo.get_rect(centerx = x, top = y+size+textFont.size(text)[1])
        frauthRect = frauthSurface.get_rect(centerx = x, top = y+capHeight)
        smRect = smSurface.get_rect(centerx = x, top = y+capHeight+frauthHeight)
        coffeeRect = coffeeSurface.get_rect(centerx = x, top = y+capHeight+frauthHeight+smHeight)
        syrupRect = syrupSurface.get_rect(centerx = x, top = y+capHeight+frauthHeight+smHeight+coffeeHeight)
        testRect = test_surface.get_rect(centerx = x, top = y)
        screen.blit(titleSurface, titleRect)
        screen.blit(titleSurfaceTwo, titleRectTwo)
        screen.blit(frauthSurface,frauthRect)
        screen.blit(smSurface, smRect)
        screen.blit(coffeeSurface,coffeeRect)
        screen.blit(syrupSurface, syrupRect)
        screen.blit(test_surface, testRect)
        self.test = self.size+int(self.size*0.35)
    def set(self,Size,Text,TextTwo,Syrup,Coffee,Sm,Frauth,SyrupColor):
        self.size = Size
        self.text = Text
        self.textTwo = TextTwo
        self.syrup = Syrup
        self.coffee = Coffee
        self.sm = Sm
        self.frauth = Frauth
        self.syrupColor = SyrupColor


        test = int(self.size*0.2)
        CupWidth = int(self.size*0.84)-test
        fill = int(self.size-self.size*0.2)
        self.test_surfaceX = pygame.image.load('SmallCup.png')
        self.test_surface = pygame.transform.scale(self.test_surfaceX, (CupWidth+test, self.size))
        self.syrupHeight = int((fill*self.syrup)/100)
        self.syrupSurface = pygame.Surface((CupWidth,self.syrupHeight))
        self.syrupSurface.fill(self.syrupColor)
        self.coffeeHeight = int((fill*self.coffee)/100)
        self.coffeeSurface = pygame.Surface((CupWidth,self.coffeeHeight))
        self.coffeeSurface.fill(COFFEE)
        self.smHeight = int((fill*self.sm)/100)
        self.smSurface = pygame.Surface((CupWidth,self.smHeight))
        self.smSurface.fill(SM)
        self.frauthHeight = int((fill*self.frauth)/100)
        self.frauthSurface = pygame.Surface((CupWidth,self.frauthHeight))
        self.frauthSurface.fill(FRAUTH)
        self.capHeight = int((self.size*18)/100)
        self.textFont = pygame.font.Font(None, int(self.size*0.2))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        self.titleSurfaceTwo = self.textFont.render(self.textTwo, True, GREEKWHITE)
        self.test = self.size+int(self.size*0.35)
    def setSize(self,Size):
        self.size = Size
        test = int(self.size*0.2)
        CupWidth = int(self.size*0.84)-test
        fill = int(self.size-self.size*0.2)
        self.test_surfaceX = pygame.image.load('SmallCup.png')
        self.test_surface = pygame.transform.scale(self.test_surfaceX, (CupWidth+test, self.size))
        self.syrupHeight = int((fill*self.syrup)/100)
        self.syrupSurface = pygame.Surface((CupWidth,self.syrupHeight))
        self.syrupSurface.fill(self.syrupColor)
        self.coffeeHeight = int((fill*self.coffee)/100)
        self.coffeeSurface = pygame.Surface((CupWidth,self.coffeeHeight))
        self.coffeeSurface.fill(COFFEE)
        self.smHeight = int((fill*self.sm)/100)
        self.smSurface = pygame.Surface((CupWidth,self.smHeight))
        self.smSurface.fill(SM)
        self.frauthHeight = int((fill*self.frauth)/100)
        self.frauthSurface = pygame.Surface((CupWidth,self.frauthHeight))
        self.frauthSurface.fill(FRAUTH)
        self.capHeight = int((self.size*18)/100)
        self.textFont = pygame.font.Font(None, int(self.size*0.2))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        self.titleSurfaceTwo = self.textFont.render(self.textTwo, True, GREEKWHITE)
        self.test = self.size+int(self.size*0.35)
    def addSize(self,Size):
        self.size = self.size+Size
        test = int(self.size*0.2)
        CupWidth = int(self.size*0.84)-test
        fill = int(self.size-self.size*0.2)
        self.test_surfaceX = pygame.image.load('SmallCup.png')
        self.test_surface = pygame.transform.scale(self.test_surfaceX, (CupWidth+test, self.size))
        self.syrupHeight = int((fill*self.syrup)/100)
        self.syrupSurface = pygame.Surface((CupWidth,self.syrupHeight))
        self.syrupSurface.fill(self.syrupColor)
        self.coffeeHeight = int((fill*self.coffee)/100)
        self.coffeeSurface = pygame.Surface((CupWidth,self.coffeeHeight))
        self.coffeeSurface.fill(COFFEE)
        self.smHeight = int((fill*self.sm)/100)
        self.smSurface = pygame.Surface((CupWidth,self.smHeight))
        self.smSurface.fill(SM)
        self.frauthHeight = int((fill*self.frauth)/100)
        self.frauthSurface = pygame.Surface((CupWidth,self.frauthHeight))
        self.frauthSurface.fill(FRAUTH)
        self.capHeight = int((self.size*18)/100)
        self.textFont = pygame.font.Font(None, int(self.size*0.2))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        self.titleSurfaceTwo = self.textFont.render(self.textTwo, True, GREEKWHITE)
        self.test = self.size+int(self.size*0.35)
    def location(self,X,Y):
        self.x = X
        self.y = Y
        self.titleRect = self.titleSurface.get_rect(centerx = self.x, top = self.y+self.size)
        screen.blit(self.titleSurface, self.titleRect)
        self.titleRectTwo = self.titleSurfaceTwo.get_rect(centerx = self.x, top = self.y+self.size+self.textFont.size(self.text)[1])
        self.frauthRect = self.frauthSurface.get_rect(centerx = self.x, top = self.y+self.capHeight)
        self.smRect = self.smSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight)
        self.coffeeRect = self.coffeeSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight)
        self.syrupRect = self.syrupSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight+self.coffeeHeight)
        self.testRect = self.test_surface.get_rect(centerx = self.x, top = self.y)
        screen.blit(self.titleSurface, self.titleRect)
        screen.blit(self.titleSurfaceTwo, self.titleRectTwo)
        screen.blit(self.frauthSurface,self.frauthRect)
        screen.blit(self.smSurface, self.smRect)
        screen.blit(self.coffeeSurface,self.coffeeRect)
        screen.blit(self.syrupSurface, self.syrupRect)
        screen.blit(self.test_surface, self.testRect)
    def addLocation(self,X,Y):
        self.x += X
        self.y += Y
        self.titleRect = self.titleSurface.get_rect(centerx = self.x, top = self.y+self.size)
        screen.blit(self.titleSurface, self.titleRect)
        self.titleRectTwo = self.titleSurfaceTwo.get_rect(centerx = self.x, top = self.y+self.size+self.textFont.size(self.text)[1])
        self.frauthRect = self.frauthSurface.get_rect(centerx = self.x, top = self.y+self.capHeight)
        self.smRect = self.smSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight)
        self.coffeeRect = self.coffeeSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight)
        self.syrupRect = self.syrupSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight+self.coffeeHeight)
        self.testRect = self.test_surface.get_rect(centerx = self.x, top = self.y)
        screen.blit(self.titleSurface, self.titleRect)
        screen.blit(self.titleSurfaceTwo, self.titleRectTwo)
        screen.blit(self.frauthSurface,self.frauthRect)
        screen.blit(self.smSurface, self.smRect)
        screen.blit(self.coffeeSurface,self.coffeeRect)
        screen.blit(self.syrupSurface, self.syrupRect)
        screen.blit(self.test_surface, self.testRect)
    def display(self):
        screen.blit(self.titleSurface, self.titleRect)
        screen.blit(self.titleSurfaceTwo, self.titleRectTwo)
        screen.blit(self.frauthSurface,self.frauthRect)
        screen.blit(self.smSurface, self.smRect)
        screen.blit(self.coffeeSurface,self.coffeeRect)
        screen.blit(self.syrupSurface, self.syrupRect)
        screen.blit(self.test_surface, self.testRect)



class LargeCoffeeCup:
    x = 500
    y = 0
    size = 0
    text = 0
    textTwo = 0
    syrup = 0
    coffee = 0
    sm = 0
    frauth = 0
    syrupColor = 0
    def set(self,X,Y,Size,Text,TextTwo,Syrup,Coffee,Sm,Frauth,SyrupColor):
        x = X
        y = Y
        size = Size
        syrup = Syrup
        coffee = Coffee
        sm = Sm
        frauth = Frauth
        syrupColor = SyrupColor
        test = int(size*0.2)
        
        CupWidth = int(size*0.84)-test
        fill = int(size-size*0.2)
        test_surfaceX = pygame.image.load('SmallCup.png').convert_alpha()
        test_surface = pygame.transform.scale(test_surfaceX, (CupWidth+test, size))
        syrupHeight = int((fill*syrup)/100)
        syrupSurface = pygame.Surface((CupWidth,syrupHeight))
        syrupSurface.fill(syrupColor)
        coffeeHeight = int((fill*coffee)/100)
        coffeeSurface = pygame.Surface((CupWidth,coffeeHeight))
        coffeeSurface.fill(COFFEE)
        smHeight = int((fill*sm)/100)
        smSurface = pygame.Surface((CupWidth,smHeight))
        smSurface.fill(SM)
        frauthHeight = int((fill*frauth)/100)
        frauthSurface = pygame.Surface((CupWidth,frauthHeight))
        frauthSurface.fill(FRAUTH)
        capHeight = int((size*18)/100)
        textFont = pygame.font.Font(None, int(size*0.2))
        titleSurface = textFont.render(text, True, GREEKWHITE)
        titleRect = titleSurface.get_rect(centerx = x, top = y+size)
        screen.blit(titleSurface, titleRect)
        titleSurfaceTwo = textFont.render(textTwo, True, GREEKWHITE)
        titleRectTwo = titleSurfaceTwo.get_rect(centerx = x, top = y+size+textFont.size(text)[1])
        frauthRect = frauthSurface.get_rect(centerx = x, top = y+capHeight)
        smRect = smSurface.get_rect(centerx = x, top = y+capHeight+frauthHeight)
        coffeeRect = coffeeSurface.get_rect(centerx = x, top = y+capHeight+frauthHeight+smHeight)
        syrupRect = syrupSurface.get_rect(centerx = x, top = y+capHeight+frauthHeight+smHeight+coffeeHeight)
        testRect = test_surface.get_rect(centerx = x, top = y)
        screen.blit(titleSurface, titleRect)
        screen.blit(titleSurfaceTwo, titleRectTwo)
        screen.blit(frauthSurface,frauthRect)
        screen.blit(smSurface, smRect)
        screen.blit(coffeeSurface,coffeeRect)
        screen.blit(syrupSurface, syrupRect)
        screen.blit(test_surface, testRect)
        self.test = self.size+int(self.size*0.35)
    def set(self,Size,Text,TextTwo,Syrup,Coffee,Sm,Frauth,SyrupColor):
        self.size = Size
        self.text = Text
        self.textTwo = TextTwo
        self.syrup = Syrup
        self.coffee = Coffee
        self.sm = Sm
        self.frauth = Frauth
        self.syrupColor = SyrupColor


        test = int(self.size*0.2)
        CupWidth = int(self.size*0.84)-test
        fill = int(self.size-self.size*0.2)
        self.test_surfaceX = pygame.image.load('SmallCup.png')
        self.test_surface = pygame.transform.scale(self.test_surfaceX, (CupWidth+test, self.size))
        self.syrupHeight = int((fill*self.syrup)/100)
        self.syrupSurface = pygame.Surface((CupWidth,self.syrupHeight))
        self.syrupSurface.fill(self.syrupColor)
        self.coffeeHeight = int((fill*self.coffee)/100)
        self.coffeeSurface = pygame.Surface((CupWidth,self.coffeeHeight))
        self.coffeeSurface.fill(COFFEE)
        self.smHeight = int((fill*self.sm)/100)
        self.smSurface = pygame.Surface((CupWidth,self.smHeight))
        self.smSurface.fill(SM)
        self.frauthHeight = int((fill*self.frauth)/100)
        self.frauthSurface = pygame.Surface((CupWidth,self.frauthHeight))
        self.frauthSurface.fill(FRAUTH)
        self.capHeight = int((self.size*18)/100)
        self.textFont = pygame.font.Font(None, int(self.size*0.2))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        self.titleSurfaceTwo = self.textFont.render(self.textTwo, True, GREEKWHITE)
        self.test = self.size+int(self.size*0.35)
    def setSize(self,Size):
        self.size = Size
        test = int(self.size*0.2)
        CupWidth = int(self.size*0.84)-test
        fill = int(self.size-self.size*0.2)
        self.test_surfaceX = pygame.image.load('SmallCup.png')
        self.test_surface = pygame.transform.scale(self.test_surfaceX, (CupWidth+test, self.size))
        self.syrupHeight = int((fill*self.syrup)/100)
        self.syrupSurface = pygame.Surface((CupWidth,self.syrupHeight))
        self.syrupSurface.fill(self.syrupColor)
        self.coffeeHeight = int((fill*self.coffee)/100)
        self.coffeeSurface = pygame.Surface((CupWidth,self.coffeeHeight))
        self.coffeeSurface.fill(COFFEE)
        self.smHeight = int((fill*self.sm)/100)
        self.smSurface = pygame.Surface((CupWidth,self.smHeight))
        self.smSurface.fill(SM)
        self.frauthHeight = int((fill*self.frauth)/100)
        self.frauthSurface = pygame.Surface((CupWidth,self.frauthHeight))
        self.frauthSurface.fill(FRAUTH)
        self.capHeight = int((self.size*18)/100)
        self.textFont = pygame.font.Font(None, int(self.size*0.2))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        self.titleSurfaceTwo = self.textFont.render(self.textTwo, True, GREEKWHITE)
        self.test = self.size+int(self.size*0.35)
    def addSize(self,Size):
        self.size = self.size+Size
        test = int(self.size*0.2)
        CupWidth = int(self.size*0.84)-test
        fill = int(self.size-self.size*0.2)
        self.test_surfaceX = pygame.image.load('SmallCup.png')
        self.test_surface = pygame.transform.scale(self.test_surfaceX, (CupWidth+test, self.size))
        self.syrupHeight = int((fill*self.syrup)/100)
        self.syrupSurface = pygame.Surface((CupWidth,self.syrupHeight))
        self.syrupSurface.fill(self.syrupColor)
        self.coffeeHeight = int((fill*self.coffee)/100)
        self.coffeeSurface = pygame.Surface((CupWidth,self.coffeeHeight))
        self.coffeeSurface.fill(COFFEE)
        self.smHeight = int((fill*self.sm)/100)
        self.smSurface = pygame.Surface((CupWidth,self.smHeight))
        self.smSurface.fill(SM)
        self.frauthHeight = int((fill*self.frauth)/100)
        self.frauthSurface = pygame.Surface((CupWidth,self.frauthHeight))
        self.frauthSurface.fill(FRAUTH)
        self.capHeight = int((self.size*18)/100)
        self.textFont = pygame.font.Font(None, int(self.size*0.2))
        self.titleSurface = self.textFont.render(self.text, True, GREEKWHITE)
        self.titleSurfaceTwo = self.textFont.render(self.textTwo, True, GREEKWHITE)
        self.test = self.size+int(self.size*0.35)
    def location(self,X,Y):
        self.x = X
        self.y = Y
        self.titleRect = self.titleSurface.get_rect(centerx = self.x, top = self.y+self.size)
        screen.blit(self.titleSurface, self.titleRect)
        self.titleRectTwo = self.titleSurfaceTwo.get_rect(centerx = self.x, top = self.y+self.size+self.textFont.size(self.text)[1])
        self.frauthRect = self.frauthSurface.get_rect(centerx = self.x, top = self.y+self.capHeight)
        self.smRect = self.smSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight)
        self.coffeeRect = self.coffeeSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight)
        self.syrupRect = self.syrupSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight+self.coffeeHeight)
        self.testRect = self.test_surface.get_rect(centerx = self.x, top = self.y)
        screen.blit(self.titleSurface, self.titleRect)
        screen.blit(self.titleSurfaceTwo, self.titleRectTwo)
        screen.blit(self.frauthSurface,self.frauthRect)
        screen.blit(self.smSurface, self.smRect)
        screen.blit(self.coffeeSurface,self.coffeeRect)
        screen.blit(self.syrupSurface, self.syrupRect)
        screen.blit(self.test_surface, self.testRect)
    def addLocation(self,X,Y):
        self.x += X
        self.y += Y
        self.titleRect = self.titleSurface.get_rect(centerx = self.x, top = self.y+self.size)
        screen.blit(self.titleSurface, self.titleRect)
        self.titleRectTwo = self.titleSurfaceTwo.get_rect(centerx = self.x, top = self.y+self.size+self.textFont.size(self.text)[1])
        self.frauthRect = self.frauthSurface.get_rect(centerx = self.x, top = self.y+self.capHeight)
        self.smRect = self.smSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight)
        self.coffeeRect = self.coffeeSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight)
        self.syrupRect = self.syrupSurface.get_rect(centerx = self.x, top = self.y+self.capHeight+self.frauthHeight+self.smHeight+self.coffeeHeight)
        self.testRect = self.test_surface.get_rect(centerx = self.x, top = self.y)
        screen.blit(self.titleSurface, self.titleRect)
        screen.blit(self.titleSurfaceTwo, self.titleRectTwo)
        screen.blit(self.frauthSurface,self.frauthRect)
        screen.blit(self.smSurface, self.smRect)
        screen.blit(self.coffeeSurface,self.coffeeRect)
        screen.blit(self.syrupSurface, self.syrupRect)
        screen.blit(self.test_surface, self.testRect)
    def display(self):
        screen.blit(self.titleSurface, self.titleRect)
        screen.blit(self.titleSurfaceTwo, self.titleRectTwo)
        screen.blit(self.frauthSurface,self.frauthRect)
        screen.blit(self.smSurface, self.smRect)
        screen.blit(self.coffeeSurface,self.coffeeRect)
        screen.blit(self.syrupSurface, self.syrupRect)
        screen.blit(self.test_surface, self.testRect)

pygame.init()


screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Bean OS0')
clock = pygame.time.Clock()


#######################################################################################
#                                                                                     #
#                                    Program Begins                                   #
#                                                                                     #
#######################################################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if(count == 0):
        #Display rand num
        appSurfaceDisplay()
        standardSurfaceDisplay()
        seed(int(time.time()))
        StandardText = str(randint(1000,9999))
        standardTextDisplay(StandardTextSize, StandardText,0,0)
        #appTextDisplay(AppTextSize, AppTextTwo,0,70)
        #appTextDisplayTwo(AppTextSize, AppTextThree,0,140)
        pygame.display.update()
        count = 1
    if(count == 1):
        pygame.time.delay(5000)
        count = 2
    if(count == 2):
        while(DisapearY < 20):
            standardSurfaceDisplay()
            DisapearX -= 30
            DisapearY += 1
            standardTextDisplay(StandardTextSize, StandardText, DisapearX, 0)
            #appTextDisplay(StandardTextSize, AppTextTwo, DisapearX, 70)
            #appTextDisplayTwo(StandardTextSize, AppTextThree, DisapearX, 140)
            pygame.display.update()
            pygame.time.delay(10)
        count = 3
    if(count == 3):
        # display name
        while(apearX > 0):
            standardSurfaceDisplay()
            apearX -= 30
            circle(600, apearX, 0, GALLICGOLD, 50, 0.1)
            nameTextDisplay(NameTextSize, nameText, apearX, 0)
            pygame.display.update()
            pygame.time.delay(10)
        percentage = 0.001
        loadingCircle(600, apearX, 0, GALLICGOLD, 50, nameText, 10000)
        count = 4
    if(count == 4):
        pygame.time.delay(1000)
        while(apearX > -1000):
            standardSurfaceDisplay()
            apearX -= 5
            circle(600, apearX, 0, ORIENTALGREEN, 50, 1)
            nameTextDisplay(NameTextSize, nameText, apearX, 0)
            pygame.display.update()
            pygame.time.delay(10)





        #this will be deleted and is currently unused
    # if(count == 4):
    #     while(menuX > int(Width/2)):
    #         standardSurfaceDisplay()
    #         menuX -= 10
    #         OrangeMochaFrappechino.location(menuX,menuY)
    #         Mocha.location(menuX,(menuY-MenuSizeTwo*2))
    #         Latte.location(menuX,(menuY+MenuSizeTwo*2))
    #         FlatWhite.location(menuX,(menuY-(MenuSizeTwo+MenuSizeThree)*2))
    #         Cappuccino.location(menuX,(menuY+(MenuSizeTwo+MenuSizeThree)*2))
    #         Americano.location(menuX,(menuY-(MenuSizeTwo+MenuSizeThree+MenuSizeFour)*2))
    #         Black.location(menuX,(menuY+(MenuSizeTwo+MenuSizeThree+MenuSizeFour)*2))
    #         TriariiMocha.location(menuX,(menuY-(MenuSizeTwo+MenuSizeThree+MenuSizeFour+MenuSizeFive)*2))
    #         PeconPieLatte.location(menuX,(menuY+(MenuSizeTwo+MenuSizeThree+MenuSizeFour+MenuSizeFive)*2))
    #         pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionTop), (Width,MenuSelectionTop)], LineSize)
    #         pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionBottom), (Width,MenuSelectionBottom)], LineSize)
    #         pygame.time.delay(1)
    #         pygame.display.update()
    #     while(menuY > (((StandardHeight/2)+AppHeight)-MenuSizeTwo*2)):
    #         standardSurfaceDisplay()
    #         menuY -= 7
    #         if(thyme < 16):
    #             OrangeMochaFrappechino.addSize(-SizeChange)
    #             Mocha.addSize(-SizeChangeTwo)
    #             Latte.addSize(SizeChange)
    #             FlatWhite.addSize(-SizeChangeThree)
    #             Cappuccino.addSize(SizeChangeTwo)
    #             Americano.addSize(-SizeChangeFour)
    #             Black.addSize(SizeChangeThree)
    #             TriariiMocha.addSize(-SizeChangeFive)
    #             PeconPieLatte.addSize(SizeChangeFour)
    #             TriariiMochaTwo.addSize(SizeChangeFive)
    #             thyme = thyme+1
            
    #             #standardSurfaceDisplay()
    #         print(thyme)
    #         OrangeMochaFrappechino.location(menuX,menuY)
    #         Mocha.location(menuX,(menuY-Mocha.size*2))
    #         Latte.location(menuX,(menuY+Latte.size*2))
    #         FlatWhite.location(menuX,(menuY-(Mocha.size+FlatWhite.size)*2))
    #         Cappuccino.location(menuX,(menuY+(Latte.size+Cappuccino.size)*2))
    #         Americano.location(menuX,(menuY-(Mocha.size+FlatWhite.size+Americano.size)*2))
    #         Black.location(menuX,(menuY+(Latte.size+Cappuccino.size+Black.size)*2))
    #         TriariiMocha.location(menuX,(menuY-(Mocha.size+FlatWhite.size+Americano.size+TriariiMocha.size)*2))
    #         PeconPieLatte.location(menuX,(menuY+(Latte.size+Cappuccino.size+Black.size+PeconPieLatte.size)*2))
    #         TriariiMochaTwo.location(menuX,(menuY+(Cappuccino.size+Black.size+PeconPieLatte.size+TriariiMochaTwo.size)*2))
    #         pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionTop), (Width,MenuSelectionTop)], LineSize)
    #         pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionBottom), (Width,MenuSelectionBottom)], LineSize)
    #         pygame.time.delay(10)
    #         pygame.display.update()
    #     count = 5
    # if(count == 5):
    #     standardSurfaceDisplay()
    #     menuY = (StandardHeight/2)+AppHeight
    #     OrangeMochaFrappechino.location(menuX,menuY-OrangeMochaFrappechino.size*2)
    #     Mocha.location(menuX,(menuY-(OrangeMochaFrappechino.size+Mocha.size)*2))
    #     Latte.location(menuX,menuY)
    #     FlatWhite.location(menuX,(menuY-(OrangeMochaFrappechino.size+Mocha.size+FlatWhite.size)*2))
    #     Cappuccino.location(menuX,(menuY+Cappuccino.size*2))
    #     Americano.location(menuX,(menuY-(OrangeMochaFrappechino.size+Mocha.size+FlatWhite.size+Americano.size)*2))
    #     Black.location(menuX,(menuY+(Cappuccino.size+Black.size)*2))
    #     PeconPieLatte.location(menuX,(menuY+(Cappuccino.size+Black.size+PeconPieLatte.size)*2))
    #     TriariiMochaTwo.location(menuX,(menuY+(Cappuccino.size+Black.size+PeconPieLatte.size+TriariiMochaTwo.size)*2))
    #     pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionTop), (Width,MenuSelectionTop)], LineSize)
    #     pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionBottom), (Width,MenuSelectionBottom)], LineSize)
    #     pygame.time.delay(10)
    #     pygame.display.update()
    #     #print(OrangeMochaFrappechino.size)
    #     count = 6
    # if(count == 6):
    #     standardSurfaceDisplay()
    #     disappearTopY = menuY
    #     disapearBottomY = menuY
    #     i = 0
    #     while(MenuSelectionTop > 0):
    #         standardSurfaceDisplay()
    #         MenuSelectionTop -= 10
    #         MenuSelectionBottom += 10
    #         OrangeMochaFrappechino.addLocation(0,-10)
    #         Mocha.addLocation(0,-10)
    #         if(i < 40):
    #             Latte.addLocation(0,-7)
    #             i += 1
    #         Latte.addLocation(0,0)
    #         FlatWhite.addLocation(0,-10)
    #         Cappuccino.addLocation(0,10)
    #         Americano.addLocation(0,-10)
    #         Black.addLocation(0,10)
    #         PeconPieLatte.addLocation(0,10)
    #         TriariiMochaTwo.addLocation(0,10)
    #         pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionTop), (Width,MenuSelectionTop)], LineSize)
    #         pygame.draw.lines(screen, ROMANRED, False, [(menuX-(Width/2),MenuSelectionBottom), (Width,MenuSelectionBottom)], LineSize)
    #         appSurfaceDisplay()
    #         appTextDisplay(AppTextSize, 'App',0,0)
    #         pygame.draw.lines(screen, ROMANRED, False, [(0,AppHeight), (Width,AppHeight)], LineSize)
    #         pygame.time.delay(10)
    #         pygame.display.update()
    #     count = 7
    # if(count == 7):
    #     LatteSmall = CoffeeCup()
    #     LatteSmall.set(SmallCupHeight,'Small','',0,20,40,40,CHOCOLATE)
    #     LatteLarge = LargeCoffeeCup()
    #     LatteLarge.set(SmallCupHeight,'Large','',0,20,40,40,CHOCOLATE)
    #     SmallCupX = Width
    #     SmallCupY = ((StandardHeight-SmallCupHeight)/2)+AppHeight
    #     LatteSmall.location(SmallCupX, SmallCupY)
    #     LatteLarge.location((SmallCupX+LatteLarge.size),SmallCupY)
    #     while(SmallCupX > int((Width-LatteLarge.size)/2)):
    #         standardSurfaceDisplay()
    #         Latte.addLocation(0,0)
    #         SmallCupX -= 10
    #         LatteSmall.addLocation(-10,0)
    #         LatteLarge.addLocation(-10,0)
    #         pygame.display.update()
    #         pygame.time.delay(10)
    #     count = 8
    # if(count == 8):
    #     standardSurfaceDisplay()
    #     Latte.addLocation(0,0)
    #     if(LatteLarge.x < Width):
    #         LatteLarge.addLocation(10, 0)
    #     else:
    #         count = 9
    #     if(LatteSmall.x < (Width/2)):
    #         LatteSmall.addLocation(10, 0)
    #     else:
    #         LatteSmall.display()
    #     pygame.time.delay(10)
    #     pygame.display.update()
    clock.tick(60)
