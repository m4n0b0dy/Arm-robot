import sys
sys.path.insert(0, '../tools/')
from PCA9685_LIBRARY import ArmController
arm_robot = ArmController()
print(arm_robot.current_degrees)
