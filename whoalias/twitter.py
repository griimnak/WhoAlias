import requests

from ._writer import Output



async def scrape(all_aliases):
    aliases_tested = 0
    aliases_found = 0

    for alias in all_aliases:
        """ Might add a config file to manage all URLS ..
        """
        URL = f'https://twitter.com/{alias}'

        response = requests.get(URL)

        aliases_tested += 1

        if response.status_code == 404:
            # print(f" [*] {URL} returned nothing ..")
            pass

        elif response.status_code == 200:
            # Count to :param aliases_found:
            aliases_found += 1

            # Writer instance
            out = Output("Twitter", alias)
            out.write(f"Potential Twitter account for {alias}: {URL}")
            # print(f" [>] [>] {URL} .. -> Potential match logged")

    print(f" [*] [T] {aliases_tested} aliases tested, {aliases_found} potential Twitter matches logged.")
