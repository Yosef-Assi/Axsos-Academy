from flask import Flask, render_template 
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again", 404

@app.route('/')                           
def hello_world():
    
    return ("Hello World")
@app.route('/dojo')
def hello_woorld():
   
  
    return ("Hello Dojo")
@app.route("/say/<name>")
def hello_person(name):
   return (f"Hi {name}")

@app.route('/repeat/<times>/<name1>')
def add1(times,name1):
    return (f' {name1}'*int(times))




if __name__=="__main__":
    app.run(debug=True)   