 
from flask import Flask
from bs4 import BeautifulSoup 
import requests 
  
app = Flask(__name__) 

@app.route("/") 
def home(): 
    html_text = requests.get('https://www.firstpost.com/firstcricket/cricket-live-score').text 
    soup = BeautifulSoup(html_text, "html.parser") 
    live_matches = soup.find_all('li', class_='glide__slide')
    
    html = ""
    for match in live_matches:
        try:
            match_name = match.find('h5', class_='match-name').text.strip()
            team_one = match.find('div', class_='team-one')
            team_two = match.find('div', class_='team-two')

            team_one_name = team_one.find('span', class_='country-name').text.strip()
            team_one_score = team_one.find('span', class_='team-score').text.strip()

            team_two_name = team_two.find('span', class_='country-name').text.strip()
            team_two_score = team_two.find('span', class_='team-score').text.strip()

            match_status = match.find('div', class_='match-res-txt').text.strip()

            html+=f"<center><h1 style='color: blue'>Match: {match_name}</h1>"
            html+=f"<h3>{team_one_name}: {team_one_score}</h3>"
            html+=f"<h3>{team_two_name}: {team_two_score}</h3>"
            html+=f"<h2 style='color: red'>Status: {match_status}</h2>"
            html+="<br><hr><br></center>"
        except:
            html+=""

    return html

if __name__ == '__main__': 
    app.run(debug=True) 