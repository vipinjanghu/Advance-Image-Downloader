from flask import Flask,jsonify,request,render_template
from flask_cors import CORS, cross_origin
from collector import save_to_csv
from validate import validator
from scheduler import job
from apscheduler.schedulers.background import BackgroundScheduler




app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
    return render_template('home.html')

@app.route('/schd',methods=['POST'])
@cross_origin()
def sche():
    # if request.method==['Post']:
    name=request.form['name']
    datetime=request.form['datetime']
    email=request.form['email']
    status=validator(email)
    if status=="valid":
        save_to_csv(name,datetime,email)
        return render_template('final.html')
    else:
        return render_template('home1.html')



if __name__=='__main__':
    schd=BackgroundScheduler(daemon=True)
    schd.add_job(job,'interval',minutes=2)
    schd.start()
    app.run(debug=True)
