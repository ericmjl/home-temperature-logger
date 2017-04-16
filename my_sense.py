from sense_hat import SenseHat as SH
from time import sleep, now
from tinydb import TinyDB, where

db = TinyDB('temperatures.database')

sense = SH()

# sense.show_message(str(temperature))

while True:
    temperature = sense.get_temperature()
    print(temperature)
    sleep(1)
