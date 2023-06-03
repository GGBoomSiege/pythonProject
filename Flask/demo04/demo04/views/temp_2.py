from flask import Blueprint

temp_2 = Blueprint('temp_2', __name__)

@temp_2.route('/app_2')
def app_2():
    return 'app_2'