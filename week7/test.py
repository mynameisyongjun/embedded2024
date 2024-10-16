import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lista = [0, 0, 0, 0]
lasts = [0, 0, 0, 0]

try:
    while True:
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)

        states = [sw1Value, sw2Value, sw3Value, sw4Value]

        if states[0] == 1 and lasts[0] == 0:
            lista[0] += 1
            print("SW1 click", lista[0])
        if states[1] == 1 and lasts[1] == 0:
            lista[1] += 1
            print("SW2 click", lista[1])
        if states[2] == 1 and lasts[2] == 0:
            lista[2] += 1
            print("SW3 click", lista[2])
        if states[3] == 1 and lasts[3] == 0:
            lista[3] += 1
            print("SW4 click", lista[3])

        lasts = states
        
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
