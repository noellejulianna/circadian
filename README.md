# circadian
how the unpickled week works:
    week=[[1steventobject,datetime object of event],[2ndeventobject,datetime object of event],[3rdeventobject,datetime object of event], etc]
    
    week[0]= all info on the first event
    week[1]= second set of info
    week[2]= third

    week[0][0] = event info on first event
        week[0][0].name = the name of the habit
        #later on
        week[0][0].streak = event streak
        week[0][0].lateness = average lateness to the event
    
    week[0][1] = date info on first event
        week[0][1].weekday() = weekday of that event (0 is Monday - 6 is Sunday)
        week[0][1].year = year of event
        week[0][1].month = month of event
        week[0][1].day = number date of event
        week[0][1].hour = hour time that the event occurs in the day
        week[0][1].minute = minute time that event occurs in the day


#timing in the day is off!!!
