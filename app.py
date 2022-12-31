import json

from flask import Flask,render_template,request
import requests
# requests : We use this module (Library) to hit on API & in return we get JSON data
# request : function in flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('profile.html')



@app.route('/team-vs-team')
def team_vs_team():
    # we use again below code coz when we will run this code without below code then the team name will disappear from the dropdown
    response = requests.get('http://127.0.0.1:5000/api/teams')
    # below code is used to show what is inside the given URL & using ['teams'] I will get teams name in a list
    teams_list = response.json()['teams']

    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response1 = requests.get('http://127.0.0.1:5000/api/teamvsteam?team1={}&team2={}'.format(team1, team2))
    response1 = response1.json()

    return render_template('teamvteam.html', teams=sorted(teams_list), result=response1)




@app.route('/team-record')
def team_record():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams_list = response.json()['teams']

    team_ = request.args.get('team')
    response = requests.get('http://127.0.0.1:5000/api/team-record?team={}'.format(team_))

    response = response.json()

    return render_template('teamrecord.html', teams=sorted(teams_list), result=response)




@app.route('/batsman-record')
def batsman_record():
    response = requests.get('http://127.0.0.1:5000/api/batsmans')
    batsmans_list = response.json()['batsman']

    batsman_ = request.args.get('batsman')
    response = requests.get('http://127.0.0.1:5000/api/batsman-record?batsman={}'.format(batsman_))

    response = response.json()

    return render_template('batsmanrecord.html', teams=sorted(batsmans_list), result=response)




@app.route('/bowler-record')
def bowler_record():
    response = requests.get('http://127.0.0.1:5000/api/bowlers')
    bowlers_list = response.json()['bowler']

    bowler_ = request.args.get('bowler')
    response = requests.get('http://127.0.0.1:5000/api/bowler-record?bowler={}'.format(bowler_))

    response = response.json()

    return render_template('bowlerrecord.html', teams=sorted(bowlers_list), result=response)



# we are running this website on port 7000 not on 5000
app.run(debug=True,port=7000)