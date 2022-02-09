from datetime import datetime
from playsound import playsound

# playsound('audio.mp3')

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
# print(alarm_hour)
alarm_minute = alarm_time[3:5]
# print(alarm_minute)
alarm_seconds = alarm_time[6:8]
# print(alarm_seconds)
alarm_period = alarm_time[9:11].upper()
# print(alarm_period)
print("Setting up alarm..")
while True:
    now = datetime.now()
    # print(now)
    current_hour = now.strftime("%I")
    # print(current_hour)
    current_minute = now.strftime("%M")
    # print(current_minute)
    current_seconds = now.strftime("%S")
    # print(current_seconds)
    current_period = now.strftime("%p")
    # print(current_period)
    if alarm_period == current_period:
        # print(alarm_period)
        # print(current_period)
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break
