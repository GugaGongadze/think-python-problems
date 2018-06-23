import time

current_time = time.time()

hours_since_epoch = current_time // 60 // 60
days_since_epoch = int(hours_since_epoch // 24)

current_hours = int(hours_since_epoch - (hours_since_epoch // 24) * 24)

minutes_since_epoch = current_time // 60
current_minutes = int(minutes_since_epoch - (minutes_since_epoch // 60) * 60)

seconds_since_epoch = current_time // 1
current_seconds = int(seconds_since_epoch - (minutes_since_epoch * 60))

print('Current time: ' + str(current_hours) + ':' + str(current_minutes) + ':' + str(current_seconds))
print('Days since the epoch: ' + str(days_since_epoch))