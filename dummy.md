## Generated Story 6470950673937594110
* greet
    - utter_greet
* restaurant_search
* restaurant_search
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
* restaurant_search{"cuisine": "South Indian", "location": "chennai"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "chennai"}
    - export

## Generated Story -8655842393787724191
* email_send
    - export

## Generated Story 976368319611179428
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search
    - cuisine_check
    - export

## Generated Story -8731010974147160976
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"location": "delhi"}
    - cuisine_check
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_emailrestaurants
* affirm
    - utter_ask_emailaddress
* email_send
    - validate_email
    - export

## Generated Story 3832910781881539164
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - cuisine_check
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"cuisine": "low"}
    - slot{"cuisine": "low"}
    - export

## Generated Story -9009329725795390073
* greet
    - utter_greet
* restaurant_search{"price_range": "High"}
    - slot{"price_range": "High"}
* restaurant_search{"cuisine": "north indian", "location": "Pune"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Pune"}
    - action_location
    - slot{"location": "pune"}
    - cuisine_check
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "High"}
    - slot{"price_range": "High"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_emailrestaurants
* affirm
    - utter_ask_emailaddress
* email_send{"location": "12334"}
    - slot{"location": "12334"}
    - validate_email
    - slot{"customer_email": null}
* email_send{"customer_email": "nandakishorej8@gmail.com"}
    - slot{"customer_email": "nandakishorej8@gmail.com"}
    - export

## Generated Story 4637938852835856891
* greet
    - utter_ask_location
    - export

## Generated Story -5712681744049025091
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - cuisine_check
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price_range": "High"}
    - slot{"price_range": "High"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_ask_emailrestaurants
* affirm
    - utter_ask_emailaddress
* email_send{"customer_email": "nandakishorej8@gmail.com"}
    - slot{"customer_email": "nandakishorej8@gmail.com"}
    - validate_email
    - slot{"customer_email": "nandakishorej8@gmail.com"}
    - action_email
    - slot{"location": "chennai"}
    - utter_ask_searchmore
* deny
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "delhi"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"location": "delhi"}
    - cuisine_check
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "Medium"}
    - slot{"price_range": "Medium"}
    - action_restaurant
    - slot{"location": null}
    - utter_again
* affirm
    - utter_ask_location
* restaurant_search
    - action_location
    - export

## Generated Story 1868683377681331648
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "chennai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "chennai"}
    - action_location
    - slot{"location": "chennai"}
    - cuisine_check
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "low"}
    - slot{"price_range": "low"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_ask_emailrestaurants
* deny
    - utter_ask_searchmore
* affirm
    - utter_ask_location
* restaurant_search
    - export

## Generated Story -4109915511791888866
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - cuisine_check
    - slot{"cuisine": null}
    - utter_cuisine_again
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
* affirm
    - utter_ask_emailaddress
* email_send
    - validate_email
    - slot{"customer_email": null}
* email_send{"customer_email": "nandakishorej8@gmail.com"}
    - slot{"customer_email": "nandakishorej8@gmail.com"}
    - validate_email
    - slot{"customer_email": "nandakishorej8@gmail.com"}
    - action_email
    - slot{"location": "delhi"}
    - utter_ask_searchmore
* affirm
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_location
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - cuisine_check
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price_range": "below 2000"}
    - slot{"price_range": "below 2000"}
    - action_restaurant
    - slot{"location": null}
    - utter_again
* affirm
    - utter_ask_location
* restaurant_search
    - action_location
    - slot{"location": null}
    - utter_location_again
* affirm
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - cuisine_check
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price_range": "Low"}
    - slot{"price_range": "Low"}
    - action_restaurant
    - slot{"location": null}
    - utter_again
* deny
    - utter_goodbye
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - cuisine_check
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"cuisine": "high"}
    - slot{"cuisine": "high"}
    - action_restaurant
    - slot{"location": null}
    - utter_again
* deny
    - utter_goodbye
    - export

## Generated Story 3640965116433947470
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_location
    - slot{"location": null}
    - utter_location_again
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - cuisine_check
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "high"}
    - slot{"price_range": "high"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_emailrestaurants
* deny
    - utter_ask_searchmore
* affirm
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_location
    - slot{"location": "bengaluru"}
    - utter_ask_cuisine
* restaurant_search
    - cuisine_check
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price_range": "Medium"}
    - slot{"price_range": "Medium"}
    - action_restaurant
    - slot{"location": null}
    - slot{"price_range": null}
    - slot{"cuisine": null}
    - slot{"customer_email": null}
    - utter_again
* deny
    - utter_goodbye
    - export

