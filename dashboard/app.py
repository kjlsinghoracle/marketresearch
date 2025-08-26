from flask import Flask, render_template_string
from storage import db

app = Flask(__name__)

@app.route("/")
def index():
    entries = db.fetch_all()
    html = "<h1>Market Research Dashboard</h1><table border=1><tr><th>Company</th><th>Use Cases</th><th>Differentiators</th><th>Strategy</th><th>Pricing</th><th>Date</th></tr>"
    for e in entries:
        html += f"<tr><td>{e[1]}</td><td>{e[2]}</td><td>{e[3]}</td><td>{e[4]}</td><td>{e[5]}</td><td>{e[6]}</td></tr>"
    html += "</table>"
    return html

if __name__ == "__main__":
    app.run(debug=True)