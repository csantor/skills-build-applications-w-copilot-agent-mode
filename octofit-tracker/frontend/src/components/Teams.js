import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://orange-space-parakeet-755pg74g4gw24r6-8000.app.github.dev/api/teams')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div>
      <h1>Teams</h1>
      <ul>
        {teams.map(team => (
          <li key={team.id}>{team.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
