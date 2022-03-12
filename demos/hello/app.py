# -*- coding: utf-8 -*-
'''
    :file: app.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2022/03/10 00:51:21
'''
from apiflask import APIFlask
app = APIFlask(__name__)

@app.route("/")
def index():
    return "Hello apiflask!"

@app.route('/hello/<name>')
def hello(name:str):
    return f'Hello {name}!'

@app.route('/say_hello', defaults={'name': 'farmer'})
@app.route('/say_hello/<name>')
def say_hello(name:str):
    return f'Hello {name}!'
