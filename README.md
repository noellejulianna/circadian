# circadian
how the unpickled week works:
    week=[[firsteventname,datetime object of event],[secondeventname,datetime object of event],[thirdeventname,datetime object of event], etc]
    
    week[0]= all info on the first event
    week[1]= second set of info
    week[2]= third

    week[0][1] = date info on first event
        week[0][1].weekday() = weekday of that event (0 is Monday - 6 is Sunday)
        week[0][1].year = year of event
        week[0][1].month = month of event
        week[0][1].day = number date of event
        week[0][1].hour = hour time that the event occurs in the day
        week[0][1].minute = minute time that event occurs in the day
    

