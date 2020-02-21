import math

def getText(filename):
    f = open('data/' + filename)
    first = f.readline()
    second = f.readline()

    problemInfo = strToInt(first.split())
    rewards = strToInt(second.split())
    libInfo = dict()
    libBooks = dict()
    for i in range(problemInfo[1]):
        lineOne = f.readline()
        lineTwo = f.readline()
        libInfo[i] = strToInt(lineOne.split())
        libBooks[i] = strToInt(lineTwo.split())
    f.close()
    return problemInfo, rewards, libInfo, libBooks

def strToInt(s):
    return [int(i) for i in s]

class Library:
    def __init__(self, index, books: list, signup, ship):
        self.index = index
        self.books = set(books)
        self.signup = signup
        self.ship = ship
        self.sortedBooks = sorted(self.books, key=lambda x: rewards[x], reverse=True)
        self.send = None # TODO : modified later
    
    def rewardbyDay(self, day: int):
        pass

    def DayToFinish(self):
        self.dayToFinish = self.signup
        self.dayToFinish += math.ceil(self.books / self.ship)



#print(lib.sortedBooks)

def solveConflict():
    libs = list()
    for i in range(problemInfo[1]):
        lib = Library(i, libBooks[i], libInfo[i][1], libInfo[i][2])
        libs.append(lib)
    
    libs = sorted(libs, key= lambda x: x.ship, reverse = True)
    allBooks = set([i for i in range(problemInfo[0])])
    for i in libs:
        b = set(i.books)
        for j in b:
            if j in allBooks:
                allBooks.remove(j)
            else:
                i.books.remove(j)

        print(i.index, i.books)


def pushText(filename, libs):

    libSentInfo = dict()
    for i in libs:
        send = ""
        for book in i.send:
            send += str(book) + " "
        libSentInfo[i] = str(i.index) + " " + str(len(i.send)) + "\n" + send + "\n"
    
    f = open('data/' + filename, 'w')
    f.write(str(len(libs)) + '\n')
    for i in range(len(libs)):
        f.write(libSentInfo[i])
    f.close()


if __name__ == '__main__':
    problemInfo, rewards, libInfo, libBooks = getText("e_so_many_books.txt")
    print(problemInfo)
    num_books, num_lib, num_days = problemInfo
    average_score = sum(rewards) / len(rewards)

    # lib = Library(0, libBooks[0], libInfo[0][1], libInfo[0][2])
    # solveConflict()
