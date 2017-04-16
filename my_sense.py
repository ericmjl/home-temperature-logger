from sense_hat import SenseHat
from time import sleep
from tinydb import TinyDB, where
from datetime import datetime

db = TinyDB('temperatures.database')

sense = SenseHat()

# sense.show_message(str(temperature))

while True:
    curr_time = datetime.now()
    temperature = sense.get_temperature()
    print(temperature)
    db.insert({'year': curr_time.year, 'month': curr_time.month,
               'day': curr_time.day, 'hour': curr_time.hour,
               'minute': curr_time.minute, 'second', curr_time.second,
               'temperature': temperature})
    sleep(1)
