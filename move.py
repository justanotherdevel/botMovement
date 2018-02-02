import curses, time
import RPi.GPIO as gpio

# Left Motor (forward, backward, enable)
lF = 0
lB = 1
lE = 2

# Right Motor (forward, backward, enable)
rF = 3
rB = 4
rE = 5

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(left, gpio.OUT)
gpio.setup(right, gpio.OUT)

# Set up PWM for the motors
pwmL = gpio.PWM(lE, 100)
pwmR = gpio.PWM(rE, 100)

def switch_on(pin_number):
    gpio.output(pin_number, 1)
    
def switch_off(pin_number):
    gpio.output(pin_number, 0)

def forward():
    pwmL.ChangeDutyCycle(80)
    pwmR.ChangeDutyCycle(80)
    switch_off(rB)
    switch_off(lB)
    switch_on(rF)
    switch_on(rE)
    switch_on(lF)
    switch_on(lE)

def backward():
    pwmL.ChangeDutyCycle(80)
    pwmR.ChangeDutyCycle(80)
    switch_on(rB)
    switch_on(lB)
    switch_off(rF)
    switch_on(rE)
    switch_off(lF)
    switch_on(lE)

def softRight():
    pwmL.ChangeDutyCycle(50)
    pwmR.ChangeDutyCycle(0)
    switch_off(lB)
    switch_on(lF)
    switch_on(lE)
    switch_off(rF)
    switch_off(rB)
    switch_off(rE)

def softLeft():
    pwmR.ChangeDutyCycle(50)
    pwmL.ChangeDutyCycle(0)
    switch_off(rB)
    switch_on(rF)
    switch_on(rE)
    switch_off(lF)
    switch_off(lB)
    switch_off(lE)

def hardRight():
    pwmL.ChangeDutyCycle(50)
    pwmR.ChangeDutyCycle(50)
    switch_off(lB)
    switch_on(lF)
    switch_on(lE)
    switch_off(rF)
    switch_on(rB)
    switch_on(rE)

def hardLeft():
    pwmR.ChangeDutyCycle(50)
    pwmL.ChangeDutyCycle(50)
    switch_off(rB)
    switch_on(rF)
    switch_on(rE)
    switch_off(lF)
    switch_on(lB)
    switch_on(lE)

def leftForward():
    pwmR.ChangeDutyCycle(80)
    pwmL.ChangeDutyCycle(40)
    switch_off(rB)
    switch_off(lB)
    switch_on(rF)
    switch_on(lF)
    switch_on(rE)
    switch_on(lE)

def rightForward():
    pwmL.ChangeDutyCycle(80)
    pwmR.ChangeDutyCycle(40)
    switch_off(rB)
    switch_off(lB)
    switch_on(rF)
    switch_on(lF)
    switch_on(rE)
    switch_on(lE)

def leftBackward():
    pwmR.ChangeDutyCycle(80)
    pwmL.ChangeDutyCycle(40)
    switch_off(rF)
    switch_off(lF)
    switch_on(rB)
    switch_on(lB)
    switch_on(rE)
    switch_on(lE)

def rightBackward():
    pwmL.ChangeDutyCycle(80)
    pwmR.ChangeDutyCycle(40)
    switch_off(rF)
    switch_off(lF)
    switch_on(rB)
    switch_on(lB)
    switch_on(rE)
    switch_on(lE)

def stop():
    pwmL.ChangeDutyCycle(0)
    pwmR.ChangeDutyCycle(0)
    switch_off(rF)
    switch_off(rB)
    switch_off(rE)
    switch_off(lF)
    switch_off(lB)
    switch_off(lE)

def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)

if __name__ == "__main__":
    pwmL.start(100)
    pwmR.start(100)
    ch = 'a'
    while (ch != 'q'):
        ch = input_char("")
        if ch == 'A':
            forward()
        elif ch == 'D':
            softLeft()
        elif ch == 'B':
            backward()
        elif ch == 'C':
            softRight()
        else:
            stop()
