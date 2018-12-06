import requests




async def scrape(all_aliases):
    print("\n [*] Searching Twitter footprint ..")

    for alias in all_aliases:
        """ Might add a config file to manage all URLS ..
        """
        URL = f'https://twitter.com/{alias}'

        response = requests.get(URL)

        if response.status_code == 404:
            print(f" [*] {URL} returned nothing ..")

        elif response.status_code == 200:
            print(f" [!] {URL} HIT! Logging to output ..")
