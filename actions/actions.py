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
from rasa_sdk.events import EventType, SlotSet
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
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        pattern = r'^[a-zA-Z]+([-\'\s][a-zA-Z]+)*$'
        name = slot_value
        if re.match(pattern, name):
            print("full_name:"+ name)
            return {"full_name": name}

        dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
        print("full_name: None")
        return {"full_name": None}
    

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_submit",
                                 Name=tracker.get_slot("full_name"))