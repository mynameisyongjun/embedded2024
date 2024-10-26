import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER, 261)
p.start(50)
p.stop()

try:
    while True:
        if GPIO.input(SW1) != 0: 
            p.start(50)
            p.ChangeFrequency(261)
            time.sleep(0.5)
            p.stop()
        elif GPIO.input(SW2) != 0: 
            p.start(50)
            p.ChangeFrequency(294)
            time.sleep(0.5)
            p.stop()
        elif GPIO.input(SW3) != 0:  
            p.start(50)
            p.ChangeFrequency(330)
            time.sleep(0.5)
            p.stop()
        elif GPIO.input(SW4) != 0:  
            p.start(50)
            p.ChangeFrequency(349)
            time.sleep(0.5)
            p.stop()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
