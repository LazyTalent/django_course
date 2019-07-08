import requests


def main():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    page = requests.get(url)
    data = page.json()
    for cur in data:
        print(f"On {cur['Date']} 1 BYN is {cur['Cur_OfficialRate']} {cur['Cur_Abbreviation']}")


if __name__ == "__main__":
    main()

