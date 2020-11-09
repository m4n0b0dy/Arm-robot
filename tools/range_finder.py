from PCA9685_LIBRARY import *
import time
arm_robot = ArmController()
SERVO_RANGES = {
}

completed = []
for joint, rng in SERVO_RANGES.items():
	desc=10
	if joint in completed:
		continue
	direction = config.SERVO_DIRECTIONS[joint]
	if direction == -1:
		rng = (rng[1],rng[0])
		desc*=-1
	for pos in range(rng[0],rng[1],desc):
		print(joint, pos)
		arm_robot.set_joint(joint,pos)
		time.sleep(.1)
	input("Continue?")