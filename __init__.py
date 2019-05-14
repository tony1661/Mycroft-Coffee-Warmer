from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests # for curl
#import urllib, json, urllib2

# General Variables
host = 'http://192.168.40.186/'

class TemplateSkill(MycroftSkill):

    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")
        self.test = ''

    @intent_handler(IntentBuilder("").require("WarmMyCoffee"))
    def handle_warmmycoffee_intent(self, message):
        response = requests.get(host+'on')
        if response:
            print('Success!')
            self.speak_dialog("ok")
        else:
            print('An error has occurred.')

    @intent_handler(IntentBuilder("").require("DontWarmMyCoffee"))
    def handle_dontwarmmycoffee_intent(self, message):
        response = requests.get(host+'off')
        if response:
            print('Success!')
            self.speak_dialog("ok")
        else:
            print('An error has occurred.')

def create_skill():
    return TemplateSkill() 

