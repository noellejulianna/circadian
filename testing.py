import eventgen
import schedule
import datetime
import pickle

workoutstart = datetime.datetime(2018,7,1,17,30)
workoutend = datetime.datetime(2019,7,1,17,30)
workout = eventgen.EventGen('workout',workoutstart,workoutend,2)

shampoostart = datetime.datetime(2018,7,15,19,00)
shampooend = datetime.datetime(2019,7,15,19,00)
shampoo = eventgen.EventGen('shampoo',shampoostart,shampooend,5)

coconutoilstart = datetime.datetime(2018,6,19,12,30)
coconutoilend = datetime.datetime(2019,6,19,12,30)
coconutoil = eventgen.EventGen('coconut oil',coconutoilstart,coconutoilend,7)

sched = schedule.Schedule([coconutoil,workout,shampoo])
sched.getWeek()

sched.saveSchedule()
