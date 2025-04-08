import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    fetch('https://orange-space-parakeet-755pg74g4gw24r6-8000.app.github.dev/api/leaderboard')
      .then(response => response.json())
      .then(data => setLeaders(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Leaderboard</h1>
      <table className="table table-bordered">
        <thead className="thead-dark">
          <tr>
            <th>Rank</th>
            <th>Name</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {leaders.map((leader, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{leader.name}</td>
              <td>{leader.points}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Leaderboard;
