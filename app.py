from flask import Flask,render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/Ball", methods = ["POST"])
def Ball():

    sez=["Da","Ne","Mogoče","Vprašaj kasneje"]
    
    
    
    d=request.form
    ime1 =d.get("ime1").lower()

        
    
    rez =  random.choice(sez)
    return render_template("index.html",rezultat = rez)
           


app.run(debug=True)