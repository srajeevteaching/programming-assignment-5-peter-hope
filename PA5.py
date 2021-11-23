#Programmers: Peter Hope
#Course: CS151,
# Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: name of file with information about taxi trips
# Program Outputs:  average cost for cash and (separately) credit card payments
#                   count of all trips that started or ended on a user-given date
#                   to a file (name provided by the user) the information for all trips with a pickup or dropoff location that is within a given distance of a given location
#
import sys
import math


ID=0
START=1 #month/day/year hour:minute:second
END=2
DURATION=3 #in seconds
DISTANCE=4 #miles
COST=5
PAY_TYPE=6 #"Cash" or "Credit Card"
COMPANY=7
PICKUP_LAT=9 #-90 to 90
PICKUP_LON=9 #-180 to 180
DROPOFF_LAT=10
DROPOFF_LON=11

def load_file(): #loads the file given by user into a list of lists
    filename = input("file name: ")
    taxis = []
    try:
        file = open(filename, "r")
        for line in file:
            taxi = line.split(",")
            taxis.append(taxi)
        return taxis
    except FileNotFoundError:
        print("file not found")
        sys.exit()

def avgCost(taxis): # gathers and validates necessary input from lists about how much each trip cost and what payment they used
    cashTotal=0
    cashCount=0
    cardTotal=0
    cardCount=0
    otherCount=0
    for taxi in taxis:
        cost=float(taxi[COST])
        type=str(taxi[PAY_TYPE])
        if type == "Cash":
            cashTotal+=cost
            cashCount+=1
        elif type == "Credit Card":
            cardTotal+=cost
            cardCount+=1
        else:
            otherCount+=1
    cashAvg = avgCostCalc(cashTotal, cashCount)
    cardAvg = avgCostCalc(cardTotal, cardCount)
    print ("average cash total: ", cashAvg)
    print("average card total: ", cardAvg)

def avgCostCalc(total, count): #calculates how much the average cost was for a given payment type
    if count > 0:
        avg = total/count
        return avg
    else:
        print ("invalid input")
        sys.exit()

def dateCount(taxis): # gathers and validates neccessary input about the date and times of each trip and the inputted date by the user
    dcount=0
    date=input("What date would you like to use? (yyyy-m-d) ")
    for taxi in taxis:
        start=taxi[START]
        startDate,startTime = start.split(" ")
        end=taxi[END]
        endDate,endTime = end.split(" ")
        if startDate==date or endDate==date:
            dcount+=1
    if dcount > 0:
        print (dcount, "taxis started or ended on the date", date)
    else:
        print ("no taxis started or ended on the date", date)

def dateCountCalc(taxis, date): #calculates if date is on given date and then adds to count if it is
    for taxi in taxis:
        if startDate == date or endDate == date:
            count += 1
    return count

def location(taxis): #asks for location and distance, opens file, calls calc function for each taxi, if in distance then prints to file
    try:
        filename = input("what is the name of the file you would like to output to? ")
        outfile = open(filename, "w")
        print("please input the location")
        lat1 = float(input("latitude: "))
        while lat1 < -90 or lat1 > 90:
            lat1 = float(input("latitude (-90 to 90): "))
        lon1 = float(input("longitude: "))
        while lon1 < -180 or lon1 > 180:
            lon1 = float(input("longitude (-180 to 180): "))
        dist1 = float(input("how close does the distance have to be? (miles) "))
        while dist1 < 0:
            dist1 = float(input("how close does the distance have to be? (miles) "))
        for taxi in taxis:
            lat2 = float(taxi[PICKUP_LAT])
            lon2 = float(taxi[PICKUP_LON])
            lat3 = float(taxi[DROPOFF_LAT])
            lon3 = float(taxi[DROPOFF_LON])
            start = locationCalc(lat1, lon1, lat2, lon2, dist1)
            if start:
                print (taxi, file=outfile)
            else:
                end=locationCalc(lat1, lon1, lat3, lon3, dist1)
                if end:
                    print (taxi, file=outfile)

    except:
        print ("error")
        sys.exit()

def locationCalc(lat1,lon1,lat2,lon2,dist1): # calls distance function, sees if distance is smaller than user given distance
    dist2 = distance(lat1, lon1, lat2, lon2)
    if dist2 <= dist1:
        return True
    else:
        return False

def distance(lat1, lon1, lat2, lon2): #converts to radians and uses equation to find distance
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    #print(lat1, lon1, lat2, lon2)
    distance = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * 3959
    #print(distance)
    return distance

def main (): #drives the function, ask user what operation they would like to use and call the necessary functions
    taxis = load_file()
    print("file loaded")
    print("which operation would you like to do?")
    print("1. Calculates average cost for cash and credit card payments")
    print("2. Counts how many trips that started or ended on a given date")
    print("3. Finds all the trips that started or ended within a given distance to a given location")
    print("4. quit")
    choice = input()
    while choice != "4":
        if choice == "1":
            avgCost(taxis)
        elif choice == "2":
            dateCount(taxis)
        elif choice == "3":
            location(taxis)
        elif choice == "4":
            print("quitting")
        else:
            print("invalid choice")
        print("which operation would you like to do?")
        print("1. Calculates average cost for cash and credit card payments")
        print("2. Counts how many trips that started or ended on a given date")
        print("3. Finds all the trips that started or ended within a given distance to a given location")
        print("4. quit")
        choice = input()


main()

