import asyncio
import os

from ._cli import build_aliases_array, splash_text
from .facebook import scrape as fb_scrape
from .github import scrape as gb_scrape
from .instagram import scrape as ig_scrape
from .league import scrape as lg_scrape
from .twitter import scrape as tw_scrape

loop = asyncio.get_event_loop()

class WhoAlias():
    def __init__(self, all_aliases):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n [+] Appending .. "+ str(all_aliases))
        self.all_aliases = all_aliases

        try:
            loop.run_until_complete(self.main())
        except Exception as e:
            exit(str(e))
        finally:
            loop.close()

    async def main(self):
        print(" [*] Initializing WhoAlias.main() ..")
        # Social medias
        # Facebook scrape
        t1 = loop.create_task(fb_scrape(self.all_aliases))
        # Twitter scrape
        t2 = loop.create_task(tw_scrape(self.all_aliases))
        # Github scrape
        t3 = loop.create_task(gb_scrape(self.all_aliases))
        # Instagram scrape
        t4 = loop.create_task(ig_scrape(self.all_aliases))

        # Games
        # # League of Legends scrape
        t5 = loop.create_task(lg_scrape(self.all_aliases))

        await asyncio.wait([t1, t2, t3, t4, t5])
        return t1, t2, t3, t4, t5


def run():
    # Clear console and display splash
    os.system('cls' if os.name == 'nt' else 'clear')
    print(splash_text)

    # Build aliases array
    aliases = build_aliases_array()

    # Initialize
    WhoAlias(aliases)


