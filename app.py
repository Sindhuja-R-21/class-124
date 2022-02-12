from flask import Flask


#app- object for Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/abc')
def hi_world():
    return "hi World"

@app.route('/divya')
def divya_world():
    return "hi Divya"


if(__name__=="__main__"):
    app.run(debug=True)
