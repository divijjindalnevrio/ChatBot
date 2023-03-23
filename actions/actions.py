# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction


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
    
# class ActionFormInfo(FormAction):

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "form_info"
    
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""

#         return ["name", "phone_number", "email_id"]

#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {}

        
