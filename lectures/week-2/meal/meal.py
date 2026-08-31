# breakfast 7-8 / 7-8 a.m.
# lunch 12-13 / 12-1 p.m.
# dinner 18-19 / 6-7 p.m.
# both start/end points inclusive
# assume input as #:## or ##:##
# extra challenge - include 12 hrs time #:## a.m./p.m. and ##:## a.m./p.m.

def main():
    time = input("enter time: ")
    time = convert(time)
    if(7 <= time <= 8):
        print('breakfast time')
    elif(12 <= time <= 13):
        print('lunch time')
    elif(18 <= time <= 19):
        print('dinner time')

# converts 'time', a 'str' in 24h format to a corresponding format numbers of hours as float
# ex - 7:30 as 7.5 hours
def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes)/60

if __name__ == "__main__":
    main()
