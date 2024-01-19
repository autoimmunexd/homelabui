from flask import Flask, render_template, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from uptime import uptime
from software_list import apps
import psutil
import logging
from scrape import scrape_wikipedia_main_page
from weather import get_weather_data
from storage import storage
from bandwidth import get_bandwidth

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')

#EXAMPLE OF WRONG WAY TO PASS DATA WITH THESE TWO ROUTES
@app.route('/wiki')
def wiki():
     wiki = scrape_wikipedia_main_page()
     return render_template('dashboard.html', wiki=wiki)

@app.route('/weather')
def weather():
    ui_data = get_weather_data()
    return ui_data

@app.route('/storage')
def storageroute():
    storage_data = storage()
    return storage_data

@app.route('/bandwidth')
def bandwidthroute():
    bandwidth_usage = get_bandwidth()
    print(bandwidth_usage)
    return bandwidth_usage

#TO DO LIST :
    #download upload in mb
    #disk free space used space
    #time day date
    #start, stop, restart and status of docker container
    #pass data from docker to applicationlist

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html', apps=apps)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/uptime')
def server_up():
    server_up = uptime()
    return server_up

@app.route('/utilization')
def utilization():
    cpu = f"CPU utilization: {psutil.cpu_percent()}%"
    mem = f" \n Memory utilization: {psutil.virtual_memory().percent}%"
    return jsonify({'cpu': cpu, 'mem': mem})

@app.route('/plex')
def plex():
    return redirect("https://app.plex.tv/desktop/?_gl=1*1n8rd66*_ga*NTQwNTQwMTkzLjE3MDIwNjU1NTY.*_ga_G6FQWNSENB*MTcwMzA3NjA0Ny4zLjEuMTcwMzA3NjEyMi42MC4wLjA.#!/media/b58766b8d9e142033a9dea6f927eca5df97dead7/com.plexapp.plugins.library?source=2")

@app.route('/portainer')
def portainer():
    return redirect("https://192.168.1.144:9443/#!/auth")

@app.route('/overseerr')
def overseerr():
    return redirect("https://192.168.1.144:5055")

@app.route('/radarr')
def radarr():
    return redirect("http://192.168.1.144:7878/")

@app.route('/sonarr')
def sonarr():
    return redirect("http://192.168.1.144:8989/")

@app.route('/lidarr')
def lidarr():
    return redirect("http://192.168.1.144:8686/")

@app.route('/metube')
def metube():
    return redirect("http://192.168.1.144:8081/")

@app.route('/prowlarr')
def prowlarr():
    return redirect("http://192.168.1.144:9696")

@app.route('/qbittorrent')
def qbittorrent():
    return redirect("http://192.168.1.144:8085")

@app.route('/proxmox')
def proxmox():
    return redirect("http://192.168.1.199:8006")

@app.route('/opnsense')
def opnsense():
    return redirect("http://192.168.1.1")

@app.route('/syncthing')
def syncthing():
    return redirect("http://192.168.1.144:8384")

if __name__ == "__main__":
    app.run(debug=False)