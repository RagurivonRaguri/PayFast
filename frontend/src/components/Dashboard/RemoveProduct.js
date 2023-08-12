import React from 'react';

function RemoveProduct({ products }) {
  const handleDelete = (productId) => {
    const token = sessionStorage.getItem("access_token");
    fetch(`/product/${productId}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(`Successfully deleted: ${data.msg}`);
      })
      .catch((error) => {
        console.error('Error deleting product:', error);
      });
  };

  return (
    <div className="bg-gray-100 h-screen py-10">
      <div className="max-w-xl mx-auto p-6 bg-white shadow rounded-lg">
        <h2 className="text-2xl font-bold mb-4">Remove Product</h2>
        {products.length === 0 ? (
          <p>No products to remove.</p>
        ) : (
          products.map((product) => {
            return (
              <div key={product.id} className="border-b py-4 flex justify-between items-center">
                <span>{product.name}</span>
                <button
                  className="text-red-500"
                  onClick={() => {
                    console.log(product.id);
                    handleDelete(product.id)}}
                >
                  Remove
                </button>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}

export default RemoveProduct;
