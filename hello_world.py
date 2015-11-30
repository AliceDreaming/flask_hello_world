from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template_hello.html', your_name=name.title())

@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
    jedi = last_name.title()[0:3]+first_name[0:2]
    return render_template('template_jedi.html', name_first=first_name.title(), name_last=last_name.title(), jedi_name=jedi)
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            