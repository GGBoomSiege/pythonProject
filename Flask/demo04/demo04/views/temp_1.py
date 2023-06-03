from flask import Blueprint

temp_1 = Blueprint('temp_1', __name__)

@temp_1.route('/app_1')
def app_1():
    return 'app_1'