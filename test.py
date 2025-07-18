import math
LEDScreenMatrix = [ # empty 5x5 matrix
    [0,0,0,0,0], # row 0
    [0,0,0,0,0], # row 1
    [0,0,1,0,0], # row 2
    [0,0,0,0,0], # row 3
    [0,0,0,0,0], # row 4
                   ]
# columns of matrix go by indice of row
# ex: row 2, column 3 => LEDScreenMatrix[2[2]] => 'indice 2 of row 2 == column 3 of row 3'



def alterLEDMatrixPixel(row, column, value):
    """
    `row: int`: ROW is the  row (0-4) that you are addressing. \n
    `column: int`: COLUMN is the column (0-4) that you are addressing. \n
    `value: int`: VALUE is an integer between 0 and 1 that defines if a pixel on the screen is ON or OFF. Integers other than 0 or 1 will default to 1 if the number is higher than 1, and default to 0 if the number is lower than 0\n
    """
    
    # since the screen's pixels are ON or OFF, the value has to be 0 or 1.
    if value > 1: value = 1 
    elif value < 1: value = 0
    LEDScreenMatrix[row][column] = value
    # dbg: print(LEDScreenMatrix[row-1][column-1])
    return 0
#print(LEDScreenMatrix[2][2])
#print(LEDScreenMatrix)
#alterLEDMatrix(3,3,-2)
#print(LEDScreenMatrix)

LEDList = [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]
print([LEDList[5*i:5*i+5] for i in range(0,math.ceil(len(LEDList)/5))])