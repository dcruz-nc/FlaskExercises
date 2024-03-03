from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            if number % 2 == 0:
                result = "Even number"
            else:
                result = "Odd number"
        except ValueError:
            result = "Not an integer"
        return redirect(url_for('result', result=result))
    return render_template('index.html')

@app.route('/result')
def result():
    result = request.args.get('result')
    if result:
        return render_template('valid.html', result=result)
    else:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)
