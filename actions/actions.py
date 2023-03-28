# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import phonenumbers
import re


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"
        # return "comapany_website_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        Link = "https://nevrio.tech/"
        # dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_template("utter_info",tracker,link=Link)

        return []
    

def clean_name(name):
    return "".join([c for c in name if c.isalpha()])    

class ValidateInfoForm(FormValidationAction):

    def name(self) -> Text:

        return "validate_info_form"
    

    def validate_full_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'full_name' value."""
        
        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text= "That must've been a typo.")
            return {"full_name": None}
        return {"full_name": name}
    
    
    
    def validate_email_id(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        # full_name = tracker.get_slot("full_name")

        email = slot_value

        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

        if re.match(pat,email):
            dispatcher.utter_message(text= f"Thank {full_name}")
            return {"email_id": email}
        return {"email_id": None}
    
    
    def validate_phone_number(self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'phone_number' value."""

        # full_name = tracker.get_slot("full_name")
        # email_id = tracker.get_slot("email_id")

    
        if phonenumbers.parse(slot_value):
            
            number = slot_value
            dispatcher.utter_message(text= f"Thank you {full_name} for your Email Id {email_id}.")
            return {"phone_number": number}
        
        dispatcher.utter_message(text= f"Please enter correct phone number.")
        return {"phone_number": None}
        


        