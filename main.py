import time
import machine
from machine import Pin

adc = machine.ADC(bits=10)
#Important that this pin is the same one as the sensor is conected to
tempPin = adc.channel(pin='P16')

#Same as above, remember pin numbers you used
ledOrange = Pin('P22', Pin.OUT, pull = Pin.PULL_DOWN)
ledGreen = Pin('P21', Pin.OUT, pull = Pin.PULL_DOWN)
ledRed = Pin('P20', Pin.OUT, pull = Pin.PULL_DOWN)



while True:
    millivolts = tempPin.voltage()
    celsius = (millivolts - 500.0) / 10.0

    if celsius < 23:
        ledOrange.value(1)
        ledGreen.value(0)
        ledRed.value(0)

    elif celsius > 28:
        ledOrange.value(0)
        ledGreen.value(0)
        ledRed.value(1)

    else:
        ledOrange.value(0)
        ledGreen.value(1)
        ledRed.value(0)

    pybytes.send_signal(1, celsius)
    print("sending: {}".format(celsius))
    #Send every 15 minutes
    time.sleep(900)