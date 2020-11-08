import sys
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
pwm.set_pwm(0,0,200)
pwm.set_pwm(2,0,200)