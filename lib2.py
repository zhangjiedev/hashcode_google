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
        self.send = None  # TODO : modified later

    def rewardbyDay(self, day: int):
        pass

    def DayToFinish(self):
        self.dayToFinish = self.signup
        self.dayToFinish += math.ceil(self.books / self.ship)


def pushText(filename, libs):
    libSentInfo = dict()
    for i in libs:
        send = ""
        for book in i.send:
            send += str(book) + " "
        libSentInfo[i.index] = str(i.index) + " " + str(len(i.send)) + "\n" + send + "\n"

    f = open('data/' + filename, 'w')
    f.write(str(len(libs)) + '\n')
    for i in libs:
        f.write(libSentInfo[i.index])
    f.close()


if __name__ == '__main__':
    problemInfo, rewards, libInfo, libBooks = getText("c_incunabula.txt")
    # print(problemInfo)
    num_books, num_lib, num_days = problemInfo
    libs = []
    for i, lib in libInfo.items():
        libs.append(Library(i, libBooks[i], libInfo[i][1], libInfo[i][2]))
    # libs = list(libInfo.values())
    libs.sort(key=lambda x: (x.signup, x.ship, -len(x.books)))
    # libs.sort(key=lambda x: x[0], reverse=True)
    # for i in libs:
    #     print(i.index, i.signup, i.ship, len(i.books))

    for i in libs:
        i.send = sorted(i.books, key=lambda x: rewards[x], reverse=True)

    total_days = num_days
    index = 0
    for i in libs:
        total_days -= i.signup
        index += 1
        if total_days <= 0:
            break

    libs = libs[:index - 1]
    for i in libs:
        print(i.index, i.signup, i.ship, len(i.books))

    total = 0
    for i in libs:
        total += i.signup

    print(total)
    pushText('out.txt', libs)
