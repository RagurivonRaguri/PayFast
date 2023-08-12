import React, { useState, useEffect } from 'react';

function PatchProduct({ products }) {
  const [selectedProductId, setSelectedProductId] = useState('');
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [cost, setCost] = useState('');
  const [quantity, setQuantity] = useState('');
  

  useEffect(() => {
    if (selectedProductId !== '') {
      const selectedProduct = products.find((product) => product.id === parseInt(selectedProductId));
      if (selectedProduct) {
        setName(selectedProduct.name || '');
        setDescription(selectedProduct.description || '');
        setCost(selectedProduct.cost || '');
        setQuantity(selectedProduct.quantity || '');
      }
    }
  }, [selectedProductId, products]);
  const handlePatch = (e) => {
    e.preventDefault();
    const token = sessionStorage.getItem('access_token');
    fetch(`/product/${selectedProductId}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        name,
        description,
        cost,
        quantity
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Product updated:', data);
      });
  };

  const handleProductSelect = (e) => {
    const productId = e.target.value;
    setSelectedProductId(productId);
  };
  return (
    <div className="container mx-auto px-4 h-full">
      <div className="flex content-center items-center justify-center h-full">
        <div className="w-full lg:w-4/12 px-4">
          <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
            <div className="rounded-t mb-0 px-6 py-6 bg-white">
              <form onSubmit={handlePatch}>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Select Product</label>
                  <select
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    value={selectedProductId}
                    onChange={handleProductSelect}
                  >
                    <option value="">Select a product</option>
                    {products.map((product) => (
                      <option key={product.id} value={product.id}>
                        {product.name}
                      </option>
                    ))}
                  </select>
                  <label className="block text-gray-700 text-sm font-bold mb-2">Name</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Description</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="text"
                    value={description}
                    onChange={(e)=>setDescription(e.target.value)}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Cost</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    value={cost}
                    onChange={(e) => setCost(parseFloat(e.target.value))}
                  />
                </div>
                <div className="mb-4">
                  <label className="block text-gray-700 text-sm font-bold mb-2">Quantity</label>
                  <input
                    className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="number"
                    value={quantity}
                    onChange={(e) => setQuantity(parseInt(e.target.value))}
                  />
                </div>
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                  Patch Product
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PatchProduct