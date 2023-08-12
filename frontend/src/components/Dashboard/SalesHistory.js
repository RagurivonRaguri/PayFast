import React, { useState, useEffect } from 'react';

function SalesHistory() {
  const [sales, setSales] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = sessionStorage.getItem("access_token");
    if (token) {
      setIsAuthenticated(true);
      fetch('/sales', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then((response) => response.json())
        .then((data) => setSales(data))
        .catch((error) => {
          console.error('An error occurred:', error);
        });
    }
  }, []);

  return (
    <div className="bg-gray-100 h-screen py-10">
      <div className="max-w-xl mx-auto p-6 bg-white shadow rounded-lg">
        <h1 className="text-2xl font-bold mb-4">Sales History</h1>
        <div>
          {isAuthenticated ? null : (
            <div className="text-red-500 font-bold">You are not authorized to view sales history.</div>
          )}
        </div>
        {isAuthenticated && (
          <ul className="divide-y divide-gray-300">
            {sales.map((sale, index) => (
              <li key={index} className="py-4">
                <p className="text-gray-600">
                  <span className="font-semibold">Date:</span> {sale.date_of_purchase}
                </p>
                <p className="text-gray-600">
                  <span className="font-semibold">Amount:</span> {sale.total_amount}
                </p>
                <p className="text-gray-600">
                  <span className="font-semibold">Cashier ID:</span> {sale.user_id}
                </p>
                <p className="text-gray-600">
                  <span className="font-semibold">Product ID:</span> {sale.product_id}
                </p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default SalesHistory;
