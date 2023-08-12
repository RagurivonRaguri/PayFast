import React, {useState} from 'react';
import { useHistory } from 'react-router-dom';

function Signup() {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();
  const handleSignup = async () => {
    let formData = {
      email: email,
      username: username,
      password: password,
    };
    try {
      const response = await fetch('/register', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
    
      if (response.ok) {
        const data = await response.json();
  
        // Store the access token and metadata in session storage
        sessionStorage.setItem("access_token", data.access_token);
        sessionStorage.setItem("metadata", JSON.stringify(data.metadata));
        console.log("Signup successful");
        history.push('/sales');
      } else {
        console.error("Signup failed");
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };
  
  return (
    <div className="flex justify-center items-center h-screen">
      <div className="w-full max-w-md p-6 bg-gray-100 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Sign Up</h2>
        <form onSubmit={handleSignup}>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-600">Email</label>
            <input
              type="email"
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
              value={email}
              onChange={(e)=>setEmail(e.target.value)}
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-600">Username</label>
            <input
              type="text"
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
              value={username}
              onChange={(e)=>setUsername(e.target.value)}
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-600">Password</label>
            <input
              type="password"
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
              value={password}
              onChange={(e)=>setPassword(e.target.value)}
            />
          </div>
          <button
            className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300"
            type="submit"
          >
            Sign Up
          </button>
        </form>
      </div>
    </div>
  );
}

export default Signup;
