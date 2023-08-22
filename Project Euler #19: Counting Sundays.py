# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #19: Counting Sundays
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler019/problem?isFullScreen=true

months = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}


# tells whether an year is a leap year
def is_leap_year(year):
    active = False
    if year % 100 == 0:
        if year % 400 == 0:
            active = True
    else:
        if year % 4 == 0:
            active = True
    return active


# number of odd days for that number of years
years = {0: 0, }
od = 0
for i in range(1, 400):
    if is_leap_year(i):
        od += 2
    else:
        od += 1
    od = od % 7
    years[i] = od


# tells whether a given date of "YYYY MM DD" format had sunday on it.
def day_calc(st):
    odd_days = 0
    item = st.split()
    year = int(item[0])
    mon = int(item[1])
    day = int(item[2])
    odd_days += day
    odd_days += months[mon]
    if is_leap_year(year) and mon > 2:
        odd_days += 1
    year = (year - 1) % 400
    odd_days += years[year]
    if odd_days % 7 == 0:
        return True
    else:
        return False


# now my recipes are ready, and I just have to calc dates between start and end date and use my day_calc function on them

for _ in range(int(input())):
    strt_date = input().strip()
    end_date = input().strip()
    dates = []
    item = strt_date.split()
    day = int(item[2])
    month = int(item[1])
    year = int(item[0])

    if day == 1:
        dates.append(f'{year} {month} {day}')
    day = 1
    e_item = end_date.split()
    e_day = int(e_item[2])
    e_month = int(e_item[1])
    e_year = int(e_item[0])
    while True:
        if month == 12:
            month = 0
            year += 1
        month += 1
        date = f"{year} {month} {day}"
        if year > e_year:
            break
        elif year == e_year:
            if month > e_month:
                break
        dates.append(date)

    res = 0
    for i in dates:
        if day_calc(i):
            res += 1
    print(res)