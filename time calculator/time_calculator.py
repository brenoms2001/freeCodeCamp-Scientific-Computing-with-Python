def weekday_name_number(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    elif day == "Sunday":
        return 6

def weekday_number_name(day):
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"

def add_time(start_time, duration_time, day=None):
    #Copy the hour of start
    hour_start = start_time[: start_time.find(":")]
    hour_start = int(hour_start)

    #Copy the minute of start
    minute_start = start_time[-5 : start_time.find("M")-1]
    minute_start = int(minute_start)

    #Copy the new_turn (AM/PM)
    turn = start_time[-2 : ]
    new_turn = turn[:]

    #Copy the hour added
    hour_added = duration_time[0 : duration_time.find(":")]
    hour_added = int(hour_added)

    #Copy the minutes added
    minute_added = duration_time[-2 : ]
    minute_added = int(minute_added)
    
    #The sum of minutes
    new_minute = (minute_start + minute_added)

    #The hours resulted by the sum of minutes
    extra_hour = int(new_minute / 60)

    #Format the minutes 
    new_minute -= int(extra_hour * 60)

    #The sum of hours
    new_hour = int(hour_start + hour_added + extra_hour)

    #print(f"{new_hour}:{new_minute} {new_turn}")

    if new_hour > 24:
        days_later = int(new_hour / 24)
        new_hour -= int(days_later * 24)
    else:
        days_later = 0

    if turn == "AM" and new_hour > 12:
        new_hour -= 12
        new_turn = "PM"

    elif turn == "AM" and new_hour == 12:
        new_turn = "PM"

    elif turn == "PM" and new_hour > 12:
        new_hour -= 12
        new_turn = "AM"

    elif turn == "PM" and new_hour == 12:
        new_turn = "AM"
    
    if new_turn:
        if turn == "PM" and new_turn == "AM":
            days_later += 1

    new_day = None
    if day:
        new_day = (weekday_name_number(day) + days_later) % 6
        new_day = weekday_number_name(new_day)
    
    if new_day and days_later:
        time = f"{new_hour}:{new_minute:02} {new_turn}, {new_day} ({days_later} days later)"
        return print(time)
    elif days_later > 1:
        time = f"{new_hour}:{new_minute:02} {new_turn} ({days_later} days later)"
        return print(time)
    elif days_later == 1:
        time = f"{new_hour}:{new_minute:02} {new_turn} (next day)"
        return print(time)
    elif new_day:
        time = f"{new_hour}:{new_minute:02} {new_turn}, {new_day}"
        return print(time)
    else:
        time = f"{new_hour}:{new_minute:02} {new_turn}"
        return print(time)

def weekday_name_number(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    elif day == "Sunday":
        return 6

def weekday_number_name(day):
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"

def add_time(start_time, duration_time, day=None):
    #Copy the hour of start
    hour_start = start_time[: start_time.find(":")]
    hour_start = int(hour_start)

    #Copy the minute of start
    minute_start = start_time[-5 : start_time.find("M")-1]
    minute_start = int(minute_start)

    #Copy the new_turn (AM/PM)
    turn = start_time[-2 : ]
    new_turn = turn[:]

    #Copy the hour added
    hour_added = duration_time[0 : duration_time.find(":")]
    hour_added = int(hour_added)

    #Copy the minutes added
    minute_added = duration_time[-2 : ]
    minute_added = int(minute_added)
    
    #The sum of minutes
    new_minute = (minute_start + minute_added)

    #The hours resulted by the sum of minutes
    extra_hour = int(new_minute / 60)

    #Format the minutes 
    new_minute -= int(extra_hour * 60)

    #The sum of hours
    new_hour = int(hour_start + hour_added + extra_hour)

    #print(f"{new_hour}:{new_minute} {new_turn}")

    if new_hour > 24:
        days_later = int(new_hour / 24)
        new_hour -= int(days_later * 24)
    else:
        days_later = 0

    if turn == "AM" and new_hour > 12:
        new_hour -= 12
        new_turn = "PM"

    elif turn == "AM" and new_hour == 12:
        new_turn = "PM"

    elif turn == "PM" and new_hour > 12:
        new_hour -= 12
        new_turn = "AM"

    elif turn == "PM" and new_hour == 12:
        new_turn = "AM"
    
    if new_turn:
        if turn == "PM" and new_turn == "AM":
            days_later += 1

    new_day = None
    if day:
        new_day = (weekday_name_number(day.title()) + days_later) % 7
        new_day = weekday_number_name(new_day)
    
    if new_day and days_later == 1:
        time = f"{new_hour}:{new_minute:02} {new_turn}, {new_day} (next day)"
        return time
    elif new_day and days_later > 1:
        time = f"{new_hour}:{new_minute:02} {new_turn}, {new_day} ({days_later} days later)"
        return time
    elif days_later > 1:
        time = f"{new_hour}:{new_minute:02} {new_turn} ({days_later} days later)"
        return time
    elif days_later == 1:
        time = f"{new_hour}:{new_minute:02} {new_turn} (next day)"
        return time
    elif new_day:
        time = f"{new_hour}:{new_minute:02} {new_turn}, {new_day}"
        return time
    else:
        time = f"{new_hour}:{new_minute:02} {new_turn}"
        return time