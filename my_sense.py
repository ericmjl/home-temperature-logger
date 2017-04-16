from sense_hat import SenseHat
from time import sleep
from tinydb import TinyDB, where
from datetime import datetime, timedelta

db = TinyDB('temperatures.database')

sense = SenseHat()

# sense.show_message(str(temperature))

def sleep_till_next_minute():
    curr_time = datetime.now()
    next_time = curr_time + timedelta(seconds=60-curr_time.second) - timedelta(microseconds=curr_time.microsecond)
    print('Current time: {0}'.format(curr_time))
    print('Next time: {0}'.format(next_time))
    td = next_time - curr_time
    sleep(td.total_seconds())

while True:
    curr_time = datetime.now()
    temperature = sense.get_temperature()
    print(temperature)
    db.insert({'year': curr_time.year, 'month': curr_time.month,
               'day': curr_time.day, 'hour': curr_time.hour,
               'minute': curr_time.minute, 'second': curr_time.second,
               'temperature': temperature})
    sleep_till_next_minute()
