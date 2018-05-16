
from datetime import datetime, timedelta
import time

# Get next 10 shuttles at my location.
# Out of these shuttles, isolate the ones that have my destination en route
# Out of those shuttles, calculate when they'll arrive to me next and using that info when they'll get to my destination next
# Recommend the one that will get to me next in >2 minutes and will get to my destination soonest.
shuttleSchedule = [{
    # These run from Monday 01:00 to Saturday 01:00
    "Mather Express":{
        "Mather House":['7:40', '8:00',"8:20","8:30","8:40","8:50","9:00","9:10","9:30","9:40","9:50","10:00","10:10","10:20","10:30","10:40","10:50","11:00","11:10","11:20","11:30","11:40","11:50","12:00","12:10","12:20","12:30","12:40","12:50","13:00","13:10","13:30","13:40","13:50","14:00","14:10","14:20","14:30","14:40","14:50","15:00","15:10","15:20","15:40","16:00"],
        'The Inn':['7:42','8:02',"8:22","8:32","8:42","8:52","9:02","9:12","9:22","9:32","9:42","9:52","10:02","10:12","10:22","10:32","10:42","10:52","11:02","11:12","11:22","11:32","11:42","11:52","12:02","12:12","12:22","12:32","12:42","12:52","13:02","13:12","13:22","13:32","13:42","13:52","14:02","14:12","14:22","14:32","14:42","14:52","15:02","15:12","15:22","15:42","16:02"],
        'Widener Gate':["7:43","8:03","8:23","8:33","8:43","8:53","9:03","9:13","9:23","9:33","9:43","9:53","10:03","10:13","10:23","10:33","10:43","10:53","11:03","11:13","11:23","11:33","11:43","11:53","12:03","12:13","12:23","12:33","12:43","12:53","13:03","13:13","13:23","13:33","13:43","13:53","14:03","14:13","14:23","14:33","14:43","14:53","15:03","15:13","15:23","15:43","16:03"],
        'Memorial Hall':["7:50","8:10","8:30","8:40","8:50","9:00","9:10","9:20","9:40","9:50","10:00","10:10","10:20","10:30","10:40","10:50","11:00","11:10","11:20","11:30","11:40","11:50","12:00","12:10","12:20","12:30","12:40","12:50","13:00","13:10","13:20","13:40","13:50","14:00","14:10","14:20","14:30","14:40","14:50","15:00","15:10","15:20","15:30","15:50","16:10"],
        'Lamont Library':["7:53","8:13","8:33","8:43","8:53","9:03","9:13","9:23","9:33","9:43","9:53","10:03","10:13","10:23","10:33","10:43","10:53","11:03","11:13","11:23","11:33","11:43","11:53","12:03","12:13","12:23","12:33","12:43","12:53","13:03","13:13","13:23","13:33","13:43","13:53","14:03","14:13","14:23","14:33","14:43","14:53","15:03","15:13","15:23","15:33","15:53","16:13"]
    },
    'Quad Stadium':{
        'Quad':["5:15","5:40","6:05","6:35","7:00"],
        'Garden St':["5:17","5:42","6:07","6:37","7:02"],
        'Lamont Library':["5:20","5:45","6:10","6:40","7:05"],
        'Winthrop House':["5:23","5:48","6:13","6:43","7:08"],
        'Mather House':["5:25","5:50","6:15","6:45","7:10"],
        'Stadium':["5:30","5:55","6:20","6:50","7:20"]
    },
    'Quad Yard Express':{
        'Quad':["16:55","17:20","17:45","18:10","18:35","19:00","19:25","19:50","20:10","20:30","20:50","21:10","21:30","21:50","22:10","22:30","22:50","23:10","23:30","23:50","0:10","0:30"],
        'Mass Ave Garden St':["17:00","17:25","17:50","18:15","18:40","19:05","19:30","19:53","20:13","20:33","20:53","21:13","21:33","21:53","22:13","22:33","22:53","23:13","23:33","23:53","0:13","0:33"],
        'Lamont Library':["17:05","17:30","17:55","18:20","18:45","19:10","19:35","19:55","20:15","20:55","21:15","21:35","21:55","22:15","22:35","22:55","23:15","23:35","23:55","0:15"],
        'Widener Gate':["16:45","17:10","17:35","18:00","18:25","18:50","19:15","19:40","20:00","20:20","20:40","21:00","21:20","21:40","22:00","22:20","22:40","23:00","23:20","23:40","0:00","0:20"]
    },
    'Mather House, Crimson Cruiser, Overnight':{
        'Mather House':["16:30","16:55","17:20","17:50","18:20","19:00","19:40","20:20","20:55","21:20","21:40","22:00","22:20","22:40","23:00","23:20","23:40","0:00"],
        'Peabody Terrace':["21:25","21:45","22:05","22:25","22:45","23:05","23:25","23:45","0:05"],
        'The Inn':["16:32","16:57","17:22","17:52","18:22","19:02","19:42","20:22","20:57","21:27","21:47","22:07","22:27","22:47","23:07","23:27","23:47","0:07"],
        'Widener Gate':["16:35","17:00","17:30","18:00","18:30","19:10","19:50","20:25","21:00","21:30","21:50","22:10","22:30","22:50","23:10","23:30","23:50","0:10"],
        'Quad':["18:40","19:20","20:00","20:35","21:20","21:40","22:00","22:20","22:40","23:00","23:20","23:40","0:00","0:20"],
        'Mass Ave Garden St':["18:43","19:23","20:03","20:38","21:23","21:43","22:03","22:23","22:43","23:03","23:23","23:43","0:03"],
        'Law School':["16:37","17:02","17:32","18:02","18:45","19:25","20:05","20:40","21:25","21:45","22:05","22:25","22:45","23:05","23:25","23:45","0:05"],
        'Maxwell Dworkin':["16:38","17:03","17:33","18:03","18:46","19:26","20:06","20:41","21:26","21:46","22:06","22:26","22:46","23:06","23:26","23:46","0:06"],
        'Memorial Hall':["16:45","17:10","17:40","18:10","18:50","19:30","20:10","20:45","21:05","21:30","21:50","22:10","22:30","22:50","23:10","23:30","23:50","0:10"],
        'Lamont Library':["16:48","17:13","17:43","18:13","18:53","19:33","20:13","20:48","21:08","21:33","21:53","22:13","22:33","22:53","23:13","23:33","23:53","0:13"],
        'Winthrop House':["21:17","21:37","21:57","22:17","22:37","22:57","23:17","23:37","23:57"]
    }
},
{
    # These run all 7 days
    'Overnight':{
        'Quad':["0:50","1:25","2:00","2:35","3:10","3:45"],
        'Mass Ave Garden St':["0:52","1:27","2:02","2:37","3:12","3:47"],
        'Law School':["0:53","1:28","2:03","2:38","3:13"],
        'Memorial Hall':["1:00","1:35","2:10","2:45","3:20"],
        'Lamont Library':["1:03","1:38","2:13","2:48","3:23"],
        'Winthrop House':["1:07","1:42","2:17","2:52","3:27"],
        'Mather House':["1:10","1:45","2:20","2:55","3:30"],
        'Peabody Terrace':["0:40","1:15","1:50","2:25","3:00","3:35"],
        'The Inn':["0:42","1:17","1:52","2:27","3:02","3:37"],
        'Widener Gate':["0:45","1:20","1:55","2:30","3:05","3:40"]
    }
},
{
    # These run from Saturday 03:00 to Sunday 05:00
    'Overnight':{
        'Quad':['4:20'],
        'Mass Ave Garden St':['4:22'],
        'Law School':['4:23'],
        'Memorial Hall':['3:55','4:30'],
        'Lamont Library':['3:58','4:33'],
        'Winthrop House':['4:02','4:37'],
        'Mather House':['4:05','4:40'],
        'Peabody Terrace':['4:10','4:45'],
        'The Inn':['4:12','4:47'],
        'Widener Gate':['4:15','4:50']
    }
},
{
    # These run from Saturday 01:00 to Monday 01:00
    'Crimson Cruiser':{
        'Quad':["8:30","9:05","9:40","10:15","10:50","11:25","12:05","12:40","13:15","13:50","14:25","15:00","15:35","16:10"],
        'Mass Ave Garden St':["8:33","9:08","9:43","10:18","10:53","11:28","12:08","12:43","13:18","13:53","14:28","15:03","15:38","16:13"],
        'Law School':["8:35","9:10","9:45","10:20","10:55","11:30","12:10","12:45","13:20","13:55","14:30","15:05","15:40","16:15"],
        'Memorial Hall':["8:40","9:15","9:50","10:25","11:00","11:35","12:15","12:50","13:25","14:00","14:35","15:10","15:45","16:20"],
        'Lamont Library':["8:43","9:18","9:53","10:28","11:03","11:38","12:18","12:53","13:28","14:03","14:38","15:13","15:48","16:23"],
        'Mather House':["8:15","8:50","9:25","10:00","10:35","11:10","12:25","13:00","13:35","14:10","14:45","15:20","15:55"],
        'The Inn':["8:17","8:52","9:27","10:02","10:37","11:12","12:27","13:02","13:37","14:12","14:47","15:22","15:57"],
        'Widener Gate':["8:20","8:55","9:30","10:05","10:40","11:15","12:30","13:05","13:40","14:15","14:50","15:25","16:00"]
    },
    "1636'Er":{
        'Quad':["16:30","16:50","17:10","17:30","17:50","18:10","18:30","18:50","19:10","19:30","19:50","20:10","20:45","21:05","21:25","21:45","22:05","22:25","22:45","23:05","23:25","23:45","0:10","0:25"],
        'Mass Ave Garden St':["16:33","16:53","17:13","17:33","17:53","18:13","18:33","18:53","19:13","19:33","19:53","20:13","20:48","21:08","21:28","21:48","22:08","22:28","22:48","23:08","23:28","23:48"],
        'Law School':["16:35","16:55","17:15","17:35","17:55","18:15","18:35","18:55","19:15","19:35","20:50","21:10","21:30","21:50","22:10","22:30","22:50","23:10","23:30","23:50"],
        'Maxwell Dworkin':["16:36","16:56","17:16","17:36","17:56","18:16","18:36","18:56","19:16","19:36","20:51","21:11","21:31","21:51","22:11","22:31","22:51","23:11","23:31","23:51"],
        'Memorial Hall':["16:40","17:00","17:20","17:40","18:00","18:20","18:40","19:00","19:20","19:40","20:55","21:15","21:35","21:55","22:15","22:35","22:55","23:15","23:35","23:55"],
        'Lamont Library':["16:43","17:03","17:23","17:43","18:03","18:23","18:43","19:03","19:23","19:43","20:58","21:18","21:38","21:58","22:18","22:38","22:58","23:18","23:38","23:58"],
        'Mather House':["16:50","17:10","17:30","17:50","18:10","18:30","18:50","19:10","19:30","19:50","21:05","21:25","21:45","22:05","22:25","22:45","23:05","23:25","23:45","0:05"],
        'Peabody Terrace':["16:55","17:15","17:35","17:55","18:15","18:35","18:55","19:15","19:35","19:55","20:30","20:50","21:10","21:30","21:50","22:10","22:30","22:50","23:10","23:30","23:50","0:10"],
        'The Inn':["16:57","17:17","17:37","17:57","18:17","18:37","18:57","19:17","19:37","19:57","20:32","20:52","21:12","21:32","21:52","22:12","22:32","22:52","23:12","23:32","23:52","0:12"],
        'Widener Gate':["16:20","16:40","17:00","17:20","17:40","18:00","18:20","18:40","19:00","19:20","19:40","20:00","20:35","20:55","21:15","21:35","21:55","22:15","22:35","22:55","23:15","23:35","23:55","0:15"]
    }
}]

myStops = ['The Inn', 'Widener Gate', 'Lamont Library']

def nextShuttle(destination):
    year, month, day, hour, minute, second, DoW = time.strftime("%Y,%m,%d,%H,%M,%S,%w").split(',')
    simTime = str(DoW)+":"+str(hour)+":"+str(minute)
    # First increment three minutes because we don't want to catch shuttle that is < 3 minutes away
    simTime = incrementOneMin(simTime)
    simTime = incrementOneMin(simTime)
    simTime = incrementOneMin(simTime)
    shuttleList = []
    while(True):
        simTime = incrementOneMin(simTime)
        tDoW, thour, tminute = simTime.split(":")
        curTime = str(thour)+":"+str(tminute)
        for busStop in myStops:
            if isBetween(1, '01:00', 6, '01:00', tDoW, thour, tminute):
                # Access Weekday Stuff
                if len(shuttlesNow(curTime, shuttleSchedule[0], busStop, 0)) > 0:
                    shuttleList.append(shuttlesNow(curTime, shuttleSchedule[0], busStop, 0))

            if True:
                # Access Daily Stuff
                if len(shuttlesNow(curTime, shuttleSchedule[1], busStop, 1)) > 0:
                    shuttleList.append(shuttlesNow(curTime, shuttleSchedule[1], busStop, 1))

            if isBetween(6, '3:00', 0, '5:00', tDoW, thour, tminute):
                # Access frisay stuff
                if len(shuttlesNow(curTime, shuttleSchedule[2], busStop, 2)) > 0:
                    shuttleList.append(shuttlesNow(curTime, shuttleSchedule[2], busStop, 2))

            if isBetween(6, '1:00', 1, '1:00', tDoW, thour, tminute):
                # Access Weekend stuff
                if len(shuttlesNow(curTime, shuttleSchedule[3], busStop, 3)) > 0:
                    shuttleList.append(shuttlesNow(curTime, shuttleSchedule[3], busStop, 3))

        if len(shuttleList) > 20:
            #print(shuttleList)
            break

    # Now go through the shuttleList and figure out which one will get you to your destination the fastest
    # First make a list of shuttles that will actually go to your destination
    okShuttles = []
    for query in shuttleList:
        for shuttle in query:
            try:
                arrivalTimes = shuttleSchedule[shuttle[0]][shuttle[1]][destination]
                #print(shuttle)
                NextShuttle = False
                for arrivalTime in arrivalTimes:
                    #print(arrivalTime)
                    # Start incrementing 1 minute from shuttle[3] and then see which is the next time that is hit within 100 iterations
                    # Check if it comes after the shuttle arrival time and then add it to okShuttles and break out of this for loop
                    simulatedTime = shuttle[3]
                    #stop = False
                    #print(arrivalTime)
                    for x in range(100):
                        simulatedTime = incrementOneMinHourMinute(simulatedTime)
                        #print(timeDiff(shuttle[3], arrivalTime))

                        simHour, simMin = simulatedTime.split(":")
                        arrHour, arrMin = arrivalTime.split(":")
                        #print(shuttle)

                        if int(simHour) == int(arrHour) and int(simMin) == int(arrMin) and NextShuttle == False:
                            tempshuttle = shuttle
                            tempshuttle.append(reformatTime(simulatedTime))
                            #print(tempshuttle)
                            okShuttles.append(tempshuttle)
                            NextShuttle = True
                            #break
                    if NextShuttle == True:
                        break
            except:
                continue

    print(okShuttles)
        #print(simTime)

def reformatTime(time):
    """ input ugly time in the form H:M and this will fill in the zeros """
    hour, minute = time.split(":")
    if int(minute) < 10:
        minute = "0" + minute
    return hour+":"+minute

def shuttlesNow(curTime, dictionary, stop, scheduleReferenceNumber):
    """ curTime should be of the format %H:%M and the dictionary should be one of the big shuttle dictionaries. """
    # Gives you all the shuttle that is leaving at the specified time and stop
    shuttles = []
    for shuttle, stops in dictionary.items():
        try:
            for stoptime in stops[stop]:
                hour, minute = stoptime.split(":")
                chour, cminute = curTime.split(":")
                if int(hour) == int(chour) and int(minute) == int(cminute):
                    shuttles.append([scheduleReferenceNumber, shuttle, stop, stoptime])
        except:
            continue
    return shuttles

def incrementOneMin(date):
    """ date is inputted as %w:%H:%M and the function returns another date that is one minute ahead. """
    stringDoW, stringhour, stringminute = date.split(":")
    DoW = int(stringDoW)
    hour = int(stringhour)
    minute = int(stringminute)
    minute = (minute + 1) % 60
    if minute == 0:
        # Must've incremented an hour
        hour = (hour + 1) % 24
        if hour == 0:
            # Must've incremented a day
            DoW = (DoW + 1) % 7
    return str(DoW)+":"+str(hour)+":"+str(minute)

def incrementOneMinHourMinute(date):
    """ date is inputted as %H:%M and the function returns another time that is one minute ahead. """
    stringhour, stringminute = date.split(":")
    hour = int(stringhour)
    minute = int(stringminute)
    minute = (minute + 1) % 60
    if minute == 0:
        # Must've incremented an hour
        hour = (hour + 1) % 24
    return str(hour)+":"+str(minute)

def timeDiff(s1, s2):
    """ Assuming the times are formatted like Hour:Minute. If s2 is later than s1 it will be positive. """
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    return convertToMins(str(tdelta))

def convertToMins(tdelta):
    """ Assuming that tdelta is of the format H:M:S """
    if "day" in tdelta:
        ntdelta = tdelta.replace(" day, ",":")
        days, hours, mins, secs = ntdelta.split(":")
    else:
        hours, mins, secs = tdelta.split(":")

    totalmins = int(hours) * 60 + int(mins)

    if "-" in tdelta:
        totalmins = totalmins * -1

    #print(totalmins)

    return totalmins

def isBetween(DoW1, time1, DoW2, time2, DoW, hour, minute):
    # May do funky things if the same day of weeks are inputted....
    # Time should be formatted as H:M and DoW should be an integer with 0 being sunday and 6 being saturday

    #year, month, day, hour, minute, second, DoW = time.strftime("%Y,%m,%d,%H,%M,%S,%w").split(',')

    # if the date is on a day between the two dates then it is def okay
    checkDay = int(DoW1)
    while (True):
        checkDay += 1
        if checkDay % 7 == int(DoW2):
            break;
        if checkDay % 7 == int(DoW):
            return True

    #print(timeDiff(time1, hour+":"+minute))
    #print(str(DoW)+ " " +str(DoW1))

    # Now it's gotta be either DoW == DoW1 or 2
    if int(DoW) == int(DoW1):
        if timeDiff(time1, hour+":"+minute) > 0:
            return True
    elif int(DoW) == int(DoW2):
        if timeDiff(hour+":"+minute, time2) > 0:
            return True
    return False

#print(isBetween(1, '1:00',0, '4:40'))
#print(timeDiff('2:1','02:05'))
nextShuttle('Quad')