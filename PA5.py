#Programmers: Peter Hope
#Course: CS151,
# Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: name of file with information about taxi trips
# Program Outputs:  average cost for cash and (separately) credit card payments
#                   count of all trips that started or ended on a user-given date
#                   to a file (name provided by the user) the information for all trips with a pickup or dropoff location that is within a given distance of a given location
#


id=0
startDate=1 #month/day/year
startTime=2 #hour:minute
endDate=3
endTime=4
duration=5 #in seconds
distance=6 #miles
cost=7
payType=8 #"Cash" or "Credit Card"
company=9
pickupLat=10 #-90 to 90
pickupLong=11 #-180 to 180
dropoffLat=12
dropoffLong=13





def load_file(filename):
    taxis = []
    try:
        file = open(filename, "r")
        for line in file:
            taxi = line.split(",")
            taxis.append(taxi)
    except:
        print("no")
    return taxis



filename=input("filename:")
load_file(filename)
print(taxis)