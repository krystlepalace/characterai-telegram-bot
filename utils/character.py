from main import client


class Character:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if str(kwargs["user_id"]) not in cls._instances:
            cls._instances[str(kwargs["user_id"])] = super(Character, cls).__new__(cls)
            cls._instances[str(kwargs["user_id"])].__init(*args, **kwargs)
        return cls._instances[str(kwargs["user_id"])]

    def __init(self, user_id=None, character=None):
        self.user_id = user_id
        self.chat = None
        self.character = character

    async def reply_to_bot(self, text):
        if self.chat is None:
            self.chat = await client.chat.new_chat(
                char=self.character)
        participants = self.chat['participants']

        if not participants[0]['is_human']:
            tgt = participants[0]['user']['username']
        else:
            tgt = participants[1]['user']['username']

        data = await client.chat.send_message(
            self.chat['external_id'], tgt, text
        )

        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']

        return f"{name}: {text}"

    async def change_char(self, character):
        self.chat = None
        self.character = character
