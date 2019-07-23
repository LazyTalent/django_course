from bot.bot_logic import BotBrain
from bot.bot_exceptions import *
import requests
from time import sleep


class IrishAlcholicBot:
    TOKEN = "840417277:AAHifTr8MUHpmnQftL4eSqJA6exdrSnF-N0"
    URL = "https://api.telegram.org/bot" + TOKEN + "/"
    START_MESSAGE = r"Do you wanna speak with cattle IrishAlcholic or with polite one? (Print 'cattle' or whatever)"
    EXPLANATION = r"Print '/currency_name' to get an official rate. For example '/USD'. Print 'stop it[,please]' to stop it"

    def __init__(self, chat_id, custom_start=False):
        global last_upd
        last_upd = 0
        if chat_id is None:
            raise ChatIdNotFoundError("Chat Id is None")
        self.chat_id = chat_id
        self.brain = BotBrain()
        if not custom_start:
            self.start()

    def start(self):
        IrishAlcholicBot._get_message()
        self.send_message(text=IrishAlcholicBot.START_MESSAGE)
        message = None
        while message is None:
            message = IrishAlcholicBot._get_message()
            sleep(3)
        if message["message"].lower() == "cattle":
            self.brain.character = "cattle"

        self.send_message(text=IrishAlcholicBot.EXPLANATION)
        self.conversation()

    def send_message(self, text):
        url = IrishAlcholicBot.URL + f"sendmessage?chat_id={self.chat_id}&text={text}"
        requests.get(url)

    @staticmethod
    def _get_message():
        r = IrishAlcholicBot._get_updates()
        last_obj = r["result"][-1]
        curr_update_id = last_obj["update_id"]
        global last_upd
        if last_upd != curr_update_id:
            last_upd = curr_update_id
            chat_id = last_obj["message"]["chat"]["id"]
            message_text = last_obj["message"]["text"]
            message = {"id": chat_id,
                       "message": message_text}
            return message

        return None

    @staticmethod
    def _get_updates():
        url = IrishAlcholicBot.URL + "GetUpdates"
        r = requests.get(url)
        #  print(r)
        return r.json()

    def conversation(self):
        while True:
            answer = IrishAlcholicBot._get_message()
            if answer is not None:
                if answer["message"].lower() == "stop it" or answer["message"].lower() == "stop it, please":
                    self.send_message(text=self.brain.good_buy(answer["message"].lower()))
                    break
                elif answer["message"].lower()[:18] == "i really wanna see":
                    try:
                        number = int(answer["message"][19:])
                        self.send_previous_message(number=number)
                    except ValueError:
                        self.send_message(text=self.brain.bad_number(answer["message"][19:]))
                else:
                    self.send_message(text=answer["message"].lower()[:18])
                    self.send_message(text=self.brain.get_currency(name=answer["message"]))
            else:
                sleep(3)
                continue
            sleep(1)

    def send_previous_message(self, number):
        r = IrishAlcholicBot._get_updates()
        try:
            message = r["result"][-number]["message"]["text"]
            self.send_message(text=self.brain.previous_message(message))
        except IndexError:
            self.send_message(text=self.brain.bad_number(number))


