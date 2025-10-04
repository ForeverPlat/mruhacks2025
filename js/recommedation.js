let recommendedRestaurants = []; // list of restaurant objects

const setRecommendedRestaurants = async () => {
    try {
        const res = await fetch(`${backendUrl}/api/restaurants/recommendation`)

        const result = await res.json();

        recommendedRestaurants = result.data;

    } catch (error) {
        console.error(error)
    }
}

window.onload = () => {
    const currentPath = window.location.pathname;

    if (currentPath !== '/recommendation.html')
        return;

    setRecommendedRestaurants();
}