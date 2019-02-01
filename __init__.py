#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:17:28 2019

@author: hridul.gupta
"""

import requests
import json
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
__author__ = 'eward'

LOGGER = getLogger(__name__)


class CorrectSkill(MycroftSkill):
    def __init__(self):
        super(CorrectSkill, self).__init__(name="CorrectSkill")

    def initialize(self):

        detail_event_intent = IntentBuilder("DetailEventIntent"). \
            require("DetailEventKeyword").build()
        self.register_intent(detail_event_intent,
                             self.handle_detail_event_intent)

    def handle_detail_event_intent(self, message):

        url = "https://ip0rzvwy82.execute-api.us-east-1.amazonaws.com/Test/mycroft-skill-emp-details"

        payload = "{\n\t\"inputparams\":\"hridul gupta\"\n}"
        headers = {
            'Content-Type': "application/json",
            'Host': "ip0rzvwy82.execute-api.us-east-1.amazonaws.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        data2 = json.loads(data['body'])
        id_emp = data2['emp_id']
        designation=data2['designation']
        location=data2['location']
        birth_date=data2['birth_date']
        joining_date=data2['joining_date']
        self.speak_dialog("Employee ID,{} , Designation , {}, location, {} , Birth Date , {} , Joining date, {}".format(id_emp,designation,location,birth_date,joining_date))
    
    def stop(self):
         pass
    


def create_skill():
    return CorrectSkill()
        
