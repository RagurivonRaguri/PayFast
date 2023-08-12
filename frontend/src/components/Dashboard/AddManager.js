import React, {useState} from 'react'

function AddManager() {
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const formData = (
        username,
        email,
        password
    )

    function handleManager(){
        const token = sessionStorage.getItem("access_token")
        fetch('/post_manager',{
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setUsername("")
            setEmail("")
            setPassword("")
        })
        .catch(error => {
            console.error('Error adding manager:', error);
        });
};

return (
    <div className="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md space-y-4">
        <h2 className="text-2xl font-semibold">Add Manager</h2>
        <div className="space-y-2">
            <label className="block text-sm font-medium text-gray-700">Username:</label>
            <input
                className="border rounded-md w-full py-2 px-3 focus:outline-none focus:ring focus:border-blue-300"
                type="text"
                value={username}
                onChange={e => setUsername(e.target.value)}
            />
        </div>
        <div className="space-y-2">
            <label className="block text-sm font-medium text-gray-700">Email:</label>
            <input
                className="border rounded-md w-full py-2 px-3 focus:outline-none focus:ring focus:border-blue-300"
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)}
            />
        </div>
        <div className="space-y-2">
            <label className="block text-sm font-medium text-gray-700">Password:</label>
            <input
                className="border rounded-md w-full py-2 px-3 focus:outline-none focus:ring focus:border-blue-300"
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)}
            />
        </div>
        <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded focus:outline-none focus:ring focus:border-blue-300"
            onClick={handleManager}
        >
            Add Manager
        </button>
    </div>
);
}

export default AddManager;