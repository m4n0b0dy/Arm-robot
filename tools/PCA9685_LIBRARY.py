import sys
import Adafruit_PCA9685
from Adafruit_PCA9685 import PCA9685
from multiprocessing.pool import ThreadPool
from configs import config

class ArmController(PCA9685):
	def __init__(self, freq=50):
		self.set_pwm_freq(freq)
		self.servo_channels = config.SERVO_CHANNELS
		self.servo_ranges = config.SERVO_RANGES
		self.servo_keys = list(self.servo_channels.keys())
		self.set_all_joints(config.DEFAULT_STARTS)
		self.current_positions = config.DEFAULT_STARTS.copy()

	def set_joint(self, joint, pos):
		#not doing checks here for latency
		channel = self.servo_channels[joint]
		self.set_pwm(channel, 0, pos)
		self.current_positions[joint] = pos

	def convert_deg_to_pos(self, joint, deg):
		rng = self.servo_ranges[joint]
		return deg*(rng[1]-rng[0])+rng[0]

	def convert_and_set(self, joint, deg):
		pos = self.convert_deg_to_pos(deg, joint)
		self.set_joint(self, joint, pos)
	
	def set_all_joints(self, command_dic):
		command_list = list(command_dic.items())
		pool = ThreadPool(len(self.servo_keys))
		pool.map(self.convert_and_set, *zip(*command_list))
		pool.close()
		pool.join()