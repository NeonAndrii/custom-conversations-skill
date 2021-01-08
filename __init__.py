from mycroft import MycroftSkill, intent_file_handler


class CustomConversations(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('conversations.custom.intent')
    def handle_conversations_custom(self, message):
        available = ''

        self.speak_dialog('conversations.custom', data={
            'available': available
        })


def create_skill():
    return CustomConversations()

