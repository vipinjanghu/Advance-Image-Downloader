from flask import Flask,jsonify,request,render_template
from flask_cors import CORS, cross_origin
from collector import save_to_csv
from validate import validator
from scheduler import job
from apscheduler.schedulers.background import BackgroundScheduler




app = Flask(__name__)
# Define a route for the home page
@app.route('/')
@cross_origin()
def index():
    """ Home page of our Interface
    """
    return render_template('home.html')

# Define a route for scheduling
@app.route('/schd',methods=['POST'])
@cross_origin()
def sche():
    """
    Collect the data fromt the user
    """
    name=request.form['name']
    date_time=request.form['date_time']
    email=request.form['email']
    status=validator(email)
    if status=="valid":
        save_to_csv(name,date_time,email)
        return render_template('final.html')
    else:
        return render_template('home1.html')



if __name__=='__main__':
    # Create a background scheduler
    schd=BackgroundScheduler(daemon=True)
    # Add the job to the scheduler
    schd.add_job(job,'interval',minutes=1)
    schd.start()
    # Run the Flask app
    app.run(debug=True)
