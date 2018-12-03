from graphics import *
import math
import random 
def main():
    win = GraphWin('CONNECT 4',430,370)
    win.yUp()
    rect1 = Rectangle(Point(0,0),Point(430,370))
    rect1.setFill("blue")
    rect1.draw(win)
    RGB = 0
    fileShape = makeCircles(win)
    winner = None 
    player = 0
    countTurn = 0
    playAgain = True 

    
    for x in range(43):
        if RGB == 0 :
            fileShape[x].setFill('Green')
            RGB = 1
        else:
            fileShape[x].setFill('Red')
            RGB = 0
            
        '''elif RGB == 2:
            fileShape[x].setFill('Blue')
        elif RGB == 3:
            fileShape[x].setFill('Yellow')
        elif RGB == 4:
            fileShape[x].setFill('White')
        elif RGB == 5:
            fileShape[x].setFill('Orange')
            

    '''
    for x in range(43):
        fileShape[x].setFill('White')

        
    while playAgain:
        turn = 1
        '''random.randint(0,1)'''
        if turn == 1:
            playerTurn = True
            computerTurn = False
        else:
            playerTurn = False
            computerTurn = True

        if playerTurn:
            
            mouse = win.getMouse()
            print('WORKS')
            player = 0
            inCircle(mouse,fileShape,player)

        if computerTurn:
            rand = random.randint(0,5)
            
    '''
    while winner  == 0:
        mouse = win.getMouse()
            inCircle(mouse,fileShape,player)
                
     
    '''      
            
    '''
    while winner == 0:
        for x in fileShape:
            Position = pygame.mouse.get_pos()
            if fileShape[x].collidepoint(position) and player == 0:
                fileShape[x].setFill('Red')
    '''
def inCircle(mouse, fileShape,player):
    # distance
    print('1')
    for x in range(43):
        print('2')
        dx = mouse.getX() - fileShape[x].getCenter().getX()
        dy = mouse.getY() - fileShape[x].getCenter().getY()
        dist = math.sqrt(dx*dx + dy*dy)

            
        if dist <= fileShape[x].getRadius() and player == 0 :
            '''fileShape[x].setFill('Red')'''
            check = checkUnder(fileShape,x)
        elif dist <= fileShape[x].getRadius() and player == 1:
            fileShape[x].setFill('Yellow')
            

                               
        
    # check whether the distance is less than the radius

def checkUnder(fileShape,x):
    if x < 6:
        fileShape[x].setFill('Red')
    elif x < 13:
        if fileShape[x-6].color() != 'white':
            print('#3')
            fileShape[x].setFill('Red')
            
        
        '''find how to check the color of shapes'''
    
    
def makeCircles(win):
    cir1 = Circle(Point(35,35), 25)
    cir1.setFill('Red')
    cir1.draw(win)

    cir2 = Circle(Point(95,35),25)
    cir2.setFill('red')
    cir2.draw(win)

    cir3 = Circle(Point(155,35),25)
    cir3.setFill('red')
    cir3.draw(win)
    
    cir4 = Circle(Point(215,35),25)
    cir4.setFill('red')
    cir4.draw(win)

    cir5 = Circle(Point(275,35),25)
    cir5.setFill('red')
    cir5.draw(win)

    cir6 = Circle(Point(335,35),25)
    cir6.setFill('red')
    cir6.draw(win)

    cir7 = Circle(Point(395,35),25)
    cir7.setFill('red')
    cir7.draw(win)

    cir8 = Circle(Point(35,95),25)
    cir8.setFill('red')
    cir8.draw(win)
    
    cir9 = Circle(Point(95,95),25)
    cir9.setFill('red')
    cir9.draw(win)
    
    cir10 = Circle(Point(155,95),25)
    cir10.setFill('red')
    cir10.draw(win)

    cir11 = Circle(Point(215,95),25)
    cir11.setFill('red')
    cir11.draw(win)

    cir12 = Circle(Point(275,95),25)
    cir12.setFill('red')
    cir12.draw(win)
    
    cir13 = Circle(Point(335,95),25)
    cir13.setFill('red')
    cir13.draw(win)
    
    
    cir14 = Circle(Point(395,95),25)
    cir14.setFill('red')
    cir14.draw(win)

    cir15 = Circle(Point(35,155),25)
    cir15.setFill('red')
    cir15.draw(win)

    cir16 = Circle(Point(95,155),25)
    cir16.setFill('red')
    cir16.draw(win)

    cir17 = Circle(Point(155,155),25)
    cir17.setFill('red')
    cir17.draw(win)

    cir18 = Circle(Point(215,155),25)
    cir18.setFill('red')
    cir18.draw(win)

    cir19 = Circle(Point(275,155),25)
    cir19.setFill('red')
    cir19.draw(win)

    cir20 = Circle(Point(335,155),25)
    cir20.setFill('red')
    cir20.draw(win)

    cir21 = Circle(Point(395,155),25)
    cir21.setFill('red')
    cir21.draw(win)

    cir22 = Circle(Point(35,215),25)
    cir22.setFill('red')
    cir22.draw(win)

    cir23 = Circle(Point(95,215),25)
    cir23.setFill('red')
    cir23.draw(win)

    cir24 = Circle(Point(155,215),25)
    cir24.setFill('red')
    cir24.draw(win)

    cir25 = Circle(Point(215,215),25)
    cir25.setFill('red')
    cir25.draw(win)

    cir26 = Circle(Point(275,215),25)
    cir26.setFill('red')
    cir26.draw(win)

    cir27 = Circle(Point(335,215),25)
    cir27.setFill('red')
    cir27.draw(win)

    cir28 = Circle(Point(395,215),25)
    cir28.setFill('red')
    cir28.draw(win)

    cir29 = Circle(Point(35,275),25)
    cir29.setFill('red')
    cir29.draw(win)

    cir30 = Circle(Point(95,275),25)
    cir30.setFill('red')
    cir30.draw(win)

    cir31 = Circle(Point(155,275),25)
    cir31.setFill('red')
    cir31.draw(win)

    cir32 = Circle(Point(215,275),25)
    cir32.setFill('red')
    cir32.draw(win)

    cir33 = Circle(Point(275,275),25)
    cir33.setFill('red')
    cir33.draw(win)

    cir34 = Circle(Point(335,275),25)
    cir34.setFill('red')
    cir34.draw(win)

    cir35 = Circle(Point(395,275),25)
    cir35.setFill('red')
    cir35.draw(win)

    cir36 = Circle(Point(35,335),25)
    cir36.setFill('red')
    cir36.draw(win)

    cir37 = Circle(Point(95,335),25)
    cir37.setFill('red')
    cir37.draw(win)

    cir38 = Circle(Point(155,335),25)
    cir38.setFill('red')
    cir38.draw(win)

    cir39 = Circle(Point(215,335),25)
    cir39.setFill('red')
    cir39.draw(win)

    cir40 = Circle(Point(275,335),25)
    cir40.setFill('red')
    cir40.draw(win)

    cir41 = Circle(Point(335,335),25)
    cir41.setFill('red')
    cir41.draw(win)

    cir42 = Circle(Point(395,335),25)
    cir42.setFill('red')
    cir42.draw(win)

    
    return [cir1,cir2,cir3,cir4,cir5,cir6,cir7,cir8,cir9,cir9,cir10
            ,cir11,cir12,cir13,cir14,cir15,cir16,cir17,cir18,cir19,cir20,cir21,cir22
            ,cir23,cir24,cir25,cir26,cir27,cir28,cir29,cir30,cir31,cir32,cir33,cir34
            ,cir35,cir36,cir37,cir38,cir39,cir40,cir41,cir42]


main()

