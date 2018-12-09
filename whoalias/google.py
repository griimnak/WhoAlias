from urllib.parse import urlencode, urlparse, parse_qs

import requests

from bs4 import BeautifulSoup, SoupStrainer

from ._writer import Output


async def scrape(all_aliases):
    aliases_tested = 0
    aliases_found = 0

    for alias in all_aliases:
        """ Might add a config file to manage all URLS ..
        """
        URL = f"https://google.com/search?q={alias}"

        response = requests.get(URL)

        aliases_tested += 1

        if response.status_code == 404:
            # print(f" [*] {URL} returned nothing ..")
            pass
        elif response.status_code == 503:
            print(" [!] [O] Status code 503 received from google. Connection might be blocked.")
            pass
        elif response.status_code == 200:
            # Count to :param aliases_found:
            aliases_found += 1

            # Writer instance
            out = Output("Google", alias)
            out.write(f"Google summary for {alias}\n")
            # Grab anchors from :param response.text:
            for link in BeautifulSoup(response.text, parse_only=SoupStrainer('a'), features="html.parser"):
                if link.has_attr('href'):
                    # Parse urls
                    if link['href'].startswith("/url?"):
                        url = parse_qs(urlparse(link['href']).query)['q']
                        out.write(url[0])
            # print(f" [>] [>] {URL} .. -> Potential match logged")

    print(f" [*] [O] {aliases_tested} aliases tested, Google summary logged.")
