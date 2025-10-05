let recommendedRestaurants = []; // list of restaurant objects
const backendUrl = 'http://localhost:5500';

const setRecommendedRestaurants = async () => {
    try {
        const res = await fetch(`${backendUrl}/api/recommendation`)

        const result = await res.json();

        recommendedRestaurants = result.data;
        console.log(recommendedRestaurants);
        
    } catch (error) {
        console.error(error)
    }
}

document.addEventListener('DOMContentLoaded', () => setRecommendedRestaurants());