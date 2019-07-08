import requests
from bs4 import BeautifulSoup


class Something:  # just show my ability to create classes
    def __init__(self, where="Somewhere", how="Somehow", who="Someone", what="Something"):
        self.where = where
        self.how = how
        self.who = who
        self.what = what

    def tell(self):
        print(f"{self.who} {self.where} did {self.what} {self.how}")
        print("Sorre for this inglosh. Let's call it specific accent")

    def __add__(self, other):
        params = {
            "where": self.where + " and " + other.where,
            "how": self.how + " and " + other.how,
            "who": self.who + " with " + other.who,
            "what": self.what + " and " + other.what,
        }
        return Something(**params)

    def __mul__(self, number: int):
        return Something(what=self.what + f" {number} times", who=self.who, where=self.where, how=self.how)


class MyInt(int):
    def __init__(self, *values):
        super().__init__()


def make_beauty_parsing(text):
    bfs = BeautifulSoup(text, 'lxml')
    smth = bfs.find('section', id='lpc-footer-nav').find("h3").text
    print(smth)


def make_parsing():
    url = "https://wordpress.com"
    r = requests.get(url)
    print(f"Headers : {r.headers}")
    with open("page.html", "w") as f:
        f.write(r.text)

    make_beauty_parsing(r.text)


def main():
    
    # funny shit starts
    my_int = MyInt(67.5)
    print(f"My Integer: {my_int}")
    smth1 = Something(who="Woody", where="In Forest", how="Really fast", what="fuck mushrooms")
    smth1 *= 5
    smth2 = Something()
    new_smth = smth1 + smth2
    new_smth.tell()
    # funny shit ends
    
    # parsing with requests
    make_parsing()


if __name__ == "__main__":
    main()

