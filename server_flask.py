from flask import Flask, render_template, request

########################
### Step 1:  Declare session scope variables & methods
app = Flask(__name__)


########################
### Step 2:  Build an Flask app to render each HTML page
###    @apps are the Flask object for HTML pages
###    Define an @app for each HTML page
###       1. '/' is the homepage
###       2. '/result' is the nearly identical page but with

### Step 2a: Render the home_screen
########
@app.route('/')
def home_screen():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
