#!/home/asier/anaconda3/bin/python
# /usr/bin/python3

'''
#  pip install flask flask_restful 
# Hauek ez det uste beharko direnik: flask_sqlalchemy flask_migrate flask_marshmallow marshmallow-sqlalchemy

# Android rest client:
# https://play.google.com/store/apps/details?id=com.app.restclient&hl=es&gl=US
'''

# Sudo-rekin zer egin?¿

import os
  
#from flask import Flask
from flask import Flask
app = Flask(__name__)


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    result= os.system("sudo halt")# "shutdown -s 1  ")
    return "cmd result "+str(result)

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    result= os.system("sudo reboot") # "shutdown /r /t 1")
    return "cmd result:"+str(result)

@app.route('/service/shutdown', methods=['GET', 'POST'])
def serviceShutdown():
    from flask import request
    service = request.args['service']
    result =os.system("sudo systemctl shutdown "+service)
    return "Command result:"+str(result)

@app.route('/service/start', methods=['GET', 'POST'])
def serviceStart():
    from flask import request
    service = request.args['service']
    result = os.system("sudo systemctl start "+service)
    return "cmd result:"+str(result)

@app.route('/service/restart', methods=['GET', 'POST'])
def serviceRestart():
    from flask import request
    service = request.args['service']
    result= os.system("sudo systemctl restart "+service)
    return "cmd result:"+str(result)
    
@app.route('/service/hello', methods=['GET'])
def hello():
    print('hello')
    from flask import request
    args= request.args
    term=args['term']
    return "Hello "+term

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9080)
