import requests
import json


def finestFoodOutlet(city, votes):
    base_url = "https://jsonmock.hackerrank.com/api/food_outlets"
    page = 1
    best_outlet = None
    best_rating = 0.0
    best_votes = 0
    total_pages = 1  # Initial value

    while page <= total_pages:
        url = f"{base_url}?city={city}&page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            break
        data = json.loads(response.text)
        total_pages = data["total_pages"]

        for outlet in data["data"]:
            rating = outlet["user_rating"]["average_rating"]
            outlet_votes = outlet["user_rating"]["votes"]
            if outlet_votes >= votes:
                if (rating > best_rating) or (
                    rating == best_rating and outlet_votes > best_votes
                ):
                    best_rating = rating
                    best_votes = outlet_votes
                    best_outlet = outlet["name"]

        page += 1

    if best_outlet is None:
        return "-1"
    return best_outlet
