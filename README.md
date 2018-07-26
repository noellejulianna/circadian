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

        # weekday helper function
        def wname(n):
            if n == 0:
                return "Monday"
            elif n == 1:
                return "Tuesday"
            elif n == 2:
                return "Wednesday"
            elif n == 3:
                return "Thursday"
            elif n == 4:
                return "Friday"
            elif n == 5:
                return "Saturday"
            elif n == 6:
                return "Sunday"

        # label days on pie, rotate days for today to  be at the top,
        # a for loop could also be used
        current = datetime.datetime.today()
        today = self.bigFont.render(wname(current.weekday()), 100, DAYS)
        # rotate day name to be tangent to pie
        # rotate (surface, angle)
        rtd = pygame.transform.rotate(today, 0)
        # draws our day name surface
        window.blit(rtd, (self.td[0] +85, self.td[1]- 60))

        # today plus one    
        todayplus1 = self.bigFont.render(wname((current+datetime.timedelta(days=1)).weekday()), 100, DAYS)
        rtdplus1 = pygame.transform.rotate(todayplus1, 305)
        window.blit(rtdplus1, (self.tdplusone[0] + 90, self.tdplusone[1]+35))

        # today plus two           
        todayplus2 = self.bigFont.render(wname((current+datetime.timedelta(days=2)).weekday()), 100, DAYS)
        rtdplus2 = pygame.transform.rotate(todayplus2, 260)
        window.blit(rtdplus2, (self.tdplustwo[0], self.tdplustwo[1] + 90))

        # today plus threes
        todayplus3 = self.bigFont.render(wname((current+datetime.timedelta(days=3)).weekday()), 100, DAYS)
        rtdplus3 = pygame.transform.rotate(todayplus3, 210)
        window.blit(rtdplus3, (self.tdplusthree[0] - 130, self.tdplusthree[1] + 55))

        # today plus four
        todayplus4 = self.bigFont.render(wname((current+datetime.timedelta(days=4)).weekday()), 100, DAYS)
        rtdplus4 = pygame.transform.rotate(todayplus4, 160)
        window.blit(rtdplus4, (self.tdplusfour[0]- 180, self.tdplusfour[1] - 40))

        # today plus five
        todayplus5 = self.bigFont.render(wname((current+datetime.timedelta(days=5)).weekday()), 100, DAYS)
        rtdplus5 = pygame.transform.rotate(todayplus5, 105)
        window.blit(rtdplus5, (self.tdplusfive[0] - 100, self.tdplusfive[1] - 155))

        # today plus six
        todayplus6 = self.bigFont.render(wname((current+datetime.timedelta(days=6)).weekday()), 100, DAYS)
        rtdplus6 = pygame.transform.rotate(todayplus6, 60)
        window.blit(rtdplus6, (self.tdplusfive[0] - 75, self.tdplussix[1] - 155))