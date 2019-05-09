import requests
import ast
import json

base_url = "https://developers.zomato.com/api/v2.1/"


def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key = config["user_key"]
	
    def get_location(self, query="", limit=5):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "locations?query=" + str(query) + "&count=" + str(limit), headers=headers).content).decode("utf-8")
        return r


    
    def restaurant_search(self, query, latitude, longitude, cuisines, price_range, email):
        cuisines = "%2C".join(cuisines.split(","))
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "search?q=" + str(query)  + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&cuisines=" + str(cuisines)+"&sort=rating&order=desc", headers=headers).content).decode("utf-8")
        price=price_range.lower()
        email=email.lower()
        if (price=='high'):
            result=self.searchbyprice(100000,700,r,email)
            return result
        elif (price=='medium'):
            result=self.searchbyprice(700,300,r,email)
            return result
        else:
            result=self.searchbyprice(300,0,r,email)
            return result

    def searchbyprice(self,high,low,r,email):
        #a = ast.literal_eval(r)
        d = json.loads(r)
        restaurant_details = []
        if (email=='no'):
            for restaurant in d['restaurants']:
                response=""
                if (int(low)<int(restaurant['restaurant']['average_cost_for_two'])<=int(high)):
                    response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating "+restaurant['restaurant']['user_rating']['aggregate_rating']
                    restaurant_details.append(response)

                    if (len(restaurant_details)==5):
                        break
                    else:
                        continue
                else:
                    continue
            return restaurant_details
        else:
            for restaurant in d['restaurants']:
                response=""
                if (low<int(restaurant['restaurant']['average_cost_for_two'])<=high):
                    response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with rating "+restaurant['restaurant']['user_rating']['aggregate_rating']+" And price for two "+str(restaurant['restaurant']['average_cost_for_two'])
                    restaurant_details.append(response)
                    if (len(restaurant_details)==10):
                        break
                    else:
                        continue
                else:
                    continue
            return restaurant_details
                    