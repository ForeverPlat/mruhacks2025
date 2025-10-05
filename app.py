from flask import Flask, request, jsonify, render_template, g
from recommendation import get_recommendations, get_recommendation_from_name

app = Flask(__name__, template_folder='templates')

# commenting this out for now, going to hard code for testing
# restaurants = []
# cuisine = []
# price = ""

@app.route("/")
def home():
    # make sure your template file name matches exactly
    # return render_template("/userPreference.html")
    return render_template('userPreference.html')

@app.route("/api/preference", methods=["POST"])
def form_data():
    # Parse JSON from body
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No JSON body provided or invalid JSON."}), 400

    required = {"cuisines", "price", "restaurants"}
    missing = required - data.keys()
    if missing:
        return jsonify({"error": "Missing required fields.", "missing": sorted(missing)}), 400

    restaurants = data["restaurants"]  # e.g., list or string—your choice
    cuisine = data["cuisines"]
    price = data["price"]

    print(restaurants)
    print(price)

    with open("res/preference.txt", "w") as f:
        if (len(restaurants) == 0):
            f.write("\n")

        for i in range(len(restaurants)):
            if (i == len(restaurants) - 1):
                print("i")  
                print(i)
                f.write(restaurants[i]+"\n")
                print("i")  
                print(restaurants[i])
            else:
                f.write(restaurants[i]+ ",")
                print(i)
                print(restaurants[i])

        f.write(price + "\n")

        for i in range(len(cuisine)):
            if (i == len(cuisine) - 1):
                print("c")  
                print(i)
                f.write(cuisine[i]+"\n")
                print(cuisine[i])
            else:
                f.write(cuisine[i]+ ",")
                print("c")  
                print(i)
                print(cuisine[i])
        

    # Do something with the data
    # print("restaurants:", restaurants)
    # print("cuisines:", cuisine)
    # print("price:", price)

    return jsonify({
        "ok": True,
        "received": {"cuisine": cuisine, "price": price, "restaurants": restaurants}
    }), 200
    









@app.route("/recommendation")
def show_recommendations():
    return render_template('recommendation.html')

@app.route("/api/recommendation", methods=["GET"])
def get_recommendations_route():

    restaurants = []
    price = ""
    cuisines = []

    with open("res/preference.txt", "r") as preferenceFile:
        for index, line in enumerate(preferenceFile):
            if index == 0:
                restaurants = line.strip().split(',')
            elif index == 1:
                price = line.strip()
            elif index == 2:
                cuisines = line.strip().split(',')

    
    if (len(cuisines) == 0 and price != "" and restaurants[0] == ''):
        return jsonify("error: Missing preferences."), 400
    
    # if no restaurants is selected
    if (restaurants[0] == ''):
        for c in cuisines:
            print(c)
        recommendations = get_recommendations(price, cuisines)

        return jsonify({
            "ok": True,
            "data": recommendations
        })
        # get recommendation
        # return the data
    
    # this is when a restaurant is selected
    if (restaurants[0] != ''):
        recommendations = []
        for restaurant in restaurants:
            recommendation = get_recommendation_from_name(restaurant)
            recommendations.append(recommendation)
            
        print(recommendations)    
        return jsonify({
            "ok": True,
            "data": recommendations
        })
        # get_recommendations
        # return the data

if __name__ == "__main__":
    app.run(port=5500, debug=True)

    