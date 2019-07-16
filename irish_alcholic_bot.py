from bot_logic import BotBrain
import requests
import json
from time import sleep

TOKEN = "BlahBlahBlah..."
URL = "https://api.telegram.org/bot" + TOKEN + "/"
START_MESSAGE = r"Do you wanna speak with cattle IrishAlcholic or with polite one? (Print 'cattle' or whatever)"
EXPLANATION = r"Print '/currency_name' to get an official rate. For example '/USD'. Print 'stop it[,please]' to stop it"


def main():
    global last_upd
    last_upd = 0
    message = get_message()
    send_message(message["id"],
                 text=START_MESSAGE)
    bot = BotBrain()
    message = None
    while message is None:
        message = get_message()
        sleep(3)
    if message["message"].lower() == "cattle":
        bot.character = "cattle"
    send_message(message["id"], text=EXPLANATION)
    while True:
        answer = get_message()
        if answer is not None:
            if answer["message"].lower() == "stop it" or answer["message"].lower() == "stop it, please":
                send_message(answer["id"], text=bot.good_buy(answer["message"].lower()))
                break
            else:
                send_message(answer["id"], text=bot.get_currency(name=answer["message"]))
        else:
            sleep(3)
            continue
        sleep(1)


def get_updates():
    url = URL + "GetUpdates"
    r = requests.get(url)
    print(r)
    return r.json()


def get_message():
    r = get_updates()
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


def send_message(chat_id, text):
    url = URL + f"sendmessage?chat_id={chat_id}&text={text}"
    requests.get(url)


if __name__ == "__main__":
    main()

