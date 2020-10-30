from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def get_form():
    return render_template("index.html", prompts = story.prompts)

@app.route("/story")
def return_story():
    return render_template("story.html", story = story.generate(request.args))