const backendUrl = 'http://localhost:5000';
let form;

document.addEventListener('DOMContentLoaded', () => {
    form = document.getElementById('restaurant-preferences');

    if (form) {
        form.addEventListener("submit", handleSubmit);
    }
})

//  gets the form data and sends it to the backend
const handleSubmit = async (e) => {
    e.preventDefault();

    const selectedRestaurants = document.querySelectorAll('input[name="restaurant[]"]:checked');
    const selectedPrice = document.querySelector('input[name="price"]:checked');
    const selectedCuisine = document.querySelectorAll('input[name="cuisine[]"]:checked');

    const restaurantValues = Array.from(selectedRestaurants).map(checkbox => checkbox.value);
    const priceValue = selectedPrice ?  selectedPrice.value : null;
    const cuisineValues = Array.from(selectedCuisine).map(checkbox => checkbox.value);

    if (cuisineValues.length === 0) {
        const errorMsg = document.querySelector('#cuisine-error');
        errorMsg.style.display = 'block';
        return;
    }

    const data = {
        restaurants: restaurantValues,
        price: priceValue,
        cuisines: cuisineValues
    }
    
    console.log(restaurantValues);
    console.log(priceValue);
    console.log(cuisineValues);

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

