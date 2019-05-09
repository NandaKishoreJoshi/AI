## Generated Story -5711297067970279752
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - cuisine_check
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "High"}
    - slot{"price_range": "High"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_emailrestaurants
* deny
    - utter_ask_searchmore
* affirm
    - utter_goodbye
    - export

