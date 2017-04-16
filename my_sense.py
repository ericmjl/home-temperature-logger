from sense_hat import SenseHat
from time import sleep, now
from tinydb import TinyDB, where
from datetime import datetime

db = TinyDB('temperatures.database')

sense = SenseHat()

# sense.show_message(str(temperature))

while True:
    curr_time = datetime.now()
    temperature = sense.get_temperature()
    print(temperature)
    db.insert({'time': curr_time, 'temperature': temperature})
    sleep(1)
