# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
import requests
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import json

__author__ = 'eward'

LOGGER = getLogger(__name__)


class CorrectSkill(MycroftSkill):
    def __init__(self):
        super(CorrectSkill, self).__init__(name="CorrectSkill")

    def initialize(self):

        detail_event_intent = IntentBuilder("DetailEventIntent"). \
            require("DetailEventKeyword").build()
        self.register_intent(detail_event_intent, self.handle_detail_event_intent)



    def handle_detail_event_intent(self, message):
        url = "https://ip0rzvwy82.execute-api.us-east-1.amazonaws.com/Test/mycroft-skill-emp-details"
        payload = "{\n\t\"inputparams\":\"hridul gupta\"\n}"
	headers = {'Content-Type': "application/json",
    	'Host': "ip0rzvwy82.execute-api.us-east-1.amazonaws.com"
    	}
        response = requests.request("POST", url, data=payload, headers=headers)
        data = json.loads(response.text)
        data2 = json.loads(data['body'])
        id_emp=data2['emp_id']
        self.speak_dialog("Today in history event {} occured".format(id_emp)

    

    def stop(self):
        pass


def create_skill():
    return CorrectSkill()
