from flask import Flask, render_template, url_for, redirect, flash, get_flashed_messages
from forms import RegistrationForm, LoginForm
# import bcrypt

app = Flask(__name__)
app.secret_key = '4f057ce657d242729e1dd9ce096f6973'
app.config['SECRET KEY'] = '4f057ce657d242729e1dd9ce096f6973'
posts = [
    {
        'author' : 'Eugene',
        'title' : 'World',
        'content': 'First post content',
        'date_posted': 'November 17, 2023'
    }
]

# password = "user_password"
# hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            if form.email.data == 'admin@classified.com' and form.password.data == 'password':
                flash('You have been logged in as Admin', 'Success')
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)