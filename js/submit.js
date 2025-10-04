const backendUrl = 'http://localhost:2500';

//  gets the form data and sends it to the backend
const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
         const response = await fetch(`${backendUrl}/api/preference`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        if (!response.ok) {
            throw new Error(`HTTP error — status: ${response.status}`)
        }

        const result = await response.json();
        console.log('API Response:', result);
       
    } catch (error) {
        console.error('Error sending data to API:', error)
    }
}


document.querySelector('form').addEventListener("submit", () => {
    sendCustomerData();
});