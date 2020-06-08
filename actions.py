
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import psycopg2

# connection sql
def con ():
    connection = psycopg2.connect(user="xdjbqgulyhzhck"
                                  ,password="d8aa4a5f3335d5489970c10428d5adbcd7c7ad5d215ec54b8d0fd8afdaf9b763"
                                  ,host="ec2-52-72-65-76.compute-1.amazonaws.com"
                                  ,port="5432"
                                  ,database="db3kr1a2ptuutr")
    return  connection



# actions_mn
class Actiontuvan(Action):


     def name(self) -> Text:
         return "action_mn"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         x = tracker.get_slot("mn")
         print(x)
         x_main = "SELECT manganh,tennganh,tdn0,tdn1,tdn2,tdn3 FROM indexjob WHERE tennganh = '"
         x_OR_0 = "' OR tdn0 = '"
         x_OR_1 = "' OR tdn1 = '"
         x_OR_2 = "' OR tdn2 = '"
         x_OR_3 = "' OR tdn3 = '"
         x_over = "';"
         x_result = x_main + x + x_OR_0 + x + x_OR_1 + x + x_OR_2 + x + x_OR_3 + x + x_over
         print(x_result)

         cursor = con().cursor()
         cursor.execute(x_result)
         records = cursor.fetchall()
         for lis in records:
             print(lis[1])
             print(lis[0])
             dispatcher.utter_message("Mã ngành của ngành {} là {}".format(lis[1],lis[0]))
         return []

# action_nn

