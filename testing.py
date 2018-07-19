import eventgen
import schedule
import datetime
import history
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

schedulestart = datetime.datetime(2018,8,1)
scheduleend = datetime.datetime(2018,8,31)
sched = schedule.Schedule(workout,schedulestart,scheduleend)
sched.egInfo.append(shampoo)
sched.egInfo.append(coconutoil)

with open('fuile.txt', 'w+') as f:
    p = pickle.dumps(sched)
    f.write(p)

    pickle.dump(sched, f)

s = pickle.load()

s.createSchedule()