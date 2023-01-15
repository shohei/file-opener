from flask import Flask
from flask import request
import os
app = Flask(__name__)

@app.route('/')
def main():
    pdf = request.args.get('pdf')
    if pdf==None:
        pdf = ""
    cmd = "open " + pdf
    os.system(cmd)
    return "" 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT',4568)))
