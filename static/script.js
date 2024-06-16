function fetchData() {
    fetch('/get', {
        method: 'POST',
        body: JSON.stringify({ msg: 'Hello from JavaScript' }), // Convert object to JSON string
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Log the response data
        document.getElementById('response').innerText = data.response; // Update a DOM element with the response
    })
    .catch(error => console.error('Error:', error));
}
