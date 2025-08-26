home_page_code = """
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './HomePage.css';

const HomePage = () => {
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMatches = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/matches');
        setMatches(response.data.response || []);
      } catch (err) {
        setError('Failed to fetch matches');
      } finally {
        setLoading(false);
      }
    };

    fetchMatches();
  }, []);

  return (
    <div className="homepage">
      <h1>Today's Football Matches</h1>
      {loading && <p>Loading matches...</p>}
      {error && <p className="error">{error}</p>}
      {!loading && !error && matches.length === 0 && <p>No matches found.</p>}
      <ul className="match-list">
        {matches.map((match) => (
          <li key={match.fixture.id} className="match-item">
            <span>{match.teams.home.name}</span> vs <span>{match.teams.away.name}</span>
            <div className="match-time">{new Date(match.fixture.date).toLocaleString()}</div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
"""

