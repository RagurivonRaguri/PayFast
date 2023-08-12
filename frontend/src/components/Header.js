import React from 'react';
import Navbar from './Navbar';

function Header() {
  return (
    <div className="bg-gradient-to-r from-purple-500 via-pink-500 to-red-500">
      <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center">
          <div className="flex items-center">
            <h1 className="text-3xl font-extrabold text-white">PayFast</h1>
          </div>
          <Navbar />
        </div>
      </div>
    </div>
  );
}

export default Header;



