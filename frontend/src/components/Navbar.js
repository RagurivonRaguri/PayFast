import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';

function Navbar() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  const handleLogout = () => {
    console.log(sessionStorage.getItem('access_token'));
    fetch('/logout', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        if (response.ok) {
          sessionStorage.removeItem('access_token'); // Corrected key here
          console.log('Logout successful');
        } else {
          console.error('Logout failed');
        }
      })
      .catch(error => {
        console.error('Logout error:', error);
      });
  };
  
  return (
    <div className="navbar" style={{ position: 'fixed', top: 0, right: 0, margin: '20px' }}>
      <div className="dropdown relative inline-block">
        <button className="dropbtn text-black px-4 py-2 bg-transparent border-none" onClick={toggleDropdown}>
          Menu
        </button>
        {isDropdownOpen && (
          <div
            className="dropdown-content absolute right-0 mt-2 py-2 bg-lightblue rounded-lg shadow-lg"
            style={{ minWidth: '120px', zIndex: '1', backgroundColor: 'white' }}
          >
            <NavLink to="/profile" className="block px-4 py-2 text-blue-600 hover:bg-blue-100" activeStyle={{ color: 'brown' }}>
              Profile
            </NavLink>
            <NavLink to="/sales" className="block px-4 py-2 text-blue-600 hover:bg-blue-100" activeStyle={{ color: 'brown' }}>
              Sales
            </NavLink>
            <NavLink to="/dashboard" className="block px-4 py-2 text-blue-600 hover:bg-blue-100" activeStyle={{ color: 'brown' }}>
              Dashboard
            </NavLink>
            <NavLink exact to="/" className="block px-4 py-2 text-blue-600 hover:bg-blue-100" activeStyle={{ color: 'brown' }}>
              Get Started
            </NavLink>
            <NavLink
                to="/login"
                className="block px-4 py-2 text-blue-600 hover:bg-blue-100"
                activeStyle={{ color: 'brown' }}
                onClick={handleLogout}
              >
                Logout
              </NavLink>
          </div>
        )}
      </div>
    </div>
  );
}

export default Navbar;
