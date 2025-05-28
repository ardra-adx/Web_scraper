from flask import Flask, render_template
from scraper import scrape_remoteok_jobs

app = Flask(__name__)

@app.route("/")
def home():
    jobs = scrape_remoteok_jobs()
    return render_template("dashboard.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
