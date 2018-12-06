import requests




async def scrape(all_aliases):
    print("\n [*] Searching League of Legends footprint ..")

    for alias in all_aliases:
        """ Might add a config file to manage all URLS ..
        """
        URL = f'http://na.op.gg/summoner/userName={alias}'

        response = requests.get(URL)

        if response.status_code == 404:
            print(f" [*] {URL} returned nothing ..")

        elif response.status_code == 200:
            print(f" [!] {URL} Summoner found! Logging to output ..")
