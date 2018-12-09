import requests




async def scrape(all_aliases):

    for alias in all_aliases:
        """ Might add a config file to manage all URLS ..
        """
        URL = f'http://na.op.gg/summoner/userName={alias}'

        response = requests.get(URL)

        if response.status_code == 404:
            # print(f" [*] {URL} returned nothing ..")
            pass

        elif response.status_code == 200:
            print(f" [>] [>] {URL} Summoner found! Logging to output ..")
