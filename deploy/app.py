from flask import Flask
from flask import jsonify, request
import josn
from configs import config
from tools.PCA6685_LIBRARY import ArmController

app = Flask(__name__)

arm_robot = ArmController()


@app.route('/', methods=['GET'])
def get_angles():
    commands = request.get_json(force=True)
    arm_robot.



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)