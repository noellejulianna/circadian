import eventgen
import schedule
import datetime
import pickle
import main

workoutstart = datetime.datetime(2018,7,1,17,30)
workoutend = datetime.datetime(2019,7,1,17,30)
workout = eventgen.EventGen('workout',workoutstart,workoutend,1)

shampoostart = datetime.datetime(2018,7,15,21,00)
shampooend = datetime.datetime(2019,7,15,21,00)
shampoo = eventgen.EventGen('shampoo',shampoostart,shampooend,3)

kombuchastart = datetime.datetime(2018,6,1,8,30)
kombuchaend = datetime.datetime(2019,6,1,8,30)
kombucha = eventgen.EventGen('kombucha', kombuchastart,kombuchaend,2)

coconutoilstart = datetime.datetime(2018,6,19,12,30)
coconutoilend = datetime.datetime(2019,6,19,12,30)
coconutoil = eventgen.EventGen('coconut Oil',coconutoilstart,coconutoilend,7)

sched = schedule.Schedule([coconutoil,workout,shampoo])
print(sched.eventColors)
print(coconutoil.color,workout.color,shampoo.color)
sched.addEvent(kombucha)
print(kombucha.color)
sched.getWeek()

sched.saveSchedule()

# cyclesNow = sched.findCyclePoint()
# print(cyclesNow)

# #Edit testing
# print([x.name for x in sched.egInfo])
# coconutoilNewStart = datetime.datetime(2018,6,21,22)
# coconutoilNewEnd = datetime.datetime(2019,6,21,22)
# coconutoil = eventgen.EventGen('coconut oil', coconutoilNewStart,coconutoilNewEnd,5)
# main.editEvent(sched.egInfo, coconutoil)
# print(coconutoil.freq,coconutoil.start,coconutoil.end)

# test = sched.getTimeFrame(datetime.datetime(2018,7,16), datetime.datetime.today())
# print([[x[0].name, x[1]] for x in test])
# print(len(test))
