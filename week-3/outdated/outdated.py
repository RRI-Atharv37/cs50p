MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

# input in month-day-year ex - 9/8/1636 or September 8, 1636
# output it as YYYY-MM-DD
# if its not in valid date format, reprompt
# assume each month has 31 days
def main():
    while True:
        try:
            date = input("Date: ").lstrip().rstrip()
            if not validate_date(date): continue

            if '/' in date:
                month,day,year = date.split('/')
                print(f"{year.strip()}-{int(month):02}-{int(day):02}", end='')
                break
            elif ',' in date:
                md,year = date.split(',')
                month, day = md.strip().split(' ')
                print(f"{year.strip()}-{int(MONTHS[month]):02}-{int(day):02}", end='')
                break
        except (ValueError, KeyError):
            pass

def validate_date(date): 
    month,day,year = date.replace('/', '-').replace(' ', '-').replace(',', '').split('-')
    # print(f"month: {month}")
    # print(f"day: {day}")
    # print(f"year: {year}")

    if month.isdigit():
        if not 1<=int(month)<=12: return False
    elif month not in MONTHS:
        return False
    if not 1<=int(day)<=31:
        return False
        
    return True
    # try:
    #     month,day,year = date.replace('/', '-').replace(' ', '-').replace(',', '').split('-')

    #     if not 1<=int(day)<=31:
    #         return False
    #     if month.isdigit():
    #         if not 1<=int(month)<=12: return False
    #     elif month not in MONTHS:
    #         return False
        
    #     return True
    # except (ValueError, KeyError):
    #     return False

main()

        # date = input("Date:  ").strip() # 9/8/1636 or sept8,1636
        # month,day,year = date.split('/')

        # date = input("Date: ").replace('/', '-').replace(' ', '-')
        # month,day,year = date.split('-')

"""
        month,day,year = input("Date: ").replace('/', '-').replace(' ', '-').replace(',', '').split('-')
        if not 1 <= int(day) <= 31:
            break

        if month in MONTHS:
            print(f"{year}-{int(MONTHS[month]):02}-{int(day):02}")
            break
        elif 1 <= int(month) <= 12:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except KeyError:
        pass
"""

        # for const in date:
        #     if not const.isalnum:
        #         # eg - 9/8/1636 becomes 9-8-1636 or sept 8, 1636 becomes sept 8-1636
        #         const.replace(const, '-')


