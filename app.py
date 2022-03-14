from flask import Flask

# All you need to start a flask app
app = Flask(__name__)

# adding routes

# you can add multiple routes for same
#@app.route('/index') - both routes lead to same place
@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)