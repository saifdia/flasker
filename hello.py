from flask import Flask, render_template



#Create an install of flask 
app = Flask(__name__)

#create a route decorator

''' Python filter with jinja using |
safe
capitalize
lower
upper
title
trim
striptages
'''
@app.route('/')
@app.route('/index')
def index():
    first_name="Saifoulaye"
    stuff="This is <strong>Bonld</strong> Text"
    stuff2="This is <strong>Bonld</strong> Text"
    
    favorite_pizza = ["Pepperoni", "Mazarita", "Reine", "4 fromage"]

    return render_template("index.html",
        first_name=first_name,
        stuff=stuff,
        stuff2=stuff2,
        favorite_pizza=favorite_pizza)

# # localhost:5000/user/John
# @app.route('/user/<name>')
# def user(name):
#     return "<h1>Hello {}<h1>".format(name)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

#Create custom error pages
#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    title="404 Error"
    return render_template("404.html",title=title), 404

#Internal server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


