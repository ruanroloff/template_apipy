
# third-party imports
import os
import urllib.request
from flask import Flask

#internal
from app import main
app = main.create_app()

from app.swagger import swagger
from app.swagger import user

##### BEGIN GLOBAL HTTP CONFIGURATIONS

@app.route("/myip")
def ip_page():
    url = 'http://ifconfig.me/ip'
    external_ip = urllib.request.urlopen(url).read().decode('utf8')
    return 'You connected from IP address: ' + external_ip



### END GLOBAL HTTP CONFIGURATIONS

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)