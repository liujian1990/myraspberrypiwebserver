#test for flask
from flask import Flask,url_for,render_template
import datetime

app = Flask(__name__)

@app.route('/')
def context():
    return "This liujian's website."

@app.route('/index')
def index():
    return "index"

@app.route('/login')
def login(): 
    now = datetime.datetime.now()
    nowtimeformat = now.strftime("%Y-%m-%d  %H:%M")
    templatedata = {
        'time' : nowtimeformat
    }
    return render_template('index.html', **templatedata)

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='lj')
    
if __name__ == "__main__":
    try:
        print "Start webserver."
        #app.run()
    	app.run(host="0.0.0.0", port=80,debug=True)
        print "A web Server end."  
    except Exception,e:
        print Exception,":",e
