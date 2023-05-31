def add_time(start, duration, start_day=None):
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if period == 'PM':
        start_hour += 12

    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    period = 'AM' if new_hour < 12 else 'PM'

    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12
        days_later = total_minutes // (24 * 60)

    if start_day:
        start_day = start_day.lower()
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index].capitalize()
        new_time = f'{new_hour:02d}:{new_minute:02d} {period}, {new_day}'
    else:
        new_time = f'{new_hour:02d}:{new_minute:02d} {period}'

    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    return new_time


if __name__ == "__main__":
    
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))

