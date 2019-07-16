import requests


class BotBrain:

    URL = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"

    def __init__(self, character=None):
        self.character = character

    def get_currency(self, name):
        currency_list = requests.get(url=BotBrain.URL).json()
        answer = None
        for curr in currency_list:
            if curr["Cur_Abbreviation"] == name[1:]:
                answer = curr
        if answer is None and self.character == "cattle":
            return "There is no such currency you stupid moron"
        elif answer is None:
            return "I'm extremely sorry but there is no such currency"
        elif self.character == "cattle":
            return f"Here is your rate bitch: 1 {name[1:]} = {answer['Cur_OfficialRate']/answer['Cur_Scale']} BYN"
        else:
            return f"It's always a pleasure to help you. 1 {name[1:]} = {answer['Cur_OfficialRate']/answer['Cur_Scale']} BYN"

    def good_buy(self, message):
        if self.character == "cattle":
            if message == "stop it":
                return "Go fuck yourself"
            else:
                return "oooo you're so polite GO.FUCK.YOURSELF"
        else:
            return "Good luck will see ya! (Pronounce it with weird irish accent)"
