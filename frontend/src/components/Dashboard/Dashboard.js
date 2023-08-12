import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
  const [salesTotal, setSalesTotal] = useState([]);

  useEffect(() => {
    const token = sessionStorage.getItem("access_token");
    fetch('/sales',{
      method: 'GET',
      headers: {
        "content-type": "application/json",
        Authorization: `Bearer ${token}`
      }
    })
      .then(response => response.json())
      .then(data => setSalesTotal(data.length))
      .catch(error => console.error('Error fetching sales:', error));
    
  }, []);

  return (
    <div className="bg-gray-100 min-h-screen py-10">
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-8 text-center text-gray-800">
          Welcome to the Dashboard
        </h1>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          <Link
            to="/add-product"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            Add a Product
          </Link>
          <Link
            to="/patch-product"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            Patch a Product
          </Link>
          <Link
            to="/remove-product"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            Remove a Product
          </Link>
          <Link
            to="/add-manager"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            Add a Manager
          </Link>
          <Link
            to="/add-cashier"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            Add a Cashier
          </Link>
          <Link
            to="/sales-history"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            View Sales History
          </Link>
          <Link
            to="/view-suppliers"
            className="btn border rounded-lg text-center text-black bg-slate-200 hover:text-blue-600"
          >
            View Suppliers
          </Link>
        </div>
        <div className="mt-8 grid grid-cols-2 gap-4">
          <div className="bg-blue-500 text-white rounded-lg p-4 text-center">
            <h2 className="text-2xl font-bold">Total Sales</h2>
            <p className="text-3xl">{salesTotal}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
