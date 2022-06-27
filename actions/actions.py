# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict

# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence

class ActionOrderStatusVerify(Action):

    def name(self) -> Text:
        return "action_order_status_verify"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order_number = tracker.get_slot("order_number")
        
        if order_number == "742890907":
            dispatcher.utter_message(text=f"I have your name as Maxwell email address as maxpfeiffer306@hotmail.com and phone number as 4024800686 order number as {order_number}, Is that correct ?")
        elif order_number == "805189262":
            dispatcher.utter_message(
                text=f"I have your name as Mike email address as mmike@gmail.com and phone number as 3925297709 order number as {order_number}, Is that correct ?")
        elif order_number == "978396231":
            dispatcher.utter_message(
                text=f"I have your name as Khai email address as realtorkevinfung@gmail.com and phone number as 6047800280 order number as {order_number}, Is that correct ?")
        elif order_number == None:
            dispatcher.utter_message(text=f"Hey I missed your order number, Would you mind me to repeat that, thanks!")
        else:
            dispatcher.utter_message(text=(f"I don't see any record with the following order number : {order_number}"))
            dispatcher.utter_message(text=f"is there anything else I can help you with?")

        return []

class ActionOrderStatus(Action):

    def name(self) -> Text:
        return "action_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # play rock paper scissors
        print("hey i'm into the action")
        order_number = tracker.get_slot("order_number")
        # data = pd.read_excel(".\\actions\\data.xlsx")

        # data['order_id'] = data['order_id'].astype('str')
        # data['status'] = data['status'].astype('str')
        # data['return'] = data['return'].astype('str')
        # _message_l = data[data['order_id']==order_number]['status'].values.tolist()[0]
        # if len(_message_l) > 0:
        #     for _message in _message_l.split("."):
        #         dispatcher.utter_message(text=_message)
        # else:
        #     dispatcher.utter_message(text=f"Thank you for confirming.")
        #     #dispatcher.utter_message(text=f"Please allow me 2-3 minutes while I check the information and get back to you with a resolution")
        #     dispatcher.utter_message(text=(f"I don't see any record with the following order number : {order_number}"))
        #     dispatcher.utter_message(text=f"is there anything else I can help you with?")
        # return [SlotSet("order_number", None)]
        
        if order_number == "742890907":
            dispatcher.utter_message(text=f"Thank you for confirming.")
            #dispatcher.utter_message(text=f"Please allow me 2-3 minutes while I check the information and get back to you with a resolution")
            dispatcher.utter_message(text=f"Maxwell The order status on your order number is ready to ship")
            dispatcher.utter_message(text=f"However the order estimated ship date is March 29 2022 and estimated delivery date is April 26")
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        elif order_number == "805189262":

            dispatcher.utter_message(text=f"Thank you for confirming.")
            #dispatcher.utter_message(text=f"Please allow me 2-3 minutes while I check the information and get back to you with a resolution")
            dispatcher.utter_message(text=f"Mike I see that your order is in pre-production, we sincerely apologize to you for the delay in delivery of the products you ordered with us. Due to irregularities in the manufacturing department, this inconvenience has been caused to you. We are also flooded with a large number of unexpected orders this month and all this has led to this delay.")
            dispatcher.utter_message(text=f"Not to worry, we will submit an expedite request and we have escalated and this order will be prioritized.")
            dispatcher.utter_message(text=f"However the order estimated ship date is July 21 2022 and estimated delivery date is July 26")
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        elif order_number == "978396231":
            dispatcher.utter_message(text=f"Thank you for confirming.")
            #dispatcher.utter_message(text=f"Please allow me 2-3 minutes while I check the information and get back to you with a resolution")
            dispatcher.utter_message(text=f"Khai I would like to inform you that the order is in ready to ship stage and it completed its production stage")
            dispatcher.utter_message(text=f"However the order estimated ship date is April 20 2022 and estimated delivery date is May 25")
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        else:
            dispatcher.utter_message(text=f"Thank you for confirming.")
            #dispatcher.utter_message(text=f"Please allow me 2-3 minutes while I check the information and get back to you with a resolution")
            dispatcher.utter_message(text=(f"I don't see any record with the following order number : {order_number}"))
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        return [SlotSet("order_number", None)]

class ActionOrderReturns(Action):

    def name(self) -> Text:
        return "action_order_returns"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("hey i'm into the action action_order_returns")
        # name = tracker.get_slot("name")
        order_number = tracker.get_slot("order_number")
        address = tracker.get_slot("address")

        # data = pd.read_excel(".\\actions\\data.xlsx")

        # data['order_id'] = data['order_id'].astype('str')
        # data['status'] = data['status'].astype('str')
        # data['return'] = data['return'].astype('str')

        # _message_l = data[data['order_id']==order_number]['return'].values.tolist()[0]
        # if len(_message_l) > 0:
        #     for _message in _message_l.split("."):
        #         dispatcher.utter_message(text=_message)
        # else:
        #     dispatcher.utter_message(text=(f"I don't see any record with the following order number : {order_number}"))
        #     dispatcher.utter_message(text=f"is there anything else I can help you with?")
        # return [SlotSet("order_number", None), SlotSet("address", None)]

        if order_number == "742890907":
            dispatcher.utter_message(text=f"I have arranged a return request. I have also sent an email with service request number and return details")
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        elif order_number == "805189262":
            dispatcher.utter_message(
                text=f"I have arranged a return request. I have also sent an email with service request number and return details")
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        elif order_number == "978396231":
            dispatcher.utter_message(
                text=f"I have arranged a return request. I have also sent an email with service request number and return details")
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        else:
            dispatcher.utter_message(text=(f"I don't see any record with the following order number : {order_number}"))
            dispatcher.utter_message(text=f"is there anything else I can help you with?")
        return [SlotSet("order_number", None), SlotSet("address", None)]
