#Syed Haider Naqvi, Kara Walp, Japmeet Bedi
#Final Project
#16th December, 2020
#This program will do something which im not sure of yet

from graphics import *
from random import *
from time import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label, color = "red"):


        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
        
        self.win = win
        #Saves the graphic window upon which the button will be drawn to a variable
        
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        #Calculates middle points and edge points for the buttons
        
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        #Saves those points in the form of point objects
        
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        #Creates and draws the rectangle part of the button
        
        self.label = Text(center, label)
        self.label.draw(win)
        #Creates and draws the label part of the button
        
        self.activate()
        #Starts off the button as activated

    def getLabel(self):
        
        """Returns the label string of this button."""
        
        return self.label.getText()

    def activate(self):
        
        """Sets this button to 'active'."""
        
        self.label.setFill('black') 
        self.rect.setWidth(2)       
        self.active = True
        #Sets label fill to black, makes the rectangle have a thicker boundary 
        #and activates it
        
    def deactivate(self):
        
        """Sets this button to 'inactive'."""
        
        self.label.setFill('darkgray')  
        self.rect.setWidth(1)           
        self.active = False
        #Sets the label fill to gray, makes the rectangle have a thinner boundary
        #and deactivates it

    def isClicked(self, pt):
        
        """Returns true if button active and Point pt is inside"""
        
        if self.active == True:
            if  (self.xmin <= pt.getX() <= self.xmax) and (self.ymin <= pt.getY() <= self.ymax): 
                return True
            else:
                return False
        #Checks if the click is inside the dimensions of the button and then
        #returns a True or False Boolean 

    def setSize(self, size):
        
        """Sets the size of the text in the label to a user specified size"""
        
        self.label.setSize(size)

    def unDraw(self):
        
        """Undraws and deactivates the button"""
        
        self.rect.undraw()
        self.label.undraw()
        self.deactivate()

    def Draw(self):
        
        """Draws and activates the button"""
        
        self.rect.draw(self.win)
        self.label.draw(self.win)
        self.activate()

    def setLabel(self, label):
        
        """Sets the text of the label to a user specified text"""
        
        self.label.setText(label)

class DieView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = DieView(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win            # save this for drawing pips later
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size   # radius of each pip
        hsize = size / 2.0        # half the size of the die
        offset = 0.6 * hsize      # distance from center to outer pips

        # create a square for the face of the die
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        # create 7 little circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        
        # draw an initial value of 1 on the die face
        self.setValue(1)

    def __makePip(self, x, y):
        """Internal helper method to draw a pip at (x,y).
            (This only gets called from within this class
            not to be used by anyone importing this module.)"""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set this die to display the given value."
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn pips on to display the given value
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)        
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)


class Player():

    """ The Player class is the basis of the Snakes and Ladders game where
            the name and pieces are created and the graphics of the pieces
            are created"""

    def __init__(self, name, win):

        """Constructs an object of the player class with a random piece color,
        their initial on the piece, and assigning it a square value of 1, as
        well as drawing it on the board"""

        #Constructor of the Player class 

        self.win = win

        
        #Assigns a random color to each piece 
        self.player_piece_color = color_rgb(randrange(256),randrange(256),randrange(256))

        self.player_name = name

        #Creates the player piece
        self.player_piece = Circle(Point(9,9), 3)
        self.player_piece.setFill(self.player_piece_color)
        self.player_piece.draw(self.win)

        #Puts initial of player name on the piece
        self.player_piece_name = Text(Point(9,9), self.player_name[0])
        self.player_piece_name.draw(win)

        self.square = 1

    def getName(self):
        """ Returns name of the player"""
    
        return self.player_name

    def getPiece(self):
        """ Returns piece """

        return self.player_piece

    def getSquare(self):
        """ Returns the square that the player is on """

        return self.square

    def moveTo(self, roll):
        """ Moves the piece to designated location """

        #While loop for moving the piece
        while roll > 0:
            
            #Condition for moving the piece up
            if self.square % 10 == 0:
            #For loop for animating the moving piece
                
                for i in range(18):
                    self.player_piece.move(0, 0.5)
                    self.player_piece_name.move(0,0.5)
                    sleep(0.01)

                roll = roll - 1
                self.square = self.square + 1
            #Winning condition
                if self.square == 100:

                    break

            #Conditions for moving the piece right on even-numbered lines
            elif 0 < self.square < 10 or 20 < self.square < 30 or 40 < self.square < 50 or 60 < self.square < 70 or 80 < self.square < 90:

                for i in range(18):
                #For loop for animating the piece movement
                    self.player_piece.move(0.5, 0)
                    self.player_piece_name.move(0.5,0)
                    sleep(0.01)

                roll = roll - 1
                self.square = self.square + 1

                if self.square == 100:

                    break
            #Conditions for moving the piece left on odd-numbered lines
            elif 10 < self.square < 20 or 30 < self.square < 40 or 50 < self.square < 60 or 70 < self.square < 80 or 90 < self.square < 100:

                for i in range(18):

                    self.player_piece.move(-0.5, 0)
                    self.player_piece_name.move(-0.5,0)
                    sleep(0.01)

                roll = roll - 1
                self.square = self.square + 1

                if self.square == 100:

                    break


    def moveTo_Snake_or_Ladder(self, move_amount_x, move_amount_y, square_number):
        """ Moves player piece to identify a Snake or Ladder position"""

        for i in range(100):

            self.player_piece.move(move_amount_x/100, move_amount_y/100)
            self.player_piece_name.move(move_amount_x/100,move_amount_y/100)
            sleep(0.01)

        self.square = square_number

    
class SnakesAndLadder():
    """ The Snakes and Ladders class creates the graphic window and the foundation for the
        game and the movements """

    def __init__(self, window, list_of_player_names):

        """ This constructs a game of Snakes and Ladders with 4 players"""

        #Constructor for Snakes and Ladder class
        self.window = window

        self.P1 = Player(list_of_player_names[0], window)
        self.P2 = Player(list_of_player_names[1], window)
        self.P3 = Player(list_of_player_names[2], window)
        self.P4 = Player(list_of_player_names[3], window)

    def movePlayer(self, player_number, roll):
        
        """ Moves the piece """
        
        #Moves the player when they roll the dice
        player_list = [self.P1, self.P2, self.P3, self.P4]

        player_list[player_number - 1 ].moveTo(roll)

    def playerWon(self):
        
        """ Identifies which player has won the game """
        
        #Method to check if any player has reached 100 
        player_list = [self.P1, self.P2, self.P3, self.P4]

        for i in range(len(player_list)):

            if player_list[i].getSquare() >= 100:

                return True

        return False

    def getPlayerName(self, player_number):
        
        """ Creates a player list for all four players playing and returns the list """
        
        #Returns player name from list
        
        player_list = [self.P1, self.P2, self.P3, self.P4]

        return player_list[player_number - 1].getName()

    def isSnake_or_Ladder(self, player_number):
        
        """ Detects if a player piece is touching a snake or a ladder """
        
        #Conditional statements for detecting whether the player piece is touching
        #a snake or ladder and moving the piece accordingly

        player_list = [self.P1, self.P2, self.P3, self.P4]

        if player_list[player_number - 1].getSquare() == 15:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-9,-9, 5)

        elif player_list[player_number - 1].getSquare() == 32:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(0,-27, 9)

        elif player_list[player_number - 1].getSquare() == 35:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-27,-18, 18)

        elif player_list[player_number - 1].getSquare() == 38:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-18,-18, 20)

        elif player_list[player_number - 1].getSquare() == 58:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-18,-9, 41)

        elif player_list[player_number - 1].getSquare() == 65:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(9,-36, 26)

        elif player_list[player_number - 1].getSquare() == 81:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(18,-18, 63)

        elif player_list[player_number - 1].getSquare() == 90:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-9,-18, 69)

        elif player_list[player_number - 1].getSquare() == 94:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(9,-54, 33)

        elif player_list[player_number - 1].getSquare() == 98:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(9,-27, 64)

        elif player_list[player_number - 1].getSquare() == 4:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(0,18, 24)

        elif player_list[player_number - 1].getSquare() == 8:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-9,27, 34)

        elif player_list[player_number - 1].getSquare() == 22:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(0, 18, 42)

        elif player_list[player_number - 1].getSquare() == 25:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(27, 45, 73)

        elif player_list[player_number - 1].getSquare() == 30:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(0, 9, 31)

        elif player_list[player_number - 1].getSquare() == 44:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-9,27, 78)

        elif player_list[player_number - 1].getSquare() == 49:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-9,9, 53)

        elif player_list[player_number - 1].getSquare() == 60:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(0,9 , 61)

        elif player_list[player_number - 1].getSquare() == 72:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(-9, 18, 93)

        elif player_list[player_number - 1].getSquare() == 85:

            player_list[player_number - 1].moveTo_Snake_or_Ladder(0,9, 96)

        
def clearScreen():
    """ Clears the screen to prepare for closing window """

    background = Rectangle(Point(-15,-20), Point(115,110))
    background.setFill("yellow")
    background.draw(Snakes_and_ladders)
        
def main():

    #Used to make sure the window is global for all functions and methods
    global Snakes_and_ladders

    #Creates graphical window for the game
    Snakes_and_ladders = GraphWin("Snakes and Ladders!", 600, 600)

    Snakes_and_ladders.setCoords(-15,-20, 115, 110)

    #Yellow background for the game
    background = Rectangle(Point(-15,-20), Point(115,110))
    background.setFill("yellow")
    background.draw(Snakes_and_ladders)

    #Introduction to the snakes and ladders game with welcome buttons
    introduction = Button(Snakes_and_ladders,Point(50,50), 120,30, \
                          "Welcome to the snakes and ladders game!\nThis is a 4 player game!", "orange")
    introduction.setSize(20)

    SNL_title = Button(Snakes_and_ladders, Point(50, 102.5), 60, 10, "Snakes and Ladders!", "orange")
    SNL_title.setSize(20)
    #Creates the title button

    continue_button = Button(Snakes_and_ladders, Point(50, -10), 30, 10, "Continue", "orange")
    continue_button.setSize(20)
    #Creates the continue button

    quit_button = Button(Snakes_and_ladders, Point(105, -10), 10, 10, "Quit", "orange")
    quit_button.unDraw()
    #Creates the quit button and undraws it for the time being

    continue_click = Snakes_and_ladders.getMouse()

    #While loop for checking button clicks
    while not continue_button.isClicked(continue_click):
        continue_click = Snakes_and_ladders.getMouse()

    introduction.unDraw()
    #Undraws the introduction

    player_names_button = Button(Snakes_and_ladders,Point(50,50), 120,20, "Please enter the names of all the players\nwho will play, seperated by a comma", "orange")
    player_names_button.setSize(20)
    #Prompts the user to enter the names of the 4 players who are playing

    player_names_entry = Entry(Point(50,20), 10)
    player_names_entry.draw(Snakes_and_ladders)
    #Draws the entry box which will get the names of the players

    continue_click = Snakes_and_ladders.getMouse()

    #While loop for checking buttons 
    while not continue_button.isClicked(continue_click):
        continue_click = Snakes_and_ladders.getMouse()

    player_names = player_names_entry.getText().replace(" " ,"")
    player_names_list = player_names.split(",")
    #Takes the raw string of player names and converts it into a list

    #Undraws introduction
    player_names_entry.undraw()
    continue_button.unDraw()
    player_names_button.unDraw()

    #Image of the Snakes and Ladder board
    board = Image(Point(50,50), "SNL.gif")
    board.draw(Snakes_and_ladders)

    SNL = SnakesAndLadder(Snakes_and_ladders, player_names_list)
    #Creates an instance of our Snakes and Ladders class 

    #Creates the dice used for the roll
    dice_1 = DieView(Snakes_and_ladders, Point(10,-10), 15)
    dice_2 = DieView(Snakes_and_ladders, Point(30,-10), 15)

    roll_button = Button(Snakes_and_ladders, Point(50, -10), 20, 10, "Roll", "orange")
    roll_button.setSize(20)
    #Creates the roll button

    quit_button.Draw()
    #Now activates the quit button and draws it on screen

    #Creates player buttons for all 4 players 
    player_4_button = Button(Snakes_and_ladders, Point(80, -10), 30, 10, "It's\n" + str(SNL.getPlayerName(4)) + "'s turn", "orange")
    player_1_button = Button(Snakes_and_ladders, Point(80, -10), 30, 10, "It's\n" + str(SNL.getPlayerName(1)) + "'s turn", "orange")
    player_2_button = Button(Snakes_and_ladders, Point(80, -10), 30, 10, "It's\n" + str(SNL.getPlayerName(2)) + "'s turn", "orange")
    player_3_button = Button(Snakes_and_ladders, Point(80, -10), 30, 10, "It's\n" + str(SNL.getPlayerName(3)) + "'s turn", "orange")

    player_2_button.unDraw()
    player_3_button.unDraw()
    #Initially undraws these two buttons as they are not needed

    main_loop_click = Snakes_and_ladders.getMouse()
    #initalises the main click which be used to keep the loop running and exit it

    player_list = [1,2,3,4]
    #Initialses the list of players

    turn_number = 1
    #A variable which is used to loop through the 4 players turn by turn

    #Boolean variable for checking who has the first turn
    first_turn = True

    #While loop for checking conditionals until a player has reached 100 to win 
    while not quit_button.isClicked(main_loop_click) and not SNL.playerWon():

        if roll_button.isClicked(main_loop_click):
            #Random roll for dice
            roll_1 = randrange(1,7)
            roll_2 = randrange(1,7)

            #Creates variable to hold total of dice rolls
            total_roll = roll_1 + roll_2

            dice_1.setValue(roll_1)
            dice_2.setValue(roll_2)
            
            #Moves player for the amount of dice roll
            SNL.movePlayer(player_list[turn_number - 1], total_roll)

            SNL.isSnake_or_Ladder(player_list[turn_number - 1])

            turn_number += 1

            #Breaks the loop when a player reaches 100
            if SNL.playerWon():
                break

            #Conditionals for drawing player buttons
            if turn_number == 5:

                turn_number = 1

            if turn_number == 2:

                player_1_button.unDraw()
                player_2_button.Draw()

            if turn_number == 3:

                player_2_button.unDraw()
                player_3_button.Draw()

            if turn_number == 4:

                player_3_button.unDraw()

                if first_turn == False:
                    player_4_button.Draw()

            if turn_number == 1:

                player_4_button.unDraw()
                first_turn = False
                player_1_button.Draw()
        
            main_loop_click = Snakes_and_ladders.getMouse()

        #Gets another mouseclick if no button is clicked
        else:
            main_loop_click = Snakes_and_ladders.getMouse()

    if not quit_button.isClicked(main_loop_click):

        #Conclusion of the game
        sleep(1)
        clearScreen()
        winner_screen = Button(Snakes_and_ladders, Point(50, 50), 110, 20, SNL.getPlayerName(turn_number - 1) + " has won the game!\nPlease click anywhere to exit the game", "orange")
        winner_screen.setSize(20)

        #Gets mouse to close the game
        Snakes_and_ladders.getMouse()

    Snakes_and_ladders.close()
    
main()
#Calls the main function
                            

    


        
        

        

    
