from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')
    return render_template('index.html', current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
