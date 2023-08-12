import React, { useState } from 'react';

function Sales({ products }) {
  const [cart, setCart] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  const handleAddToCart = (product) => {
    setCart((prevCart) => [...prevCart, product]);
  };
  const handleCheckout = () => {
    const token = sessionStorage.getItem("access_token");
  
    const checkoutData = {
      date_of_purchase: Math.floor(new Date().getTime() / 1000), // Convert to Unix timestamp
      total_amount: getTotalAmount(),
      product_ids: cart.map((item) => item.id),
    };
    
    console.log(checkoutData);
  
    fetch('/post_sales', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(checkoutData),
    })
      .then((response) => {
        if (response.ok) {
          console.log('Checkout successful');
          setCart([]); // Clear the cart after successful checkout
        } else {
          console.error('Checkout failed');
        }
      })
      .catch((error) => {
        console.error('An error occurred', error);
      });
  };
  

  const handleRemoveFromCart = (productName) => {
    setCart((prevCart) => prevCart.filter((item) => item.name !== productName));
  };
  
  const getTotalAmount = () => {
    const totalAmount = cart.reduce((sum, item) => sum + item.cost, 0);
    return totalAmount;
  };

  const filteredProducts = products.filter((product) =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleClearCart = () => {
    setCart([]);
  };

  return (
    <>
      <div className="flex justify-between">
        <div className="w-3/4 mx-auto">
          <div className="flex items-center justify-between mb-4">
            <input
              type="text"
              placeholder="Search products..."
              className="px-4 py-2 border rounded-lg w-1/3"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <div className="flex space-x-2">
              <button className="bg-blue-500 text-white px-4 py-2 rounded-lg" onClick={handleCheckout}>Checkout</button>
              <button className="bg-red-500 text-white px-4 py-2 rounded-lg" onClick={handleClearCart}>Clear Cart</button>
            </div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {filteredProducts.map((product) => (
              <div key={product.id} className="rounded-lg shadow-md p-4">
                <h2 className="text-xl font-bold">{product.name}</h2>
                <p className="text-gray-600">{product.description}</p>
                <p className="text-green-500 font-bold mt-2">Ksh{product.cost}</p>
                <p className="text-green-500 font-bold mt-2">In Stock:{product.quantity}</p>
                <button
                  onClick={() => handleAddToCart(product)}
                  className="bg-blue-500 text-white px-4 py-2 rounded-lg mt-4"
                >
                  Add to Cart
                </button>
              </div>
            ))}
          </div>
        </div>
        <div className="w-1/4">
          <div className="bg-gray-200 rounded-lg p-4">
            <h2 className="text-2xl font-bold mb-4">Cart</h2>
            {cart.map((item) => (
              <div key={item.id} className="flex justify-between items-center mb-2">
                <span>{item.name}</span>
                <button
                  onClick={(e) => {
                    e.preventDefault(); // Prevent the default button behavior
                    handleRemoveFromCart(item.name);
                  }}
                  className="bg-red-500 text-white px-2 py-1 rounded-lg"
                >
                  Remove
                </button>
              </div>
            ))}
            {cart.length === 0 && <p>Your cart is empty.</p>}
            {cart.length > 0 && (
              <div className="mt-4">
                <hr />
                <p className="font-bold">Total Amount: Ksh{getTotalAmount()}</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
  
}
export default Sales;
