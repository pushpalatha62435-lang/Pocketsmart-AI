from flask import Flask, render_template
from routes.planners import planners
app = Flask(__name__)
app.register_blueprint(planners)
@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
