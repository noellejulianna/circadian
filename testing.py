import eventgen
import schedule
import datetime
import history

workoutstart = datetime.datetime(2018,7,1,17,30)
workoutend = datetime.datetime(2019,7,1,17,30)
workout = eventgen.EventGen('workout',workoutstart,workoutend,2)

shampoostart = datetime.datetime(2018,7,15,19,00)
shampooend = datetime.datetime(2019,7,15,19,00)
shampoo = eventgen.EventGen('shampoo',shampoostart,shampooend,5)

schedulestart = datetime.datetime(2018,8,1)
scheduleend = datetime.datetime(2018,8,31)
sched = schedule.Schedule(workout,schedulestart,scheduleend)
sched.egInfo.append(shampoo)

sched.createSchedule()