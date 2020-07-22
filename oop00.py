class Point:
    x = 1
    y = 1

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print("Coords must be integer")

    def getCoords(self):
        return self.__x, self.__y


pt = Point(5, 7)
