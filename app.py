from flask import Flask, render_template

# All you need to start a flask app
app = Flask(__name__)

# adding routes

# you can add multiple routes for same
@app.route('/index') # both routes lead to same place
@app.route('/')
def index():
    return render_template('index.html', current_title = 'Custom Title')

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)