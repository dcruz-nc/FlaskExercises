from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

organizations = ["Hacking Club", "Futsal Club", "Flag Football Club", "Chess Club", "Tennis Club"]


registered_users = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        
        registered_users[name] = organization
        
        return redirect(url_for('registered_users_list'))

    return render_template('index.html', organizations=organizations)

@app.route('/registered_users')
def registered_users_list():
    return render_template('registered_users.html', users=registered_users)

if __name__ == "__main__":
    app.run(debug=True)
