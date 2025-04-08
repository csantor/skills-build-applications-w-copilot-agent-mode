import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://orange-space-parakeet-755pg74g4gw24r6-8000.app.github.dev/api/leaderboard')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Activities</h1>
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.id}>
              <td>{activity.id}</td>
              <td>{activity.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Activities;
