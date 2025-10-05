from flask import Flask, request, jsonify, render_template
from recommendation import get_recommendations, get_recommendation_from_name

app = Flask(__name__, template_folder='templates')

cuisine = []
price = ""
restaurants = []

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

    cuisine = data["cuisines"]
    price = data["price"]
    restaurants = data["restaurants"]  # e.g., list or string—your choice

    # Do something with the data
    print("restaurants:", restaurants)
    print("cuisines:", cuisine)
    print("price:", price)

    return jsonify({
        "ok": True,
        "received": {"cuisine": cuisine, "price": price, "restaurants": restaurants}
    }), 200
    
@app.route("/api/recommendation", methods=["GET"])
def get_recommendations():
    data = request.get_json(silent=True)
    
    if not data:
        return jsonify({"error": "No JSON body provided or invalid JSON."}), 400
    
    if (len(cuisine) == 0 and price != "" and len(restaurants) == 0):
        return jsonify("error: Missing preferences."), 400
    
    if (len(restaurants) == 0):
        recommendations = get_recommendations()
        return jsonify({
            "ok": True,
            "data": recommendations
        })
        # get recommendation
        # return the data
        
    if (len(restaurants) != 0):
        recommendations = get_recommendation_from_name()
        return jsonify({
            "ok": True,
            "data": recommendations
        })
        # get_recommendations
        # return the data
    

if __name__ == "__main__":
    app.run(debug=True)

    