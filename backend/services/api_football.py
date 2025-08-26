import requests
from datetime import datetime

API_KEY = "2eff385f8af9f39456ad0ac55ceaea05"

# Base URL for API-Football
BASE_URL = "https://v3.football.api-sports.io"

# Common headers for all requests
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

def get_today_matches(timezone="Europe/Athens"):
    """Fetch today's football matches."""
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"{BASE_URL}/fixtures"
    params = {
        "date": today,
        "timezone": timezone
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching today's matches: {e}")
        return None

def get_team_statistics(team_id, league_id, season):
    """Fetch statistics for a specific team in a league and season."""
    url = f"{BASE_URL}/teams/statistics"
    params = {
        "team": team_id,
        "league": league_id,
        "season": season
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching team statistics: {e}")
        return None

def get_head_to_head(team1_id, team2_id):
    """Fetch head-to-head data between two teams."""
    url = f"{BASE_URL}/fixtures/headtohead"
    params = {
        "h2h": f"{team1_id}-{team2_id}"
    }
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching head-to-head data: {e}")
        return None

