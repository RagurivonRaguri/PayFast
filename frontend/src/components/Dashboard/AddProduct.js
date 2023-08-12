import React, { useState } from 'react';

function AddProduct() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [cost, setCost] = useState('');
  const [quantity, setQuantity] = useState('');
  const [category_id, setCategory_id] = useState('');
  const [suppliers_id, setSuppliers_id] = useState('');

  let formData = {
    name: name,
    description: description,
    cost: cost,
    quantity: quantity,
    category_id: category_id,
    suppliers_id: suppliers_id
  };

  
  const handleSubmit = (event) => {
    event.preventDefault();
    const token = sessionStorage.getItem("access_token");
  
    fetch('/add_product', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('New product added:', data);
        // Reset each input field to an empty string
        setName('');
        setDescription('');
        setCost('');
        setQuantity('');
        setCategory_id('');
        setSuppliers_id('');
      })
  };
  

 return (
    <div className="container mx-auto px-4 h-full">
      <div className="flex content-center items-center justify-center h-full">
        <div className="w-full lg:w-4/12 px-4">
          <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
            <div className="rounded-t mb-0 px-6 py-6 bg-white">
              <form onSubmit={handleSubmit}>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Name</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                    value={formData.name}
                    onChange={(e)=>setName(e.target.value)}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Description</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                    value={formData.description}
                    onChange={(e)=>setDescription(e.target.value)}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Cost</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    value={formData.cost}
                    onChange={(e) => setCost(parseFloat(e.target.value))}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Quantity</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    value={formData.quantity}
                    onChange={(e) => setQuantity(parseInt(e.target.value))}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Category Number</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    value={formData.category_id}
                    onChange={(e) => setCategory_id(parseInt(e.target.value))}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Supplier Number</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    value={formData.suppliers_id}
                    onChange={(e) => setSuppliers_id(parseInt(e.target.value))}
                  />
                </div>
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                  Add Product
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AddProduct;
