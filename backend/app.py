from flask import Flask, request, jsonify
from services.api_football import get_today_matches, get_team_statistics, get_head_to_head

app = Flask(__name__)

@app.route('/matches', methods=['GET'])
def matches():
    timezone = request.args.get('timezone', 'Europe/Athens')
    try:
        data = get_today_matches(timezone)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/team-stats', methods=['GET'])
def team_stats():
    team_id = request.args.get('team_id')
    league_id = request.args.get('league_id')
    season = request.args.get('season')
    if not team_id or not league_id or not season:
        return jsonify({'error': 'Missing required parameters'}), 400
    try:
        data = get_team_statistics(team_id, league_id, season)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/head-to-head', methods=['GET'])
def head_to_head():
    team1_id = request.args.get('team1_id')
    team2_id = request.args.get('team2_id')
    if not team1_id or not team2_id:
        return jsonify({'error': 'Missing required parameters'}), 400
    try:
        data = get_head_to_head(team1_id, team2_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
