import sys
from Adafruit_PCA9685 import PCA9685
from multiprocessing.pool import ThreadPool
import sys
sys.path.insert(0, '../configs/')
import config

class ArmController(PCA9685):
	def __init__(self, freq=50):
		super().__init__()
		self.set_pwm_freq(freq)
		self.servo_channels = config.SERVO_CHANNELS
		self.servo_ranges = config.SERVO_RANGES
		self.servo_directions = config.SERVO_DIRECTIONS
		self.servo_keys = list(self.servo_channels.keys())
		self.current_positions = config.DEFAULT_STARTS.copy()
		self.set_all_joints(config.DEFAULT_STARTS)

	def set_joint(self, joint, pos):
		#not doing checks here for latency
		pos = int(pos)
		channel = self.servo_channels[joint]
		self.set_pwm(channel, 0, pos)
		self.current_positions[joint] = pos

	def convert_deg_to_pos(self, joint, deg):
		rng = self.servo_ranges[joint]
		direction = self.servo_directions[joint]
		#check me
		pos = deg*(rng[1]-rng[0])
		if direction == -1:
			pos=rng[1]-pos
		elif direction == 1:
			pos+=rng[0]
			
		return pos

	def convert_and_set(self, joint, deg):
		self.set_joint(joint=joint,
			pos=self.convert_deg_to_pos(joint, deg))
	
	def set_all_joints(self, command_dic):
		command_list = list(command_dic.items())
		pool = ThreadPool(len(self.servo_keys))
		pool.starmap(self.convert_and_set, command_list)
		pool.close()
		pool.join()