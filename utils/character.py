from main import client


class Character:
    _instances = {}

    def __init__(self, user_id):
        self.chat = await client.chat.new_chat(
            char="rFKvc0ejXz_X4w7hXDhrDjtkve0GTf-cuetnkImRCDQ")

    def __call__(cls, *args, **kwargs):
        if kwargs["user_id"] not in cls._instances:
            cls._instances[kwargs["user_id"]] = super(Character, cls).__call__(*args, **kwargs)
            cls._instances[kwargs["user_id"]].__init__(*args, **kwargs)
        return cls._instances[kwargs["user_id"]]

    async def reply_to_bot(self, text):
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
