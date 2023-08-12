import React, { useState, useEffect } from 'react';

function ProfileCard({ profile }) {
  return (
    <div className="bg-white shadow-md rounded-md p-6 w-72 mx-auto">
      <div className="text-2xl font-bold text-center">Profile</div>
      <div className="mt-4">
        <div className="text-gray-600">First Name:</div>
        <div className="font-bold">{profile.firstname}</div>
        <div className="text-gray-600">Last Name:</div>
        <div className="font-bold">{profile.lastname}</div>
        <div className="text-gray-600">Location:</div>
        <div className="font-bold">{profile.location}</div>
      </div>
    </div>
  );
}

function Profile() {
  const [profiles, setProfiles] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = sessionStorage.getItem("access_token");
    if (token) {
      setIsAuthenticated(true);
      fetchProfiles(token);
    } else {
      console.error("No access token found");
    }
  }, []);

  const fetchProfiles = (token) => {
    fetch('/profile', {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then(response => {
      return response.json();
    })
    .then(data => setProfiles(data))
    .catch(error => console.error("Error fetching profiles:", error));
  };

  return (
    <div>
      <div className="bg-white shadow-md rounded-md p-6 w-72 mx-auto">
        <img
          src="https://i.pinimg.com/736x/a8/57/00/a85700f3c614f6313750b9d8196c08f5.jpg"
          alt="Profile"
          className="w-32 h-32 rounded-full mx-auto mb-4"
        />
        {isAuthenticated ? (
          profiles.map((profile) => {
            return(
            <ProfileCard key={profile.id} profile={profile} />
          )})
        ) : (
          <div className="text-center text-red-500 font-bold">
            Please Sign In to view your profile.
          </div>
        )}
      </div>
    </div>
  );
}
export default Profile;
