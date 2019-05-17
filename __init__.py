from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests # for curl
#import urllib, json, urllib2

# General Variables


class TemplateSkill(MycroftSkill):

    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")
        self.test = ''
        self.host = 'http://' + self.settings.get('host') + '/'

    @intent_handler(IntentBuilder("").require("WarmMyCoffee"))
    def handle_warmmycoffee_intent(self, message):
        response = requests.get(self.host+'on')
        if response:
            print('Success!')
            self.speak_dialog("ok")
            self.enclosure.mouth_text('On')
        else:
            print('An error has occurred.')
        self.enclosure.reset()

    @intent_handler(IntentBuilder("").require("DontWarmMyCoffee"))
    def handle_dontwarmmycoffee_intent(self, message):
        response = requests.get(self.host+'off')
        if response:
            print('Success!')
            self.speak_dialog("ok")
            self.enclosure.mouth_text('Off')
        else:
            print('An error has occurred.')
        self.enclosure.reset()

def create_skill():
    return TemplateSkill()

 

