# input
    # who is batting?
    # who is bowling?
    # is this a death over?
# (backend) idk what that means but yea
    # get stats for batsman
    # get stats for bowler
    # generate over output
# print over output
# loop back to input

import random

def getStats(f):
    statsList = []
    for line in f:
        player = []
        batAvg = line[:5]
        batAvgSD = line[6:11]
        rpo = line[12:17] # rpo is batsman's strike rate
        rpoSD = line[18:23]
        bowlAvg = line[24:29]
        bowlAvgSD = line[30:35]
        er = line[36:41] # er is bowler's economy rate
        erSD = line[42:47]
        name = line[48:-1]
        player.append(batAvg)
        player.append(batAvgSD)
        player.append(rpo)
        player.append(rpoSD)
        player.append(bowlAvg)
        player.append(bowlAvgSD)
        player.append(er)
        player.append(erSD)
        player.append(name)
        statsList.append(player)
    return statsList

def findBatter(batter, stats):
    for i, player in enumerate(stats):
        if player[8] == batter:
            return (player)

def findBowler(bowler, stats):
    for i, player in enumerate(stats):
        if player[8] == bowler:
            return (player)

def overGen(statsList):
    curBatter = input("Who is batting?: ")
    batter = findBatter(curBatter, statsList)
    overCount = input("\tHow many overs have they faced?: ")
    attackRating = input("\tWhat is their Attack Rating? (1, 2, 3, 4, 5): ")
    if attackRating != "1" and attackRating != "2" and attackRating != "3" and attackRating != "4" and attackRating != "5":
        attackRating = input("\tLet's try that again. What is their Attack Rating? (1, 2, 3, 4, 5): ")
    curBowler = input("Who is bowling?: ")
    bowler = findBowler(curBowler, statsList)
    batAvgPredict = random.normalvariate(float(batter[0]), float(batter[1])) # x,y = x: batAvg, y: batAvgSD
    rpoPredict = random.normalvariate(float(batter[2]), float(batter[3])) # x,y = x: rpo, y: rpoSD
    bowlAvgPredict = random.normalvariate(float(bowler[4]), float(bowler[5])) # x,y = x: bowlAvg, y: bowlAvgSD
    erPredict = random.normalvariate(float(bowler[6]), float(bowler[7])) # x,y = x: er, y: erSD
    if int(overCount) > 0:
         batAvgPredict = round(batAvgPredict + (batAvgPredict * int(overCount)/5))
    rpoPredict = rpoPredict * (0.7 + (0.1 * int(attackRating)))
    if rpoPredict < erPredict:
        totalRuns = abs(random.randint(round(rpoPredict), round(erPredict)))
    else:
        totalRuns = abs(random.randint(round(erPredict), round(rpoPredict)))
    if batAvgPredict < bowlAvgPredict:
        totalAvg = abs(random.randint(round(batAvgPredict), round(bowlAvgPredict)))
    else:
        totalAvg = abs(random.randint(round(bowlAvgPredict), round(batAvgPredict)))
    print("\t\t" + str(curBatter) + " scores " + str(totalRuns) + ".")
    if random.randint(1, 10) <= (10 * (totalRuns/totalAvg)):
        print("\t\t" + str(curBatter) + " is OUT!")
    else:
        print("\t\t" + str(curBatter) + " is NOT OUT!")
    if totalRuns/totalAvg * 100 <= 100:
        print("\t\t" + str(curBatter) + " had a " + str(round(totalRuns/totalAvg * 100, 2)) + "% chance of getting out.")
    else: print("\t\t" + str(curBatter) + " had a 100% chance of getting out.")

def main():
    f = open("ipl2020-22stats.csv", "r")
    statsList = getStats(f)
    while True:
        overGen(statsList)

main()
