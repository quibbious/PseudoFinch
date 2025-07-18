# TEST GIT REMOTE

import math

class Backend:
    
    NAME = None
    ID = None
    CURRENT_X = 0
    CURRENT_Y = 0
    redIntensity = 0 
    greenIntensity = 0
    blueIntensity = 0
    LEDScreenMatrix = [ # empty 5x5 matrix
        [0,0,0,0,0], # row 0
        [0,0,0,0,0], # row 1
        [0,0,0,0,0], # row 2
        [0,0,0,0,0], # row 3
        [0,0,0,0,0], # row 4
                       ]
    # columns of matrix go by indice of row
    # ex: row 2, column 3 => LEDScreenMatrix[2][2] => 'indice 2 of row 2 == column 3 of row 3'

    def setLEDMatrix(self, LEDList: list):
        # takes in a 5x5 matrix as an input to change the LEDMatrix from its current display to the desired one. 
        if len(LEDList) < 25: 
            return 1, "invalid number of values to change LEDMatrix. Please provide ALL zero and non-zero values to satisfy the list length"
        elif (all(isinstance(row, list) and len(row) == len(LEDList[0]) for row in LEDList) if LEDList else False): # i stole this code but it pretty much checks if the array can-
            # split evenly into a 5x5 matrix. if it can, it replaces the LEDScreenMatrix with itself
                LEDScreenMatrix = LEDList
                
    def alterLEDMatrixPixel(self, row, column, value):
        """
        `row: int`: ROW is the  row (0-4) that you are addressing. \n
        `column: int`: COLUMN is the column (0-4) that you are addressing. \n
        `value: int`: VALUE is an integer between 0 and 1 that defines if a pixel on the screen is ON or OFF. Integers other than 0 or 1 will default to 1 if the number is higher than 1, and default to 0 if the number is lower than 0\n
        """
        # since the screen's pixels are ON or OFF, the value has to be 0 or 1.
        if value > 1: value = 1 
        elif value < 0: value = 0

        self.LEDScreenMatrix[row][column] = value
        # dbg: print(self.LEDScreenMatrix[row-1][column-1])
        return 0

    
    

class Finch(Backend): 
    def __init__(self, name: str, id: int = 0):
        
        self.name = name # name of the finch 
        self.id = id # ID of the finch (default 0)
        
    ## OUTPUT METHODS
    
    def setMove(self, direction, distance, speed):
        pass 
    
    def setTurn(self, direction, angle, speed):
        pass
    def setMotors(self, leftSpeed, rightSpeed):
        pass
    def stop(self):
        pass
    def setBeak(self, redIntensity, greenIntensity, blueIntensity):
        pass
    def setTail(self, port, redIntensity, greenIntensity, blueIntensity):
        pass
    def playNote(self, note: int, beats: int ):
        pass
    def setDisplay(self, LEDlist: list):
        # Reshape the flat LEDlist into a 5x5 matrix and set it using the instance method
        matrix = [LEDlist[5*i:5*i+5] for i in range(0, math.ceil(len(LEDlist)/5))]
        return self.setLEDMatrix(matrix)
        
    def setPoint(self, row, column, value):
        LEDScreenMatrix = Backend.alterLEDMatrixPixel(self, row, column, value)
        return LEDScreenMatrix
    def print(self, message):
        pass
    def stopAll(self):
        pass
    
    ## INPUT METHODS
    
    def getDistance(self):
        pass
    def getLight(self, direction):
        pass
    def getLine(self, direction):
        pass
    def resetEncoders(self):
        pass
    def getEncoder(self, direction):
        pass
    def getButton(self, button):
        pass
    def isShaking(self):
        pass
    def getOrientation(self):
        pass
    def getAcceleration(self):
        pass
    def getCompass(self):
        pass
    def getMagnetometer(self):
        pass
    def getSound(self):
        pass
    def getTemperature(self):
        pass