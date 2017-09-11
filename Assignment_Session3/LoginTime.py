import datetime

time = datetime.datetime.strptime(input('Input Time in HHMM Format: '), "%H%M")

if time.hour>=0 and time.hour<12:
    print("Good Morninig!:)")
elif time.hour>12 and time.hour<=6:
    print("Good Afternoon")
elif time.hour>6:
    print("Good Evening")