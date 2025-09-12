from flask import Flask,render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/Ball", methods = ["POST"])
def Ball():

    sez=["Da.","Ne.","Mogoče.","Vprašaj kasneje."]
    
    
    
    d=request.form
    ime1 =d.get("ime1").lower()

    if ime1[-1] == "!":
        rez = "Ne kriči."
        return render_template("index.html",rezultat = rez)

    if "ljubezen" in ime1:
        rez = "Kupi raje GPU."
        return render_template("index.html",rezultat = rez)
    
    if "vikend" in ime1:
        rez = "TikTok all day."
        return render_template("index.html",rezultat = rez)

    if "denar" in ime1:
        rez = "Burek only."
        return render_template("index.html",rezultat = rez)

    if "profesor" in ime1:
        rez = "F speedrun."
        return render_template("index.html",rezultat = rez)

    


    else:
        rez =  random.choice(sez)
        return render_template("index.html",rezultat = rez)
            


app.run(debug=True)