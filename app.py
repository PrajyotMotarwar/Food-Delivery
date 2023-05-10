from flask import Flask, render_template  
app=Flask(__name__)

@app.route("/") 
def index():
    return render_template('index.html') 

@app.route("/about")
def about(): 
    return render_template('about.html') 

@app.route("/menu")
def menu(): 
    return render_template('menu.html') 

@app.route("/review")
def review(): 
    return render_template('review.html') 

@app.route("/tracker")
def tracker(): 
    return render_template('tracker.html') 


if __name__ == "__main__":
    app.run(debug = True)  