import React from 'react';

function LandingPage() {
  const backgroundImageUrl =
    'https://plus.unsplash.com/premium_photo-1668613403592-fd6c8ec1aafa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cmV0YWlsfGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60';

  const containerStyle = {
    backgroundImage: `url(${backgroundImageUrl})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  };
  return (
    <div
      className="min-h-screen bg-gradient-to-br from-blue-500 to-indigo-600 py-12 px-4 sm:px-6 lg:px-8"
      style={containerStyle}
    >
      <div className="max-w-3xl mx-auto">
        <h1 className="text-6xl font-bold text-white mb-8">Welcome to PayFast</h1>
        <p className="text-2xl text-white mb-8">A modern point of sale solution for your business.</p>
        <div className="flex justify-center">
          <a
            href="/login" 
            className="bg-white text-indigo-600 hover:bg-indigo-600 hover:text-white rounded-full px-8 py-3 text-lg font-semibold shadow-md transition duration-300"
          >
            Get Started
          </a>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
