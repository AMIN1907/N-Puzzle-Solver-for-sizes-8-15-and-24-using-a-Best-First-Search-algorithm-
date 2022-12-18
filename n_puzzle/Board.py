from copy import deepcopy


class Board:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, N):
        self.__BoardSize = N
        self.__MovCounter = 0
        self.__GoalBoard = list()
        self.__SearchSpace = {}
        self.__Solution = list()

    def setSearchSpace(self, space):
        self.__SearchSpace = deepcopy(space)

    def getRestPath(self):
        return self.__Solution

    def getSolution(self):
        self.makesolutionpath()
        self.__Solution.reverse()
        return self.__Solution

    def clearSolution(self):
        self.__Solution = list()

    def setBOARDERSIZE(self, N):
        self.__BoardSize = N

    def getBOARDERSIZE(self):
        return self.__BoardSize

    def getTILESIZE(self):
        return int(250 / self.__BoardSize)

    def getMovCounter(self):
        return self.__MovCounter

    def incMovCounter(self):
        self.__MovCounter += 1

    def resetMovCounter(self):
        self.__MovCounter = 0

    def getBoard(self):
        # Return a board data structure with tiles in the solved state.
        # For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function
        # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
        self.resetMovCounter()
        counter = 1
        board = []

        for x in range(self.__BoardSize):
            column = []
            for y in range(self.__BoardSize):
                column.append(counter)
                counter += self.__BoardSize
            board.append(column)
            counter -= self.__BoardSize * \
                (self.__BoardSize - 1) + self.__BoardSize - 1

        board[self.__BoardSize - 1][self.__BoardSize - 1] = None
        self.__GoalBoard = board
        return board

    # space is searchspace map of keys : [0:state, 1:heuristec value, 2:lastmove, 3:parentState key]
    def makesolutionpath(self):
        laststate = self.__SearchSpace.popitem()
        key = laststate[1][3]
        # self.__Solution.append(laststate[1][2])
        while True:
            if (self.__SearchSpace.get(key))[3] == -1:
                break
            self.__Solution.append(self.__SearchSpace.get(key)[2])
            # self.__Solution.append(laststate[1][2])
            key = self.__SearchSpace.get(key)[3]
