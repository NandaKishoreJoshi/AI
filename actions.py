from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
# Import smtplib for the actual sending function
import smtplib,ssl
import re

# Import the email modules we'll need
from email.message import EmailMessage

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_restaurant'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"97e6f2e3d778fbf16eb9a912420cb988"}
        zomato = zomatopy.initialize_app(config)
        price_range=tracker.get_slot('price_range')
        email='No'
        loc = tracker.get_slot('location')
        loc=loc.lower()
        cuisine = tracker.get_slot('cuisine')
        cuisine=cuisine.lower()
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'american':1,'mexican':73}
        results=zomato.restaurant_search("",lat, lon, str(cuisines_dict.get(cuisine)),str(price_range),str(email))
        response=""
        for restaurant in results:
            response=response+restaurant+"\n"
        if (len(results)==0):
            dispatcher.utter_message("Sorry, no restaurants found for your selection. Try something else!!")
            return [SlotSet('location',None),SlotSet('price_range',None),SlotSet('cuisine',None),SlotSet('customer_email',None)]
        else:
            dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]

class ActionSendEmail(Action):
    def name(self):
        return 'action_email'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"97e6f2e3d778fbf16eb9a912420cb988"}
        zomato = zomatopy.initialize_app(config)
        price_range=tracker.get_slot('price_range')
        email='yes'
        loc = tracker.get_slot('location')
        loc =loc.lower()
        customer_email=tracker.get_slot('customer_email')
        cuisine = tracker.get_slot('cuisine')
        cuisine=cuisine.lower()
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'american':1,'mexican':73}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),str(price_range),str(email))
        response=""
        for restaurant in results:
        	response=response+restaurant+"\n"
        dispatcher.utter_message("Sent hotel details to your email.. Hope you are happy!!")
        self.send_email(response,customer_email)
        return [SlotSet('location',loc)]  # For SSL
    
    def send_email(self,msg_content,email_address):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "noreplybot1234@gmail.com"  # Enter your address
        receiver_email = str(email_address)  # Enter receiver address
        password = "1!Bangalore"
        msg = EmailMessage()
        msg.set_content(msg_content)
        msg['Subject'] = "Restaurant Details from Foodie"
        msg['From'] = 'noreplybot1234@gmail.com'
        msg['To'] = str(email_address)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)

                        
class ActionLocationValidator(Action):
    def name(self):
        return 'action_location'
	
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if (loc==None):
            res='Location not recognized. Add in before Location name'
            dispatcher.utter_message(res)
            return [SlotSet('location',None)]
        loc=loc.lower()
        file = open("ZomatoCities.txt", "r")
        doclist = [ line for line in file ]
        cities=doclist[0].split(" ")
        city=[c.lower() for c in cities]
        if ( loc not in city):
            res='we do not serve in this location..!!'
            dispatcher.utter_message(res)
            return [SlotSet('location',None)]
        else :
            res='Its a great place for foodies!!'
            dispatcher.utter_message(res)
            return [SlotSet('location',loc)]          
        #res=('we do not serve in this location.. Thanks!!' if loc not in city else 'Its a great place for foodies!!')
        #dispatcher.utter_message(res)
        #return [SlotSet('location',loc)]
    
class ActionCuisineCheck(Action):
    def name(self):
        return "cuisine_check"

    def run(self,dispatcher,tracker,domain):
        cuisine=tracker.get_slot("cuisine")
        if (cuisine==None):
            dispatcher.utter_message("We do not support search for this cuisine")
            return [SlotSet('cuisine',None)]
        cuisine=cuisine.lower()
        cuisines_list=["chinese","mexican","north indian","south indian","american","italian"]
        if(cuisine not in cuisines_list):
            dispatcher.utter_message("We do not support search for this cuisine")
            return [SlotSet('cuisine',None)]
        return [SlotSet('cuisine',cuisine)]
    
class ActionEmailCheck(Action):
    def name(self):
        return "validate_email"

    def run(self,dispatcher,tracker,domain):
        email_address=tracker.get_slot("customer_email")
        #regex_pattern="^\w+@[a-zA-Z_]+[.a-zA-Z{2,3}]+"
        #x=re.search(regex_pattern, email_address)
        if(email_address==None):
            dispatcher.utter_message("Please provide valid email address")
            return [SlotSet('customer_email',None)]
        return [SlotSet('customer_email',email_address)]

class Actionreset(Action):
    def name(self):
        return "reset_slot"

    def run(self,dispatcher,tracker,domain):
        return [SlotSet('location',None),SlotSet('price_range',None),SlotSet('cuisine',None),SlotSet('customer_email',None)]

