let recommendedRestaurants = []; // list of restaurant objects
const backendUrl = 'http://localhost:5500';

const setRecommendedRestaurants = async () => {
    try {
        const res = await fetch(`${backendUrl}/api/recommendation`)

        const result = await res.json();

        recommendedRestaurants = result.data;
        // console.log(recommendedRestaurants);

        
        
    } catch (error) {
        console.error(error)
    }

    const main = document.getElementById("rec-main");
    console.log(main);
    console.log(recommendedRestaurants);

    
    
    // main.innerHTML
    recommendedRestaurants.forEach((restaurant) => {
        console.log(restaurant);
        
        main.innerHTML += `
        <div class="restaurant-card">
            <div class="restaurant-image">Placeholder Image</div>
            <div class="restaurant-info">
                <h2 class="restaurant-name">${restaurant[0]}</h2>
                <p class="restaurant-details rating">${restaurant[1]} ★</p>
                <p class="restaurant-details">Price: ${restaurant[2]}</p>
                <p class="restaurant-details">Cuisine: ${restaurant[3]}</p>
            </div>
        </div>`
    })
}

document.addEventListener('DOMContentLoaded', () => {
    setRecommendedRestaurants();

    

});



