from flask import Flask
from flask import jsonify, request
import json
import sys
sys.path.insert(0, '../configs/')
import config

sys.path.insert(0, '../tools/')
import config
from PCA9685_LIBRARY import ArmController

app = Flask(__name__)

arm_robot = ArmController()

@app.route('/', methods=['POST'])
def set_angles():
	commands = request.get_json(force=True)
	#arm_robot.set_all_joints(commands)
	msg = 'Set'+str(commands)
	print(msg)
	return msg
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5005, debug=True)