from flask import Flask
from flask import request
import os
app = Flask(__name__)

@app.route('/')
def main():
    pdf = request.args.get('pdf')
    kindle = request.args.get('kindle')
    if pdf!=None:
        pdf = pdf.replace("\s"," ")
        cmd = "open " + "'"+pdf+"'"
        os.system(cmd)
    elif kindle!=None:
        asin = kindle
        basecmd = 'kindle://book?action=open&asin=' + asin
        cmd = "open " + "'"+basecmd+"'"
        app.logger.info(cmd)
        os.system(cmd)
    return "" 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=int(os.getenv('PORT',4568)))
