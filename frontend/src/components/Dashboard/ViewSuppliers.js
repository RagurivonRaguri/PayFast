import React, { useState, useEffect } from 'react';

function ViewSuppliers() {
  const [suppliers, setSuppliers] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = sessionStorage.getItem("access_token");
    if (token) {
      setIsAuthenticated(true);
      fetch('/suppliers', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then((response) => response.json())
        .then((data) => setSuppliers(data))
        .catch((error) => {
          console.error('Error fetching suppliers:', error);
        });
    }
  }, []);

  const handleDelete = (supplierId) => {
    const token = sessionStorage.getItem("access_token");
    if (token) {
      fetch(`/supplier/${supplierId}`, {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token}`,
          "Accept": "application/json",
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(`Successfully deleted ${data.name}`);
          // After deletion, you can update the suppliers list here if needed
        })
        .catch((error) => {
          console.error('Error deleting supplier:', error);
        });
    } else {
      console.error("No access token found");
    }
  };

  return (
    <> 
    <div className="bg-gray-100 h-screen py-10">
      <div className="max-w-xl mx-auto p-6 bg-white shadow rounded-lg">
        <div>
        {isAuthenticated ? null : (
          <div className="text-red-500 font-bold">You are not authorized to view suppliers.</div>
        )}
      </div>
      {isAuthenticated && suppliers.map((supplier) => (
        <div key={supplier.id} className="border-b py-4 flex justify-between items-center">
          <span>{supplier.name}</span>
          <button
            className="text-red-500"
            onClick={() => handleDelete(supplier.id)}
          >
            Remove
          </button>
        </div>
      ))}
      </div>
        </div>
    </>
  );
}

export default ViewSuppliers;
